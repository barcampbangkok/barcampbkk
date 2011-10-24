from django.test import TestCase
from mock import Mock
from storage import image_utils

class TestHome(TestCase):
    def setUp(self):
        images = ['132883093_49660b8f2a_z.jpg',
                  '399107666.jpg',
                  '2957442267_6afce8dd8f_z.jpg',
                  '5975249429_4c076b25c1_z.jpg',
                  '6041022237_287ede031f_z.jpg',]
        self.orig = image_utils.collected_images
        image_utils.collected_images = Mock(return_value = images)

    def tearDown(self):
        image_utils.collected_images = self.orig

    def test_home_ok(self):
        response = self.client.get('/twitter_feeds/')
        self.assertEqual(200, response.status_code)

    def test_home_has_images_in_context(self):
        response = self.client.get('/twitter_feeds/')
        images = image_utils.collected_images()
        self.assertEqual(images, response.context['images'])
        
    def test_home_has_image_url_in_context(self):
        response = self.client.get('/twitter_feeds/')
        self.assertTrue(response.context['IMAGE_URL'])

    def test_home_has_thumbnial_url_in_context(self):
        response = self.client.get('/twitter_feeds/')
        self.assertTrue(response.context['THUMBNAIL_URL'])
