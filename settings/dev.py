# Load defaults to override only what is needed
from defaults import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
EMAIL_DEBUG = DEBUG

ADMINS = [
    # Don't be emailin' me in dev, yo
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

# Secure this for production!
SECRET_KEY = "c$z-3#l4jzku!+*pwby3zf!=n9#q54lv)gg@076)0xnmm8)q(9"

# we just need this here so django won't complete, only needed for "collectstatic"
STATIC_ROOT = path.join(PROJECT_ROOT, "static")

