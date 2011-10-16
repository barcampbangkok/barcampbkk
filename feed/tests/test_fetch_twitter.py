from django.test import TestCase
from feed.fetch_twitter import fetch_tweets

class TestFetchTwitter(TestCase):
    def test_can_fetch_from_twitter(self):
        response, content = fetch_tweets()
        self.assertEqual(200, response.status)

