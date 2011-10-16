from django.test import TestCase
from feed.fetch_twitter import is_imgly_response
from mock import Mock

class TestIsImglyResponse(TestCase):
    def test_is_imgly_response_is_true_for_imgly(self):
        location = 'http://img.ly/8mZP'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertTrue(is_imgly_response(response))

    def test_is_imgly_response_is_false_for_twitpic(self):
        location = 'http://twitpic.com/6m2t75'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertFalse(is_imgly_response(response))