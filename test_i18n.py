# -*- coding: utf-8 -*-

from django.test import TestCase

class TestLanguageChooser(TestCase):
    fixtures = ['dev/cms.yaml','dev/cms-text.yaml','dev/snippets.yaml',]

    def test_language_chooser_is_shown(self):
        response = self.client.get('/')
        self.assertIn('<a href="/en/" class="current">English</a>',response.content)
        self.assertIn('<a href="/th/">Thai</a>',response.content)