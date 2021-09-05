from django.shortcuts import render, get_object_or_404
from .models import Doctor, Title


def main_page(request):
    return render(request, 'RSP/index.html')


def doctors(request):
    return render(request, 'RSP/doctors.html', {'doctors': Doctor.objects.all()})


def pageNotFound(request, exception):
    return render(request, 'RSP/error404.html')
