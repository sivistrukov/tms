from django.db import models


class Counterparty(models.Model):
    class Type(models.TextChoices):
        LIMITED_LIABILITY_COMPANY = 'ООО', 'Общество с ограниченной отвественностью'
        INDIVIDUAL_ENTREPRENEUR = 'ИП', 'Индивидуальный предприниматель'
        PUBLIC_CORPORATION = 'ОАО', 'Открытое акционерное общество'
        CLOSED_CORPORATION = 'ЗАО', 'Закрытое акционерное общество'

    organization_name = models.CharField(max_length=100)
    representative = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    type = models.CharField(max_length=40, choices=Type.choices)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.organization_name
