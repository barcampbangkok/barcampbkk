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

    def test_post_required_not_found(self):
        data = {
            'name':'Barcamper',
        }
        response = self.client.post(self.url,data=data)
        self.assertEqual(response.status_code,400)
        self.assertIn(u'This field is required.',response.content)

    def test_post_email_is_not_the_right_format(self):
        data = {
            'name':'Barcamper',
            'email': 'barcamper'
        }
        response = self.client.post(self.url,data=data)
        self.assertEqual(response.status_code,400)
        self.assertIn(u'Enter a valid e-mail address.',response.content)

    def test_post_website_url_is_not_the_right_format(self):
        data = {
            'name':'Barcamper',
            'email': 'barcamper@gmail.com',
            'website': 'barcamper'
        }
        response = self.client.post(self.url,data=data)
        self.assertEqual(response.status_code,400)
        self.assertIn(u'Enter a valid URL.',response.content)

    def test_post_duplicate_name_and_email(self):
        self.test_post_required_only_check_result()
        data = {
            'name':'Barcamper',
            'email': 'barcamper@gmail.com'
        }
        response = self.client.post(self.url,data=data)
        self.assertEqual(response.status_code,400)
        self.assertIn(u'Barcamp registration with this Name and E-mail already exists.',response.content)

