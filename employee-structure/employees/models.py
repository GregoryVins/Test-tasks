import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.Model):
    """
    Роль, должность сотрудника.
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, db_index=True)
    name = models.CharField(max_length=255, verbose_name='Роль')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Employee(AbstractUser):
    """
    Модель Сотрудника.
    """
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, db_index=True)
    middle_name = models.CharField(max_length=64, verbose_name='Отчество', blank=True, null=True)
    position = models.ForeignKey('employees.Role', on_delete=models.CASCADE, verbose_name='Должность')
    hiring_date = models.DateField(verbose_name='Дата приёма на работу', auto_now_add=True)
    salary = models.PositiveIntegerField(verbose_name='Размер заработной платы')
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Начальник',
                                   related_name='coworkers')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
