from django import forms

from . import models


class AssigmentForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = '__all__'
        exclude = ['updated', 'created']


class PayloadForm(forms.ModelForm):
    class Meta:
        model = models.Payload
        fields = '__all__'
        exclude = ['assignment']
