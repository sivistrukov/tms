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

    def __int__(self, *args, **kwargs):
        super(ShippingForm, self).__init__(*args, **kwargs)
        shippings = models.Shipping.objects.all()
        assignments = Assignment.objects.filter(status=Assignment.Status.PAID)
        assignments = assignments.exclude(assignment__in=shippings)
        self.fields['assignment'] = forms.ModelChoiceField(queryset=assignments)
