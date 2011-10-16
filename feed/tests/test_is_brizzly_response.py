from django.test import TestCase
from feed.fetch_twitter import is_brizzly_response
from mock import Mock

class TestIsBrizzlyResponse(TestCase):
    def test_is_brizzly_response_is_true_for_brizzly(self):
        location = 'http://brizzly.com/pic/2SE5'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertTrue(is_brizzly_response(response))

    def test_is_brizzly_response_is_false_for_twitpic(self):
        location = 'http://pics.brizzly.com/2SE5.jpg'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertFalse(is_brizzly_response(response))