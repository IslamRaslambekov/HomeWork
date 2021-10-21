from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import *
from .forms import *


def main_page(request):
    return render(request, 'RSP/index.html')


class Doctors(ListView):  # ClassBasedView
    model = Doctor
    template_name = 'RSP/doctors.html'
    context_object_name = 'doctors'


class AddDoctors(LoginRequiredMixin, CreateView):  # ClassBasedView
    form_class = AddDoctorsForm
    template_name = 'RSP/add_doctors.html'
    success_url = reverse_lazy('doctors')


def pageNotFound(request, exception):
    return render(request, 'RSP/error404.html')


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'RSP/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'RSP/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
