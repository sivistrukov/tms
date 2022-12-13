from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, \
    UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms


class ShippingsListView(LoginRequiredMixin, ListView):
    template_name = 'shipping/list.html'
    model = models.Shipping


class ShippingCreateView(LoginRequiredMixin, CreateView):
    template_name = 'shipping/form.html'
    model = models.Shipping
    form_class = forms.ShippingForm
    success_url = reverse_lazy('shipping:list')


class ShippingUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'shipping/form.html'
    model = models.Shipping
    form_class = forms.ShippingForm
    success_url = reverse_lazy('shipping:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payloads'] = self.object.assignment.payload_set.filter(assignment=self.object.assignment)
        return context


class ShippingDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'shipping/delete.html'
    model = models.Shipping
    success_url = reverse_lazy('shipping:list')
