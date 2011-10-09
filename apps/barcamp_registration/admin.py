# -*- coding: utf-8 -*-
from django.contrib import admin

from barcamp_registration.models import BarcampRegistration

class BarcampRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name','email','twitter')
    search_fields = ('name','email','twitter')
    list_filter = ('tshirt_size',)

admin.site.register(BarcampRegistration,BarcampRegistrationAdmin)
