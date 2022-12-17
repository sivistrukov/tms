from django.db import models

from apps.assignments.models import Assignment
from apps.drivers.models import Drivers


class Shipping(models.Model):
    class Status(models.TextChoices):
        COMPLETE = 'Завершён', 'Завершён'
        ACTIVE = 'Активный', 'Активный'
        CANCELED = 'Отменен', 'Отменен'
        SUSPENDED = 'Приостановлен', 'Приостановлен'

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    driver = models.ForeignKey(Drivers, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=100, choices=Status.choices,
                              default=Status.ACTIVE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
