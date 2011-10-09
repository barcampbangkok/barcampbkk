# -*- coding: utf-8 -*-
from django.test import TestCase

from barcamp_registration.models import BarcampRegistration

class TestBarcampRegistration(TestCase):
    def test_unicode(self):
        registration = BarcampRegistration.objects.create(name='Lady Gaga',email='ladygaga@gmail.com')
        self.assertEqual(unicode(registration),u'Barcamp Registration for: Lady Gaga (ladygaga@gmail.com)')