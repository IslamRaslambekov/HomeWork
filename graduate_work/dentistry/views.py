from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
from dentistry.forms import ReceptionForm


def main_page(request):
    return render(request, 'dentistry/index.html', {'title': 'Главная'})


class ReceptionView(CreateView):
    form_class = ReceptionForm
    template_name = 'dentistry/reception.html'
    success_url = reverse_lazy('home')
