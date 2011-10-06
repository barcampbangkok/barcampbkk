# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.models import User
from pinax.apps.account.auth_backends import AuthenticationBackend

class AccountAuthenticationBackend(AuthenticationBackend):

    def authenticate(self, **credentials):
        lookup_params = {}
        if settings.ACCOUNT_EMAIL_AUTHENTICATION:
            lookup_params["email"] = credentials.get("email")
        else:
            lookup_params["username"] = credentials.get("username")
        try:
            user = User.objects.get(**lookup_params)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(credentials["password"]):
                return user
