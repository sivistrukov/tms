from django.shortcuts import redirect, render, get_object_or_404
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


class AssignmentCreateAndRedirectView(LoginRequiredMixin, CreateView):
    template_name = 'assignments/assigment_form.html'
    model = models.Assignment
    form_class = forms.AssigmentForm

    def get_success_url(self):
        return reverse_lazy('assignments:add-payload', args=(self.object.id,))


class AssignmentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'assignments/assigment_form.html'
    model = models.Assignment
    form_class = forms.AssigmentForm
    success_url = reverse_lazy('assignments:list')
    extra_context = {
        'STATUSES': models.Assignment.Status,
        'customers': counterparties_models.Counterparty.objects.all(),
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payloads'] = self.object.payloads.filter(assignment=self.object)
        return context


class AssignmentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'assignments/assigment_delete.html'
    model = models.Assignment
    success_url = reverse_lazy('assignments:list')


def create_payload(request, assignment_id):
    context = {}
    if request.method == 'POST':
        form = forms.PayloadForm(request.POST)
        if form.is_valid():
            payload = form.save(commit=False)
            payload.assignment_id = assignment_id
            payload.save()
            return redirect(reverse_lazy('assignments:update-assignment', args=(assignment_id,)))
    else:
        form = forms.PayloadForm()
    context['assignment_id'] = assignment_id
    context['form'] = form
    return render(request, 'assignments/payload_form.html', context)


def update_payload(request, assignment_id, payload_id):
    context = {'assignment_id': assignment_id}
    obj = get_object_or_404(models.Payload, id=payload_id)
    context['payload'] = obj
    form = forms.PayloadForm(request.POST or None, instance=obj)
    context['form'] = form
    if form.is_valid():
        form.save()
        return redirect(reverse_lazy('assignments:update-assignment', args=(assignment_id,)))
    return render(request, 'assignments/payload_form.html', context)


class PayloadCreateView(LoginRequiredMixin, CreateView):
    template_name = 'assignments/payload_form.html'
    model = models.Payload
    form_class = forms.PayloadForm

    def get_success_url(self):
        return reverse_lazy('assignments:update-assignment', args=(self.object.assignment.id,))


class PayloadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'assignments/payload_delete.html'
    model = models.Payload

    def get_success_url(self):
        return reverse_lazy('assignments:update-assignment', args=(self.object.assignment.id,))
