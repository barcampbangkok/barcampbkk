# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$','barcamp_registration.views.registration',name='barcamp_registration'),
)