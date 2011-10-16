from django.test import TestCase
from feed.fetch_twitter import is_twitgoo_response
from mock import Mock

class TestIsLockerzResponse(TestCase):
    def test_is_twitgoo_response_is_true_for_twitgoo(self):
        location = 'http://twitgoo.com/4j88ih'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertTrue(is_twitgoo_response(response))

    def test_is_twitgoo_response_is_false_for_twitpic(self):
        location = 'http://twitpic.com/6m2t75'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertFalse(is_twitgoo_response(response))