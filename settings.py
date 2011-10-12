# -*- coding: utf-8 -*-
# Django settings for basic pinax project.

import os.path
import posixpath
import pinax

PINAX_ROOT = os.path.abspath(os.path.dirname(pinax.__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = PROJECT_ROOT

# tells Pinax to use the default theme
PINAX_THEME = "barcamp_basic"
GOYZ_THEME = "goyz_theme"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
    # ("Your Name", "your_email@domain.com"),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "dev.db",                       # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Bangkok'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en"

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/site_media/static/"

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "site_media", "media", PINAX_THEME),
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Make this unique, and don't share it with anybody.
SECRET_KEY = "c$z-3#l4jzku!+*pwby3zf!=n9#q54lv)gg@076)0xnmm8)q(9"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",

    #cms
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
#    'cms.middleware.toolbar.ToolbarMiddleware',
#    'cms.middleware.media.PlaceholderMediaMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',


    "pinax.apps.account.middleware.LocaleMiddleware",
    #"debug_toolbar.middleware.DebugToolbarMiddleware",

    'csrf_tools.middleware.CsrfDisabledMiddleware',
]

ROOT_URLCONF = "urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(PINAX_ROOT, "templates", PINAX_THEME),
    os.path.join(PROJECT_ROOT, "templates", PINAX_THEME),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.static',
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",

    "staticfiles.context_processors.static_url",

    "pinax.core.context_processors.pinax_settings",

    "pinax.apps.account.context_processors.account",

    "notification.context_processors.notification",
    "announcements.context_processors.site_wide_announcements",

    #cms
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
]

INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.humanize",
    "django.contrib.staticfiles",

    "pinax.templatetags",

    # external
    "notification", # must be first
    "debug_toolbar",
    "mailer",
    "uni_form",
    "ajax_validation",
    "timezones",
    "emailconfirmation",
    "announcements",
    "pagination",
#    "idios",

    #for pinax.apps.profiles
    "avatar",
    "microblogging",
    "friends",

    # Pinax
    "pinax.apps.account",
    "pinax.apps.signup_codes",
    "pinax.apps.analytics",
    "pinax.apps.profiles",

    # Django Cms
    'cms',
    'menus',
    'mptt',
    'appmedia',
    'south',
    'sekizai',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',

    #nose
    "django_nose",

    # project
    "about",
#    "profiles",
    'socialregistration',
    'barcamp_registration',
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/profile/%s/" % o.username,
}

AUTH_PROFILE_MODULE = "profiles.Profile"
NOTIFICATION_LANGUAGE_MODULE = "account.Account"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False

AUTHENTICATION_BACKENDS = [
    'socialregistration.auth.TwitterAuth',
    'auth.backends.AccountAuthenticationBackend',
]

LOGIN_URL = "/account/login/" # @@@ any way this can be a url name?
LOGIN_REDIRECT_URLNAME = "what_next"
LOGIN_REDIRECT_URL = '/'

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'proteus.tech.com@gmail.com'
EMAIL_HOST_PASSWORD = 'wrong#h1n1'
EMAIL_USE_TLS = True

# URCHIN_ID = "ua-..."

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

CMS_TEMPLATES= (
    ('cms/cms_base.html', "Base" ),
    ('goyz_theme/cms/cms_base.html', "Goyz Base"),
)
CMS_MODERATOR=False
CMS_PERMISSION = False
CMS_TEMPLATE_INHERITANCE = True
CMS_PLACEHOLDER_CONF = {}
CMS_LANGUAGES =(
    ('en', 'English',),
    ('th', 'Thai',),
)
LANGUAGES= CMS_LANGUAGES

#logger
import logging
from django_logger import LoggerClass

logging.getLogger('django.db.backends').setLevel(logging.ERROR)
logging.getLogger('PYREADLINE').setLevel(logging.ERROR)
logging.getLogger('south').setLevel(logging.ERROR)

logging.setLoggerClass(LoggerClass(
    file_suffix = '.log',
    default_level = logging.INFO,
    files_path = os.path.abspath(os.path.join(PROJECT_DIR, 'logs')),
))

### Socialauth #####
TWITTER_CONSUMER_KEY = '838bFpYe8sk4eHLCGCqkYQ'
TWITTER_CONSUMER_SECRET_KEY = 'AwfRsy3AuSzpxyoXeXvtIumjQDQ0damIlzmNs1Iiak'
TWITTER_ACCESS_TOKEN = '12223502-r2LFtPSMNGYpiF2GeGNVb4JPcmyvpMa79fKh2PH03'
TWITTER_ACCESS_TOKEN_SECRET = '72A5pjsELAqrIYf7ockXa8lJmCEEh1UhLVgicOTN16E'
TWITTER_REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
TWITTER_ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
TWITTER_AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
####################

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass
