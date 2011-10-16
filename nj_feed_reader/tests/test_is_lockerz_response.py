from django.test import TestCase
from nj_feed_reader.fetch_twitter import is_lockerz_response
from mock import Mock

class TestIsLockerzResponse(TestCase):
    def test_is_lockerz_response_is_true_for_lockerz(self):
        location = 'http://lockerz.com/s/139183852'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertTrue(is_lockerz_response(response))

    def test_is_lockerz_response_is_false_for_twitpic(self):
        location = 'http://twitpic.com/6m2t75'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertFalse(is_lockerz_response(response))
        
