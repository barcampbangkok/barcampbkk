# Load defaults to override only what is needed
from defaults import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
EMAIL_DEBUG = DEBUG

ADMINS = [
    'Web Ops Team', 'ops@hackerspace.in.th'
]
MANAGERS = ADMINS

# Directory where collectstatic will aggregate assets on deployment to be
# served by a web server
STATIC_ROOT = '/var/www/barcampbangkok.org/static'

#logger
logging.setLoggerClass(LoggerClass(
    file_suffix = '.log',
    stream_enabled = True,
    default_level = logging.INFO,
    files_path = path.abspath(path.join(PROJECT_ROOT, 'logs')),
))

