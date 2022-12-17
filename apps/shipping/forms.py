from django import forms

from apps.assignments.models import Assignment
from . import models


class ShippingForm(forms.ModelForm):
    class Meta:
        model = models.Shipping
        fields = '__all__'
        exclude = ['updated', 'created']
        widgets = {
            'driver': forms.Select(attrs={
                'class': 'form-select'
            }),
            'assignment': forms.Select(attrs={
                'class': 'form-select'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(ShippingForm, self).__init__(*args, **kwargs)
        assignments = Assignment.objects.filter(status=Assignment.Status.PAID)
        assignment_ids = models.Shipping.objects.all().values_list('assignment_id', flat=True)
        assignments = assignments.exclude(id__in=assignment_ids)
        self.fields['assignment'] = forms.ModelChoiceField(queryset=assignments)


class UpdateShippingForm(forms.ModelForm):
    class Meta:
        model = models.Shipping
        fields = '__all__'
        exclude = ['assignment', 'updated', 'created']
        widgets = {
            'driver': forms.Select(attrs={
                'class': 'form-select'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }
