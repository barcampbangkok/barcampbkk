from django.test import TestCase
from json import loads

class TestViews(TestCase):
    fixtures = ['two_tweets_fixture.json']
    #fixtures = ['tweets_from_db.json']

    def test_get_new_tweets_ok(self):
        response = self.client.get('/api/new_tweets/')
        self.assertEqual(200, response.status_code)

