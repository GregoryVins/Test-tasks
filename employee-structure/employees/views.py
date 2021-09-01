from django.views.generic import ListView

from employees.models import Employee


class EmployeeListView(ListView):
    """
    Отображение списка сотрудников.
    """
    template_name = 'employee.html'
    queryset = Employee.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        context['employees'] = Employee.objects.filter(supervisor=None)
        context['employees_count'] = Employee.objects.all().count()
        return context
