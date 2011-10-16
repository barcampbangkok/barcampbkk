from django.test import TestCase
from feed.fetch_twitter import is_yfrog_response
from mock import Mock

class TestIsyfrogResponse(TestCase):
    def test_is_yfrog_response_is_true_for_yfrog(self):
        location = 'http://yfrog.com/kg95174314j'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertTrue(is_yfrog_response(response))

    def test_is_yfrog_response_is_false_for_lockerz(self):
        location = 'http://lockerz.com/s/139183852'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertFalse(is_yfrog_response(response))
        
