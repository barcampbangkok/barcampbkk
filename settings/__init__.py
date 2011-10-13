# App settings are made into a package for clean modularity of settings in
# different environments. Development settings are loaded by default, and
# production can configure overriding settings through an environment variable:
#
#   export DJANGO_SETTINGS_MODULE="barcampbkk.settings.production"
#
# The directory containing the app will need to be on the Python import path --
# see https://docs.djangoproject.com/en/dev/topics/settings/
#
# You can also use this for a settings/local.py file if you *really* need some
# special local-only settings. Just add that file to SCM ignores. You'll also
# need to be sure to use `django-admin.py runserver` instead of `manage.py` for
# the env variable to be respected, and augment the Python path as noted above.

from dev import *

