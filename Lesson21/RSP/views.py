from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Doctor, Title


def main_page(request):
    dr_all = Doctor.objects.all()
    return render(request, 'RSP/doctors.html', {'doctors': dr_all})


def title_page(request):
    titles = Title.objects.all()
    return render(request, 'RSP/get_all_titles.html', {'titles': titles})
