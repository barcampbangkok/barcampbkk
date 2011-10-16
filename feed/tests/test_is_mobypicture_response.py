from django.test import TestCase
from feed.fetch_twitter import is_mobypicture_response
from mock import Mock

class TestIsMobypictureResponse(TestCase):
    def test_is_mobypicture_response_is_true_for_mobypicture(self):
        location = 'http://www.mobypicture.com/user/marnixamsterdam/view/10743416'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertTrue(is_mobypicture_response(response))

    def test_is_mobypicture_response_is_false_for_twitpic(self):
        location = 'http://twitpic.com/6m2t75'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertFalse(is_mobypicture_response(response))