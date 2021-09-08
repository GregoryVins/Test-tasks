import uuid

from django.db import models


class Subdivision(models.Model):
    """
    Модель Подразделения.
    """
    id = models.UUIDField(default=uuid.uuid4, db_index=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255, verbose_name='Название подразделения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def get_object_list(self):
        return self.users.filter(supervisor=None)
