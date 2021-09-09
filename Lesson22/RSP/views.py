from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import *
from .forms import *


def main_page(request):
    return render(request, 'RSP/index.html')


# def doctors(request):
#     return render(request, 'RSP/doctors.html', {'doctors': Doctor.objects.all()})
class Doctors(ListView):   # ClassBasedView
    model = Doctor
    template_name = 'RSP/doctors.html'
    context_object_name = 'doctors'


# def add_doctors(request):
#     if request.method == 'POST':
#         form = AddDoctorsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('doctors')
#     else:
#         form = AddDoctorsForm()
#     return render(request, 'RSP/doctors_create.html', {'form': form})
class AddDoctors(CreateView):   # ClassBasedView
    form_class = AddDoctorsForm
    template_name = 'RSP/doctors_create.html'
    success_url = reverse_lazy('doctors')


def pageNotFound(request, exception):
    return render(request, 'RSP/error404.html')
