from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.drivers.models import Drivers
from . import models, forms


class ChatView(LoginRequiredMixin, TemplateView):
    template_name = 'chat/chat_base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chat_list'] = Drivers.objects.all()
        return context


def chat_room(request, pk):
    context = {}
    if request.method == 'POST':
        form = forms.MessageForm(request.POST)
        if form.is_valid():
            cd = form.clean()
            message = models.Message(room=Drivers.objects.get(id=pk),
                                     sender=models.Message.Sender.OPERATOR,
                                     content=cd['message'])
            message.save()
        return redirect(reverse_lazy('chat:chat-room', args=(pk,)))
    else:
        form = forms.MessageForm()
    context['form'] = form
    context['messages'] = models.Message.objects.filter(room=pk)
    context['chat_list'] = Drivers.objects.all()
    context['driver'] = Drivers.objects.get(id=pk)
    return render(request,
                  'chat/chat_room.html',
                  context)
