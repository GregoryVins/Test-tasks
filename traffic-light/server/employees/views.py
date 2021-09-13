from rest_framework.viewsets import ModelViewSet

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        user_id = self.request.GET.get('userId', None)
        if user_id:
            return Employee.objects.filter(supervisor_id=user_id)
        return Employee.objects.all().exclude(is_superuser=True)
