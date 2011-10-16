from django.test import TestCase
from feed.fetch_twitter import is_owly_response
from mock import Mock

class TestIsOwlyResponse(TestCase):
    def test_is_owly_response_is_true_for_owly(self):
        location = 'http://ow.ly/i/e0gW'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertTrue(is_owly_response(response))

    def test_is_owly_response_is_false_for_twitpic(self):
        location = 'http://twitpic.com/6m2t75'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertFalse(is_owly_response(response))