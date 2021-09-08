from django.core.management import BaseCommand

from employees.models import Employee
from subdivisions.models import Subdivision


class Command(BaseCommand):
    help = 'Clear all users and subdivisions. ! ! ! WARNING ! ! !'

    def handle(self, *args, **options):
        Employee.objects.all().exclude(is_superuser=True).delete()
        self.stdout.write(self.style.SUCCESS('Successfully'))
