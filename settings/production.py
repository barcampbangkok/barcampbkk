# Load defaults to override only what is needed
from defaults import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
EMAIL_DEBUG = DEBUG

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

ADMINS = [
    'Web Ops Team', 'ops@hackerspace.in.th'
]
MANAGERS = ADMINS

# TODO: Postgres config
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": "production.db",                # Or path to database file if using sqlite3.
        "USER": "",                             # Not used with sqlite3.
        "PASSWORD": "",                         # Not used with sqlite3.
        "HOST": "",                             # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "",                             # Set to empty string for default. Not used with sqlite3.
    }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ['BARCAMPBKK_SECRET_KEY']

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ['BARCAMPBKK_EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['BARCAMPBKK_EMAIL_HOST_PASSWORD']
EMAIL_USE_TLS = True

#logger
logging.setLoggerClass(LoggerClass(
    file_suffix = '.log',
    stream_enabled = True,
    default_level = logging.INFO,
    files_path = path.abspath(path.join(PROJECT_ROOT, 'logs')),
))

