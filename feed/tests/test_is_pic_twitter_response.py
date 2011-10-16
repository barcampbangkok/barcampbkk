#from django.test import TestCase
#from feed.fetch_twitter import is_pic_twitter_response
#from mock import Mock
#
#class TestIsPicTwitterResponse(TestCase):
#    def test_is_pic_twitter_response_is_true_for_pic_twitter(self):
#        location = 'http://twitter.com/#!/igoyz/status/114975438018842624/photo/1'
#        response = Mock()
#        response.get = Mock(return_value = location)
#        self.assertTrue(is_pic_twitter_response(response))
#
#    def test_is_pic_twitter_response_is_false_for_twitpic(self):
#        location = 'http://twitpic.com/6m2t75'
#        response = Mock()
#        response.get = Mock(return_value = location)
#        self.assertFalse(is_pic_twitter_response(response))
#
