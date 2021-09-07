from django.views.generic import ListView

from employees.models import Employee
from subdivisions.models import Subdivision


class EmployeeListView(ListView):
    """
    Отображение списка сотрудников.
    """
    template_name = 'employee.html'
    queryset = Employee.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        context['subdivisions'] = Subdivision.objects.all()
        # context['employees'] = Employee.objects.filter(supervisor=None, is_superuser=False)
        context['employees_count'] = Employee.objects.all().exclude(is_superuser=True).count()
        return context
