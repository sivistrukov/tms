from django import forms

from . import models


class CounterpartiesForm(forms.ModelForm):
    class Meta:
        model = models.Counterparty
        fields = '__all__'
        widgets = {
            'type': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
