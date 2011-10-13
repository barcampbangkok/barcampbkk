#!/usr/bin/env python
import sys

try:
    import pinax
except ImportError:
    sys.stderr.write("Error: Can't import Pinax. Make sure you are in a virtual environment that has\nPinax installed or create one with pinax-boot.py.\n")
    sys.exit(1)

from django.conf import settings
from django.core.management import setup_environ, execute_from_command_line

try:
    import settings as settings_mod # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: can't load settings -- there must be an ImportError with the settings module.\nHave you created settings/secrets.py?")
    sys.exit(1)

# setup the environment before we start accessing things in the settings.
setup_environ(settings_mod)

if __name__ == "__main__":
    execute_from_command_line()
