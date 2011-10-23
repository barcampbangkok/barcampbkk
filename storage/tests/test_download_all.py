from django.test import TestCase
from storage.image_utils import download_all

class TestDownload(TestCase):
    def test_download_all_returns_list_of_image_paths(self):
        image_urls = ['http://p.twimg.com/AZh5jT2CEAAXyR-.jpg:large',
                      'http://distillery.s3.amazonaws.com/media/2011/09/17/bf5bb54387ca4dd98573128bb02f5c0b_7.jpg',
                      'http://d3-05.twitpicproxy.com/photos/large/399879761.jpg'] 
        image_paths = download_all(image_urls)
        print 'test image_paths = ', image_paths 
        expected = [u'httpp.twimg.comAZh5jT2CEAAXyR-.jpglarge',
                    u'httpdistillery.s3.amazonaws.commedia20110917bf5bb54387ca4dd98573128bb02f5c0b_7.jpg',
                    u'httpd3-05.twitpicproxy.comphotoslarge399879761.jpg']
        self.assertEqual(expected, image_paths)

