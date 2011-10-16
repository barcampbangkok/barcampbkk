from django.test import TestCase
from nj_feed_reader.fetch_twitter import find_url_in_tweet

class TestFindUrlInTweet(TestCase):
    def test_find_url_at_the_end_in_tweet(self):
        text = 'Parking http://t.co/bXl9Izpt'
        urls = find_url_in_tweet(text)
        self.assertEqual(['http://t.co/bXl9Izpt'], urls)

    def test_find_url_in_the_middle_of_tweet(self):
        text = 'Parking http://t.co/bXl9Izpt #njwedding'
        urls = find_url_in_tweet(text)
        self.assertEqual(['http://t.co/bXl9Izpt'], urls)

