# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from emailconfirmation.models import EmailAddress

@receiver(post_save,sender=User)
def update_email_address(sender, instance, created, **kwargs):
    if instance.email:
        try:
            EmailAddress.objects.get(user=instance,email=instance.email)
            # already have one (which is unlikely, but anyway
        except EmailAddress.DoesNotExist:
            emailaddress = EmailAddress.objects.add_email(user=instance,email=instance.email)
            if EmailAddress.objects.filter(user=instance).count() == 1:
                emailaddress.set_as_primary()