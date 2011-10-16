from django.core.files.storage import default_storage
from django.test import TestCase
from storage.image_utils import download, TWITTER_IMAGE_PATH, THUMBNAIL_PATH 

class TestDownload(TestCase):
    def setUp(self):
        image_name = 'https1.proxy03.twitpic.comphotoslarge399879761.jpg'
        self.image_path = TWITTER_IMAGE_PATH + image_name
        self.thumb_image_path = THUMBNAIL_PATH + image_name

    def tearDown(self):
        default_storage.delete(self.image_path)
        default_storage.delete(self.thumb_image_path)
        
    # integration test
    def test_download__success(self):
        """
        Scenario: Download image, should download the image
        Expected:
        - image saved in collected images and 
        - its thumbnail is generated
        """
        url = 'http://s1.proxy03.twitpic.com/photos/large/399879761.jpg'
        download(url)
        self.assertTrue(default_storage.exists(self.image_path))
        self.assertTrue(default_storage.exists(self.thumb_image_path))

    def test_download_does_not_save_new_image_if_exist(self):
        """
        Scenario: Download existing image
        Expected:
        - created time of the image is not changed (image is *not* saved twice)
        - created time of the thumbnail is not changed (its thumbnail is *not* generated again)
        """
        url = 'http://s1.proxy03.twitpic.com/photos/large/399879761.jpg'
        download(url)
        image_created_time1 = default_storage.created_time(self.image_path)
        thumb_created_time1 = default_storage.created_time(self.thumb_image_path)
        download(url)
        image_created_time2  = default_storage.created_time(self.image_path)
        thumb_created_time2 = default_storage.created_time(self.thumb_image_path)
        self.assertEqual(image_created_time1, image_created_time2)
        self.assertEqual(thumb_created_time1, thumb_created_time2)

