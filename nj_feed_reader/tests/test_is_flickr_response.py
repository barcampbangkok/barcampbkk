from django.test import TestCase
from nj_feed_reader.fetch_twitter import is_flickr_response
from mock import Mock

class TestIsLockerzResponse(TestCase):
    def test_is_flickr_response_is_true_for_flickr(self):
        location = 'http://www.flickr.com/photos/63701352@N06/6158805817/'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertTrue(is_flickr_response(response))

    def test_is_flickr_response_is_false_for_twitpic(self):
        location = 'http://twitpic.com/6m2t75'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertFalse(is_flickr_response(response))