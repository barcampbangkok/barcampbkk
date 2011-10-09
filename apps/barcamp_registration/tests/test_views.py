# -*- coding: utf-8 -*-
from django.test import TestCase

class TestRegistration(TestCase):
    def test_get_form(self):
        response = self.client.get('/barcamp_registration/')
        self.assertIn(u'name="name"',response.content)
        self.assertIn(u'name="email"',response.content)
        self.assertIn(u'name="twitter"',response.content)
        self.assertIn(u'name="website"',response.content)
        self.assertIn(u'name="tshirt_size"',response.content)

        self.assertEqual(response.content.count('required_mark'),2)