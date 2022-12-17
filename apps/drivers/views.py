from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, \
    DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models, forms


class DriversListView(LoginRequiredMixin, ListView):
    template_name = 'drivers/list.html'
    model = models.Drivers


class DriversCreateView(LoginRequiredMixin, CreateView):
    template_name = 'drivers/form.html'
    model = models.Drivers
    form_class = forms.DriversForm
    success_url = reverse_lazy('drivers:list')


class DriversUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'drivers/form.html'
    model = models.Drivers
    form_class = forms.DriversForm
    success_url = reverse_lazy('drivers:list')


class DriversDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'drivers/delete.html'
    model = models.Drivers
    success_url = reverse_lazy('drivers:list')
