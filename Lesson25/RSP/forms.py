from django import forms
from django.contrib.auth.models import User

from .models import *


class AddDoctorsForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ['name', 'middle_name', 'last_name', 'title', 'image']



