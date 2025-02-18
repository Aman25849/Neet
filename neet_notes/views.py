from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import logForm
from django.urls import reverse

def home(request):
    if request.method == "POST":
        password = "Maanvi4007"
        auth_login = logForm(request.POST)
        if auth_login.is_valid() and auth_login.cleaned_data['password'] == password:
            user = (auth_login.cleaned_data['name'])
            return HttpResponseRedirect(reverse('notes', args=[user]))
    else:
        auth_login = logForm()
        
    return render(request, "index.html", {'login': auth_login})



