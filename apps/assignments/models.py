from django.db import models
from apps.counterparties.models import Counterparty


class Assignment(models.Model):
    class Status(models.TextChoices):
        AWAITING_PAYMENT = 'Ожидает оплату', 'Ожидает оплату'
        PAID = 'Оплачен', 'Оплачен'
        CANCELED = 'Отменен', 'Отменен'

    loading_address = models.CharField(max_length=150)
    unloading_address = models.CharField(max_length=150)
    status = models.CharField(max_length=50, choices=Status.choices,
                              default=Status.AWAITING_PAYMENT)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    customers = models.ForeignKey(Counterparty, related_name='assignments',
                                  on_delete=models.CASCADE)
    representative = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Payload(models.Model):
    name = models.CharField(max_length=150)
    count = models.IntegerField()
    assignment = models.ForeignKey(Assignment, related_name='payloads',
                                   on_delete=models.CASCADE)
