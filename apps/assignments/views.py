from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, \
    DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.counterparties import models as counterparties_models
from . import models
from . import forms


class AssignmentsListView(LoginRequiredMixin, ListView):
    model = models.Assignment
    template_name = 'assignments/assigment_list.html'


class AssignmentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'assignments/assigment_form.html'
    model = models.Assignment
    form_class = forms.AssigmentForm
    success_url = reverse_lazy('assignments:list')
    extra_context = {
        'customers': counterparties_models.Counterparty.objects.all()
    }


class AssignmentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'assignments/assigment_form.html'
    model = models.Assignment
    form_class = forms.AssigmentForm
    success_url = reverse_lazy('assignments:list')
    extra_context = {
        'STATUSES': models.Assignment.Status,
        'customers': counterparties_models.Counterparty.objects.all()
    }


class AssignmentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'assignments/assigment_delete.html'
    model = models.Assignment
    success_url = reverse_lazy('assignments:list')
