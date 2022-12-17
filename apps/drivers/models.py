from django.db import models


class Drivers(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.surname.title() + ' ' + self.name[0].title() + '.' + self.patronymic[0].title() \
               + '.' if self.patronymic else self.surname.title() + ' ' + \
                                             self.name[0].title() + '.'
