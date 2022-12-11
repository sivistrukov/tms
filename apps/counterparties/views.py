from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, \
    DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models
from . import forms


class CounterpartiesListView(LoginRequiredMixin, ListView):
    model = models.Counterparty
    template_name = 'counterparties/list.html'


class CounterpartiesCreateView(LoginRequiredMixin, CreateView):
    template_name = 'counterparties/form.html'
    model = models.Counterparty
    form_class = forms.CounterpartiesForm
    success_url = reverse_lazy('counterparties:list')


class CounterpartiesUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'counterparties/form.html'
    model = models.Counterparty
    form_class = forms.CounterpartiesForm
    success_url = reverse_lazy('counterparties:list')


class CounterpartiesDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'counterparties/delete.html'
    model = models.Counterparty
    success_url = reverse_lazy('counterparties:list')
