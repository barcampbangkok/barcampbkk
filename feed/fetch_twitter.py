from datetime import datetime
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db.transaction import commit_on_success
from django.db.utils import IntegrityError, DatabaseError
from feed.models import Tweet, Photo
from feed.regex import get_image_url_from_raw_html
from httplib import BadStatusLine
from httplib2 import Http, ServerNotFoundError
from json import loads
from storage.image_utils import download_all 
import logging

client = Http()
log = logging.getLogger(__name__)

def fetch_twitter():
    response, content = fetch_tweets()
    if response.status == 200:
        write_to_file(content)
        parse_tweets(loads(content))
    
def fetch_tweets():
    """
    Fetch tweets according to TWITTER_QUERY in django's settings and return
    response and python dict of the returned tweets.
    """
    query = settings.TWITTER_QUERY
    twitter_search_url = 'http://search.twitter.com/search.json?q=%s' % query
    response, content = client.request(twitter_search_url) 
    return response, content

def write_to_file(content):
    """
    Write `content` into /media/search.json
    """
    #delete current search.json
    default_storage.delete('search.json')
    #save new content to search.json, so search.json has the latest content from twitters
    path = default_storage.save('search.json', ContentFile(content))

@commit_on_success
def parse_tweets(result_dict):
    results = result_dict['results']
    messages = []
    for result in results:
        # update timezone of created_at
        created_at_str = result['created_at'] + ' UTC' # +0000 = UTC
        created_at = datetime.strptime(created_at_str, '%a, %d %b %Y %H:%M:%S +0000 %Z')
        result.update({'created_at': created_at})
        # save into database
        try:
            tweet_json = {}
            tweet_json['text'] = result['text']
            tweet_json['created_at'] = result['created_at']
            tweet_json['id_str'] = result['id_str']
            tweet_json['profile_image_url'] = result['profile_image_url']
            tweet_json['from_user'] = result['from_user']
            if result['geo']:
                tweet_json['lat'] = result['geo']['coordinates'][0]
                tweet_json['long'] = result['geo']['coordinates'][1]
            tweet = Tweet(**tweet_json)
            tweet.save()
            # download photos in the tweet
            urls = find_url_in_tweet(tweet.text)
            image_urls = extract_urls_from_tweet(urls)
            photos = download_all(image_urls)
            for photo_name in photos:
                photo = Photo(name = photo_name, tweet = tweet)
                photo.save()
        except (IntegrityError, DatabaseError):
            pass # tweet already saved

        messages.append(result['text'])
    return messages

def extract_urls_from_tweet(urls):
    image_urls = []
    for url in iter(urls):
        try:
            image_url = find_image_url_in_page(url)
        except ServerNotFoundError, e:
            log.error('fail to find photo in url %s' % url)
            log.exception(e)
        except BadStatusLine, e:
            log.error('fail to find photo in url %s' % url)
            log.exception(e)
                
        if image_url is not None:
            image_urls.append(image_url)
    return image_urls

def find_image_url_in_page(url):
    """
    Open the page, find the photo in the page, and return url of the photo 
    image.
    """
    response, content = client.request(url)
    image_url = None
    if is_twitpic_response(response):
        regex_text='id="photo-display" src="(?P<src>.+?)"'
        image_url = get_image_url_from_raw_html(content, regex_text)
    elif is_lockerz_response(response):
        regex_text='id="photo" src="(?P<src>.+?)"'
        image_url = get_image_url_from_raw_html(content, regex_text)
#    elif is_pic_twitter_response(response):
#        regex_text='src="(?P<src>.+?)" alt="pic.twitter.com.'
#        image_url = get_image_url_from_raw_html(content, regex_text)
    elif is_yfrog_response(response):
        regex_text='id="main_image" src="(?P<src>.+?)"'
        image_url = get_image_url_from_raw_html(content, regex_text)
    elif is_molome_response(response):
        regex_text='src="(?P<src>.+?)" alt="Photo"'
        image_url = get_image_url_from_raw_html(content, regex_text)
    elif is_picplz_response(response):
        regex_text='src="(?P<src>.+?)" width="\d+" height="\d+" id="mainImage"'
        image_url = get_image_url_from_raw_html(content, regex_text)
    elif is_instagram_response(response):
        regex_text='class="photo" src="(?P<src>.+?)"'
        image_url = get_image_url_from_raw_html(content, regex_text)
    elif is_flickr_response(response):
        regex_text='src="(?P<src>.+?)" alt="photo"'
        image_url = get_image_url_from_raw_html(content, regex_text)
    elif is_twitgoo_response(response):
        regex_text='id="fullsize" src="(?P<src>.+?)"'
        image_url = get_image_url_from_raw_html(content, regex_text)
    elif is_imgly_response(response):
        regex_text='id="the-image" src="(?P<src>.+?)"'
        image_url = get_image_url_from_raw_html(content, regex_text)
    elif is_mobypicture_response(response):
        regex_text='src="(?P<src>.+?)" id="main_picture"'
        image_url = get_image_url_from_raw_html(content, regex_text)
    elif is_owly_response(response):
        regex_text='</?a+\s+href+[^>]+title="View original size"+[^>]*>+\s+</?img\s+src="(?P<src>.+?)"'
        image_url = get_image_url_from_raw_html(content, regex_text)
    elif is_brizzly_response(response):
        regex_text='</?div+\s+class="picture r"+[^>]*>+\s+</?a+\s+href+[^>]*><img+\s+src="(?P<src>.+?)"'
        image_url = get_image_url_from_raw_html(content, regex_text)
    return image_url
    
def is_twitpic_response(response):
    location = response.get('content-location', '')
    return location.find('http://twitpic.com') > -1

def is_lockerz_response(response):
    location = response.get('content-location','')
    return location.find('http://lockerz.com') > -1

def is_yfrog_response(response):
    location = response.get('content-location','')
    return location.find('http://yfrog.com') > -1

def is_molome_response(response):
    location = response.get('content-location','')
    return location.find('http://molo.me') > -1

def is_picplz_response(response):
    location = response.get('content-location','')
    return location.find('http://picplz.com') > -1

def is_instagram_response(response):
    location = response.get('content-location','')
    return location.find('http://instagr.am/') > -1

def is_flickr_response(response):
    location = response.get('content-location','')
    return location.find('http://www.flickr.com') > -1

def is_twitgoo_response(response):
    location = response.get('content-location','')
    return location.find('http://twitgoo.com/') > -1

def is_imgly_response(response):
    location = response.get('content-location','')
    return location.find('http://img.ly') > -1

def is_mobypicture_response(response):
    location = response.get('content-location','')
    return location.find('http://www.mobypicture.com') > -1

def is_owly_response(response):
    location = response.get('content-location','')
    return location.find('http://ow.ly') > -1

def is_brizzly_response(response):
    location = response.get('content-location','')
    return location.find('http://brizzly.com') > -1
#def is_pic_twitter_response(response):
#    location = response.get('content-location','')
#    is_twitter = location.find('http://twitter.com') > -1
#    has_photo = location.find('/photo/') > -1
#    return is_twitter and has_photo

def find_url_in_tweet(text):
    words = text.split(' ')
    urls = [ word for word in words if word.count('http://') ]
    return urls 

