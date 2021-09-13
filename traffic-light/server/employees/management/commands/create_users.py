from datetime import datetime
from random import choice
from string import ascii_letters

from django.core.management import BaseCommand
from django.db import transaction

from employees.models import Employee, Role
from subdivisions.models import Subdivision
from utils.names import NAMES

USERNAME_LENGTH = 15

SUBDIVISION_COUNT = 25  # Подразделения

OWNER_COUNT = 100
ADMINISTRATOR_COUNT = 1000
STAFF_COUNT = 7500
MANAGER_COUNT = 12500
EMPLOYEE_COUNT = 35000


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
        owner_role, created = Role.objects.get_or_create(name='owner')
        subdivisions = Subdivision.objects.all()

        for _ in range(num):
            Employee.objects.get_or_create(username=self.create_random_username(USERNAME_LENGTH),
                                           first_name=choice(NAMES),
                                           position=owner_role,
                                           salary=1000,
                                           subdivision=choice(subdivisions))

    def get_or_create_administrators(self, num: int):
        admin_role, created = Role.objects.get_or_create(name='admin')
        owner_list = Employee.objects.all()
        admin_list = []

        for _ in range(num):
            owner = choice(owner_list)
            admin_list.append(Employee(username=self.create_random_username(USERNAME_LENGTH),
                                       first_name=choice(NAMES),
                                       position=admin_role,
                                       salary=500,
                                       supervisor=owner,
                                       subdivision=owner.subdivision))

        for item in admin_list:
            item.save()

    def get_or_create_staff(self, num: int, usr_len: int):
        admin_role, created = Role.objects.get_or_create(name='admin')
        staff_role, created = Role.objects.get_or_create(name='staff')
        administrator_list = Employee.objects.filter(position=admin_role)
        staff_list = []

        for _ in range(num):
            administrator = choice(administrator_list)
            staff_list.append(Employee(username=self.create_random_username(usr_len),
                                       first_name=choice(NAMES),
                                       position=staff_role,
                                       salary=250,
                                       supervisor=administrator,
                                       subdivision=administrator.subdivision))
        for item in staff_list:
            item.save()

    def get_or_create_manager(self, num: int, usr_len: int):
        staff_role, created = Role.objects.get_or_create(name='staff')
        manager_role, created = Role.objects.get_or_create(name='manager')
        stall_list = Employee.objects.filter(position=staff_role)
        manager_list = []

        for _ in range(num):
            administrator = choice(stall_list)
            manager_list.append(Employee(username=self.create_random_username(usr_len),
                                         first_name=choice(NAMES),
                                         position=manager_role,
                                         salary=125,
                                         supervisor=administrator,
                                         subdivision=administrator.subdivision))

        for item in manager_list:
            item.save()

    def get_or_create_employee(self, num: int, usr_len: int):
        manager_role, created = Role.objects.get_or_create(name='manager')
        employee_role, created = Role.objects.get_or_create(name='employee')
        manager_list = Employee.objects.filter(position=manager_role)
        employee_list = []

        for _ in range(num):
            administrator = choice(manager_list)
            employee_list.append(Employee(username=self.create_random_username(usr_len),
                                          first_name=choice(NAMES),
                                          position=employee_role,
                                          salary=62,
                                          supervisor=administrator,
                                          subdivision=administrator.subdivision))

        for item in employee_list:
            item.save()

    def handle(self, *args, **options):
        with transaction.atomic():
            start = datetime.now()
            self.create_subdivisions(SUBDIVISION_COUNT)
            print('self.create_subdivisions', datetime.now() - start)
            start = datetime.now()
            self.get_or_create_owner(OWNER_COUNT)
            print('self.get_or_create_owner', datetime.now() - start)
            start = datetime.now()
            self.get_or_create_administrators(ADMINISTRATOR_COUNT)
            print('self.get_or_create_administrators', datetime.now() - start)
            start = datetime.now()
            self.get_or_create_staff(STAFF_COUNT, USERNAME_LENGTH)
            print('self.get_or_create_staff', datetime.now() - start)
            start = datetime.now()
            self.get_or_create_manager(MANAGER_COUNT, USERNAME_LENGTH)
            print('self.get_or_create_manager', datetime.now() - start)
            start = datetime.now()
            self.get_or_create_employee(EMPLOYEE_COUNT, USERNAME_LENGTH)
            print('self.get_or_create_employee', datetime.now() - start)
            self.stdout.write(self.style.SUCCESS('Successfully'))
