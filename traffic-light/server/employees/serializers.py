from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from employees.models import Employee

from employees.models import Role


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ['name', ]


class EmployeeSerializer(ModelSerializer):
    position = SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'username', 'position', 'supervisor', 'salary']

    def get_position(self, instance):
        return RoleSerializer(instance.position).data
