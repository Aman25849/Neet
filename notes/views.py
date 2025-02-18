from django.shortcuts import render
from .models import Messages
from .forms import msgForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

def notes(request, user):
    if request.method == "POST":
        data = msgForm(request.POST)
        if data.is_valid():
            Messages.objects.create(user=user, messages=f"{data.cleaned_data['message']}")
            return HttpResponseRedirect(reverse('notes', args=[user]))
    
    else:
        data = msgForm()
    msgs = Messages.objects.all()
    return render(request, 'notes/notes.html',{"msgs": msgs, 'data':data})