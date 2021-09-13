from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from employees.serializers import EmployeeSerializer
from subdivisions.models import Subdivision


class SubdivisionSerializer(ModelSerializer):
    owners = SerializerMethodField()

    class Meta:
        model = Subdivision
        fields = "__all__"

    def get_owners(self, instance):
        for item in instance.get_object_list():
            yield EmployeeSerializer(item).data

