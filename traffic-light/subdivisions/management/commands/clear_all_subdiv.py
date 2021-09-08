from django.core.management import BaseCommand

from subdivisions.models import Subdivision


class Command(BaseCommand):
    help = 'Clear all subdivisions'

    def handle(self, *args, **options):
        Subdivision.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all subdivisions'))

