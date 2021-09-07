from datetime import datetime
from random import choice
from string import ascii_letters

from django.core.management import BaseCommand
from django.db import transaction

from employees.models import Employee, Role
from subdivisions.models import Subdivision
from .names import NAMES

USERNAME_LENGTH = 5

SUBDIVISION_COUNT = 25  # Подразделения

OWNER_COUNT = 3
ADMINISTRATOR_COUNT = 30
STAFF_COUNT = 250
MANAGER_COUNT = 470
EMPLOYEE_COUNT = 900


# OWNER_COUNT = 100
# ADMINISTRATOR_COUNT = 1000
# STAFF_COUNT = 7500
# MANAGER_COUNT = 12500
# EMPLOYEE_COUNT = 35000


class Command(BaseCommand):
    help = 'Create more 50000 users'

    def create_random_username(self, num: int):
        username = ''
        for _ in range(num):
            username += choice(ascii_letters)
        return username

    def create_subdivisions(self, num: int):
        """
        Создание Подразделений.
        :param number: Создаваемое количество Подразделений.
        :return:
        """
        for i in range(num):
            Subdivision.objects.create(name=f'Subdivision_{i}')

    def get_or_create_owner(self, num: int):
        print(f'\n\nHello\n\n')
        owner_role = Role.objects.create(name='owner')
        print(f'{owner_role=}')
        subdivisions = Subdivision.objects.all()

        for _ in range(num):
            Employee.objects.create(username=self.create_random_username(USERNAME_LENGTH),
                                    first_name=choice(NAMES),
                                    position=owner_role,
                                    salary=1000,
                                    subdivision=choice(subdivisions))

    def get_or_create_administrators(self, num: int):
        admin_role, created = Role.objects.get_or_create(name='admin')
        for _ in range(num):
            owner = choice(Employee.objects.all())
            Employee.objects.create(username=self.create_random_username(USERNAME_LENGTH),
                                    first_name=choice(NAMES),
                                    position=admin_role,
                                    salary=500,
                                    supervisor=owner,
                                    subdivision=owner.subdivision)

    def get_or_create_staff(self, num: int, usr_len: int):
        admin_role, created = Role.objects.get_or_create(name='admin')
        staff_role, created = Role.objects.get_or_create(name='staff')

        for _ in range(num):
            administrator = choice(Employee.objects.filter(position=admin_role))
            Employee.objects.create(username=self.create_random_username(usr_len),
                                    first_name=choice(NAMES),
                                    position=staff_role,
                                    salary=250,
                                    supervisor=administrator,
                                    subdivision=administrator.subdivision)

    def get_or_create_manager(self, num: int, usr_len: int):
        staff_role, created = Role.objects.get_or_create(name='staff')
        manager_role, created = Role.objects.get_or_create(name='manager')

        for _ in range(num):
            administrator = choice(Employee.objects.filter(position=staff_role))
            Employee.objects.create(username=self.create_random_username(usr_len),
                                    first_name=choice(NAMES),
                                    position=manager_role,
                                    salary=125,
                                    supervisor=administrator,
                                    subdivision=administrator.subdivision)

    def get_or_create_employee(self, num: int, usr_len: int):
        manager_role, created = Role.objects.get_or_create(name='manager')
        employee_role, created = Role.objects.get_or_create(name='employee')

        for _ in range(num):
            administrator = choice(Employee.objects.filter(position=manager_role))
            Employee.objects.create(username=self.create_random_username(usr_len),
                                    first_name=choice(NAMES),
                                    position=employee_role,
                                    salary=62,
                                    supervisor=administrator,
                                    subdivision=administrator.subdivision)

    def handle(self, *args, **options):
        with transaction.atomic():
            start = datetime.now()
            self.create_subdivisions(SUBDIVISION_COUNT)
            print(datetime.now() - start)
            start = datetime.now()
            self.get_or_create_owner(OWNER_COUNT)
            print(datetime.now() - start)
            start = datetime.now()
            self.get_or_create_administrators(ADMINISTRATOR_COUNT)
            print(datetime.now() - start)
            start = datetime.now()
            self.get_or_create_staff(STAFF_COUNT, USERNAME_LENGTH)
            print(datetime.now() - start)
            start = datetime.now()
            self.get_or_create_manager(MANAGER_COUNT, USERNAME_LENGTH)
            print(datetime.now() - start)
            start = datetime.now()
            self.get_or_create_employee(MANAGER_COUNT, USERNAME_LENGTH)
            print(datetime.now() - start)
            start = datetime.now()
            self.stdout.write(self.style.SUCCESS('Successfully'))
            print(datetime.now() - start)
