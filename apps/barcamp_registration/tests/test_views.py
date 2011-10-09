# -*- coding: utf-8 -*-
from django.test import TestCase

from barcamp_registration.models import BarcampRegistration

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

class TestWhosComing(TestCase):
    url = '/barcamp_registration/whos_coming/'
    def test_get_whos_coming(self):
        BarcampRegistration.objects.create(
            name='Barcamper 1',
            email='barcamper1@gmail.com',
            twitter='barcamper1',
            website='www.abcd.com',
            topics='Agile',
        )
        BarcampRegistration.objects.create(
            name='Barcamper 2',
            email='barcamper2@gmail.com',
            twitter='barcamper2',
            website='www.asdf.com',
            topics='DCI',
        )
        response = self.client.get(self.url)

        # barcamper 1
        self.assertIn('<td class="name">Barcamper 1</td>',response.content)
        self.assertIn('<td class="email">barcamper1@gmail.com</td>',response.content)
        self.assertIn('<a href="http://twitter.com/barcamper1" target="_blank">@barcamper1</a>',response.content)
        self.assertIn('<a href="www.abcd.com" target="_blank">www.abcd.com</a>',response.content)
        self.assertIn('<td class="topics">Agile</td>',response.content)

        # barcamper 2
        self.assertIn('<td class="name">Barcamper 2</td>',response.content)
        self.assertIn('<td class="email">barcamper2@gmail.com</td>',response.content)
        self.assertIn('<a href="http://twitter.com/barcamper2" target="_blank">@barcamper2</a>',response.content)
        self.assertIn('<a href="www.asdf.com" target="_blank">www.asdf.com</a>',response.content)
        self.assertIn('<td class="topics">DCI</td>',response.content)

        # 2 must come before 1 (check ordering)
        self.assertGreater(response.content.find('Barcamper 1'),response.content.find('Barcamper 2'))
