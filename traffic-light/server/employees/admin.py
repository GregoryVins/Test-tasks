from django.contrib import admin

from employees.models import Employee, Role


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    model = Employee
    list_display = ('id', 'username', 'position', 'supervisor')


admin.site.register(Role)
