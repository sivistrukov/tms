from django import forms

from . import models


class AssigmentForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = '__all__'
        exclude = ['updated', 'created']
        widgets = {
            'customers': forms.Select(attrs={
                'class': 'form-select'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'cost': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
        }


class PayloadForm(forms.ModelForm):
    class Meta:
        model = models.Payload
        fields = '__all__'
        exclude = ['assignment']
