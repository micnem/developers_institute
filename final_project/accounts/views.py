from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegisterForm

# Create your views here.



class SignUpView(generic.CreateView):
    form_class = RegisterForm
    success_url = '/'
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


def profile(request):
    user = request.user

    return render(request, 'profile.html', {'user':user})