from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from httplib2 import Http, RelativeURIError
from PIL import Image
from StringIO import StringIO
import logging
from nj_feed_reader.models import Photo, Tweet

TWITTER_IMAGE_PATH = 'collected_twitter_images/'
THUMBNAIL_PATH = TWITTER_IMAGE_PATH + 'thumbnails/' 
THUMBNAIL_SIZE = 60, 38

client = Http()
log = logging.getLogger(__name__)

def collect_images_and_text():
    photos = Photo.objects.order_by('-tweet__created_at')
    photo_list=[]
    for photo in photos:
        if photo.tweet.lat:
            location_link = "<a href='http://maps.google.com/maps?q=%s,%s' target='_blank'>(location)</a>" % (photo.tweet.lat,photo.tweet.long)
        else:
            location_link = ""
        photo_dict = {'image':photo.name,'text':photo.tweet.text,'location_link':location_link}
        photo_list.append(photo_dict)
    return photo_list

def collected_images():
    dir_names, file_names = default_storage.listdir(TWITTER_IMAGE_PATH)
    compare_by_created_time = lambda(name): default_storage.created_time(TWITTER_IMAGE_PATH + name)
    file_names.sort(key=compare_by_created_time, reverse=True)
    return file_names 

def create_thumbnail(image_name):
    image_path = default_storage.path(TWITTER_IMAGE_PATH + image_name)
    image = Image.open(image_path)
    image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
    thumbnail_path = default_storage.path(THUMBNAIL_PATH + image_name)
    #if (image_path.lower()).find('jpg') <= -1:
    #    thumbnail_path=thumbnail_path+'.jpg'
    image.save(thumbnail_path,'JPEG')
    return thumbnail_path

def save_image(image_name, content):
    if not image_name.lower().endswith('.jpg'):
        image_name = image_name+'.jpg'
    verifying_image = Image.open(ContentFile(StringIO(content).buf))
    verifying_image.verify()
    # verify occationally cause image.fp to be None -*-
    image = Image.open(ContentFile(StringIO(content).buf))
    image_path = default_storage.path(TWITTER_IMAGE_PATH + image_name)

    print
    print
    print 'save image'
    print image.save(image_path,'JPEG')
    #image.save(image_path)
    create_thumbnail(image_name)

def download_all(image_urls):
    image_names = []
    for image_url in image_urls:
        try:
            image_name = download(image_url)
            if image_name is not None:
                image_names.append(image_name)
        except RelativeURIError:
            log.error('cannot d/l image from url %s' % image_url)
    return image_names

def download(image_url):
    response, content = client.request(image_url)
    
    #if response.status == 200 and response.get('content-type', None) == 'image/jpeg':
    if response.status == 200:
        image_url = image_url.split('?')[0] # chop the query string out
        image_name = default_storage.get_valid_name(image_url) 
        image_path = TWITTER_IMAGE_PATH + image_name
        if not default_storage.exists(image_path):
            log.info('saving image name = %s' % image_path)
            save_image(image_name, content)
        return image_name
    else:
        log.error('%s %s' % (response.status, response.get('content-type', None)))
        return None

