from django import forms

from . import models


class DriversForm(forms.ModelForm):
    class Meta:
        model = models.Drivers
        fields = '__all__'
        widgets = {
            'surname': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'patronymic': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
