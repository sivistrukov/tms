from django.db import models

from apps.assignments.models import Assignment


class Drivers(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.surname.title() + ' ' + self.name[0].title() + '.' + self.patronymic[0].title() \
               + '.' if self.patronymic else self.surname.title() + ' ' + \
                                             self.name[0].title() + '.'


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
