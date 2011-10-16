from django.core.management.base import BaseCommand, CommandError
from feed.fetch_twitter import fetch_twitter
class Command(BaseCommand):
    def handle(self, *args, **options):
        fetch_twitter()
        self.stdout.write('Successfully fetched tweets\n')
  