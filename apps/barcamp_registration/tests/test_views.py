# -*- coding: utf-8 -*-
from django.test import TestCase

class TestRegistration(TestCase):
    url = '/barcamp_registration/'
    def test_get_form(self):
        response = self.client.get(self.url)
        self.assertIn(u'name="name"',response.content)
        self.assertIn(u'name="email"',response.content)
        self.assertIn(u'name="twitter"',response.content)
        self.assertIn(u'name="website"',response.content)
        self.assertIn(u'name="tshirt_size"',response.content)

        self.assertEqual(response.content.count('required_mark'),2)

    def test_post_required_only_check_redirect(self):
        data = {
            'name':'Barcamper',
            'email': 'barcamper@gmail.com'
        }
        response = self.client.post(self.url,data=data)
        self.assertEqual(response.status_code,302)
        self.assertTrue(response['location'].endswith('/whos_coming/'))

    def test_post_required_only_check_result(self):
        data = {
            'name':'Barcamper',
            'email': 'barcamper@gmail.com'
        }
        response = self.client.post(self.url,data=data,follow=True)
        self.assertEqual(response.status_code,200)
        self.assertIn('<td class="name">Barcamper</td>',response.content)
        self.assertIn('<td class="email">barcamper@gmail.com</td>',response.content)