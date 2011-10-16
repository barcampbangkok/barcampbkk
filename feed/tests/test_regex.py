from django.test import TestCase
from feed.regex import get_image_url_from_raw_html
from feed.tests.regex_test_content import raw_content

class TestGetImage(TestCase):
    def test_get_nothing__content_is_empty(self):
        raw_content = ''
        regex_text='id="photo-display" src="(?P<src>.+?)"'
        response = get_image_url_from_raw_html( raw_content, regex_text )
        self.assertEqual(None, response)

    def test_get_nothing__not_found(self):
        regex_text='id="photo-display" src="(?P<src>.+?)"'
        raw_content = '<html><body>I like unit testing</body></html>'
        response = get_image_url_from_raw_html( raw_content, regex_text )
        self.assertEqual(None, response)

    def test_get_url(self):
        regex_text='id="photo-display" src="(?P<src>.+?)"'
        expected_result = "http://s3.amazonaws.com/twitpic/photos/large/29483605.png?AWSAccessKeyId=AKIAJF3XCCKACR3QDMOA&Expires=1316184447&Signature=gOXGQ9bmYWhdFvdOhKls658AwnY%3D"
        response = get_image_url_from_raw_html( raw_content, regex_text )
        self.assertEqual( expected_result, response)
        
