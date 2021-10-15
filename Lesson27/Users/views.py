from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class Login(LoginView):
    template_name = 'Users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')
