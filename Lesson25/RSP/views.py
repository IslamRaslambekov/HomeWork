from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
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
