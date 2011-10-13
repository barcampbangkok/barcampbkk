""" Signal hack for loaddata Django CMS placeholders

django-cms has an issue with signals fired during loaddata leading to
relational integrity errors:

  https://github.com/divio/django-cms/issues/1031

This results in our fixtures for initial data failing to load into Postgres.
Until a resolution is made upstream, this works around the problem by
monkey-patching the loaddata command to disconnect the problem signal before
the normal load operation.
"""

from django.core.management.commands import loaddata
from django.db.models import signals

class Command(loaddata.Command):

    def handle(self, *fixture_labels, **options):
        from cms.signals import update_placeholders
        from cms.models import Page

        signals.post_save.disconnect(update_placeholders, sender=Page)
        loaddata.Command.handle(self, *fixture_labels, **options)
        signals.post_save.connect(update_placeholders, sender=Page)

