from random import choice
from string import ascii_letters

from django.core.management import BaseCommand
from django.db import transaction

from employees.models import Employee, Role
from .names import NAMES


class Command(BaseCommand):
    help = 'Create more 1000 users'

    def create_random_username(self):
        username = ''
        for _ in range(5):
            username += choice(ascii_letters)
        return username

    def create_owner(self):
        owner_role = Role.objects.create(name='owner')

        for _ in range(10):
            Employee.objects.create(username=self.create_random_username(),
                                    first_name=choice(NAMES),
                                    position=owner_role,
                                    salary=600)

    def create_administrators(self):
        admin_role = Role.objects.create(name='administrator')
        owners = Employee.objects.all()

        for _ in range(100):
            Employee.objects.create(username=self.create_random_username(),
                                    first_name=choice(NAMES),
                                    position=admin_role,
                                    salary=300,
                                    supervisor=choice(owners))

    def create_employees(self):
        admin_role = Role.objects.get(name='administrator')
        employee_role = Role.objects.create(name='employee')
        administrators = Employee.objects.filter(position=admin_role)

        for _ in range(900):
            Employee.objects.create(username=self.create_random_username(),
                                    first_name=choice(NAMES),
                                    position=employee_role,
                                    salary=150,
                                    supervisor=choice(administrators))

    def handle(self, *args, **options):
        with transaction.atomic():
            self.create_owner()
            self.create_administrators()
            self.create_employees()
            self.stdout.write(self.style.SUCCESS('Successfully'))
