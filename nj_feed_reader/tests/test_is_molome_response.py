from django.test import TestCase
from nj_feed_reader.fetch_twitter import is_molome_response
from mock import Mock

class TestIsTwitpicResponse(TestCase):
    def test_is_molome_response_is_true_for_molome(self):
        location = 'http://molo.me/p/2uvG77'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertTrue(is_molome_response(response))

    def test_is_twitpic_response_is_false_for_lockerz(self):
        location = 'http://lockerz.com/s/139183852'
        response = Mock()
        response.get = Mock(return_value = location)
        self.assertFalse(is_molome_response(response))

