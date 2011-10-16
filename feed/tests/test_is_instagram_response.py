from django.test import TestCase
from feed.fetch_twitter import is_instagram_response
from mock import Mock

class TestIsLockerzResponse(TestCase):
    def test_is_instagram_response_is_true_for_instagram(self):
        location = 'http://instagr.am/p/Ncasw/'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertTrue(is_instagram_response(response))

    def test_is_instagram_response_is_false_for_twitpic(self):
        location = 'http://twitpic.com/6m2t75'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertFalse(is_instagram_response(response))