# -*- coding: utf-8 -*-

from django import forms

from barcamp_registration.models import BarcampRegistration

class BarcampRegistrationForm(forms.ModelForm):
    class Meta:
        model = BarcampRegistration