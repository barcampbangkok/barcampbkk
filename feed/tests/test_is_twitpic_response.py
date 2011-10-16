from django.test import TestCase
from feed.fetch_twitter import is_twitpic_response
from mock import Mock

class TestIsTwitpicResponse(TestCase):
    def test_is_twitpic_response_is_true_for_twitpic(self):
        location = 'http://twitpic.com/6m2t75'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertTrue(is_twitpic_response(response))

    def test_is_twitpic_response_is_false_for_lockerz(self):
        location = 'http://lockerz.com/s/139183852'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertFalse(is_twitpic_response(response))
        
