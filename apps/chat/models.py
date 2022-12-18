from django.db import models

from apps.drivers.models import Drivers


class Message(models.Model):
    class Sender(models.TextChoices):
        DRIVER = 'D', 'Driver'
        OPERATOR = 'O', 'Operator'

    room = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    content = models.TextField()
    sender = models.CharField(max_length=20, choices=Sender.choices,
                              default=Sender.OPERATOR)

    def __str__(self):
        return self.content
