from django.conf import settings
from django.core.files.storage import default_storage
from django.test import TestCase
from storage.image_utils import create_thumbnail

class TestCreateThumbnail(TestCase):
    def test_thumbnail_exists_after_created(self):
        image_name = 'test.jpg'
        
        path = create_thumbnail(image_name) 

        self.assertTrue(default_storage.exists(path))

    def test_thumbnail_created_at_right_path(self):
        image_name = 'test.jpg'

        created_path = create_thumbnail(image_name) 

        thumbnail_path = 'collected_twitter_images/thumbnails/' + image_name
        expected_path = default_storage.path(thumbnail_path)
        self.assertEqual(created_path, expected_path)

        
