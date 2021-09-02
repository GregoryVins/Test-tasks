from django.test import TestCase

from employees.models import Role, Employee


class EmployeeTestCase(TestCase):
    """
    Модель тестирования пользователей.
    """

    def setUp(self):
        self.owner_role = Role.objects.create(name='owner')
        self.admin_role = Role.objects.create(name='admin')
        self.employee_role = Role.objects.create(name='employee')

    def test_create_owner(self):
        """ Создание пользователя. """
        Employee.objects.create(username='test_username',
                                position=self.owner_role,
                                salary=1000)
        self.assertEqual(Employee.objects.all().first().username, 'test_username')
        self.assertEqual(Employee.objects.all().first().position, self.owner_role)

    def test_create_administrator(self):
        """ Создание администратора. """
        self.owner = Employee.objects.create(username='test_username_1',
                                             position=self.owner_role,
                                             salary=1000)
        self.admin = Employee.objects.create(username='test_username_2',
                                             position=self.admin_role,
                                             salary=500,
                                             supervisor=self.owner)
        self.assertEqual(self.admin.supervisor, self.owner)
        self.assertEqual(self.admin.position.name, 'admin')

    def test_create_role(self):
        """ Создание роли. """
        Role.objects.create(name='test role')
        self.assertEqual(Role.objects.all().count(), 4)
