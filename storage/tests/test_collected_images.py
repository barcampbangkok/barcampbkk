from django.test import TestCase
from django.core.files.storage import default_storage
from storage.image_utils import collected_images, TWITTER_IMAGE_PATH
from time import sleep

class TestCollectedImages(TestCase):
    def setUp(self):
        # generate sample image
        image_name = 'test.jpg'
        image_path = TWITTER_IMAGE_PATH + image_name
        image = default_storage.open(image_path)
        # saving same name will created a new file_1
        self.test_image_name = 'test_collected_images__' + image_name
        test_image_path = TWITTER_IMAGE_PATH + self.test_image_name
        self.test_image_path = default_storage.save(test_image_path, image)

    def save_image(self, image_name):
        # saving same name will created a new file_1
        self.test_image_name = 'test_collected_images__' + image_name
        test_image_path = TWITTER_IMAGE_PATH + self.test_image_name
        self.test_image_path = default_storage.save(test_image_path, image)

    def tearDown(self):
        # delete sample image
        default_storage.delete(self.test_image_path)
        
    def test_collected_images_contains_file_in_folder(self):
        images = collected_images() 
        self.assertIn(self.test_image_name, images)

class TestCollectedImagesReturnsSortedImages(TestCase):
    def setUp(self):
        # generate sample image
        image_name = 'test.jpg'
        image_path = TWITTER_IMAGE_PATH + image_name
        image = default_storage.open(image_path)
        # saving same name will created a new file_1
        self.test_image_name = 'test_collected_images__' + image_name
        test_image_path = TWITTER_IMAGE_PATH + self.test_image_name
        self.test_image_path1 = default_storage.save(test_image_path, image)
        sleep(1)
        self.test_image_path2 = default_storage.save(test_image_path, image)
        sleep(1)
        self.test_image_path3 = default_storage.save(test_image_path, image)

    def tearDown(self):
        # delete sample image
        default_storage.delete(self.test_image_path1)
        default_storage.delete(self.test_image_path2)
        default_storage.delete(self.test_image_path3)

    def test_collected_images_sorted_by_created_time(self):
        images = collected_images()
        for i in images:
            print '%s %s' % (i, default_storage.created_time(TWITTER_IMAGE_PATH + i))
        order_of_image2 = images.index('test_collected_images__test_2.jpg')
        order_of_image1 = images.index('test_collected_images__test_1.jpg')
        order_of_image0 = images.index('test_collected_images__test.jpg')
        self.assertLess(order_of_image2, order_of_image1)
        self.assertLess(order_of_image1, order_of_image0)
