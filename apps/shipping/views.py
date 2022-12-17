from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, \
    UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal

from . import models, forms


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
    form_class = forms.UpdateShippingForm
    success_url = reverse_lazy('shipping:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payloads'] = self.object.assignment.payloads.filter(assignment=self.object.assignment)
        return context


class ShippingDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'shipping/delete.html'
    model = models.Shipping
    success_url = reverse_lazy('shipping:list')


def create_pdf_service_complete(request, pk):
    shipping = get_object_or_404(models.Shipping, pk=pk)
    context = {
        'shipping': shipping,
        'vat': '{:.2f}'.format(shipping.assignment.cost * Decimal(1.20))
    }

    return render(request,
                  'shipping/pdfs/service_complete.html',
                  context)


class ServiceCompleteView(DetailView):
    template_name = 'shipping/pdfs/service_complete.html'
    model = models.Shipping

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vat'] = '{:.2f}'.format(self.object.assignment.cost * Decimal(1.20))
        return context


class ContractView(DetailView):
    template_name = 'shipping/pdfs/contract.html'
    model = models.Shipping

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
