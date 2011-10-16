from datetime import datetime
from django.test import TestCase
from nj_feed_reader.models import Tweet

class TestTweet(TestCase):
    def test_from_dict_to_model(self):
        tweet_json = { 'text': "@roofimon lets see if wp really anti-TDD",
                       'created_at': "Sun, 25 Sep 2011 14:45:05 +0000",
                       'id_str': "117972896940437504",
                       'profile_image_url': "http://a0.twimg.com/profile_images/1097051928/mypic2_normal.jpeg",
                       'from_user': "juacompe",
                     }
        created_at_str = tweet_json['created_at'] + ' UTC' # +0000 = UTC
        created_at = datetime.strptime(created_at_str, '%a, %d %b %Y %H:%M:%S +0000 %Z')
        tweet_json.update({'created_at': created_at})
        tweet = Tweet(**tweet_json) 
        tweet.save()
        self.assertTrue(tweet.id)


