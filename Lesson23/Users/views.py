from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(LoginView):
    form_class = AuthenticationForm
    template_name = 'Users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'Users/registration.html'
    success_url = reverse_lazy('login')

