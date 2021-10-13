from django import forms
from django.contrib.auth.forms import UserCreationForm

from .views import *


class RegistrationUSerForm(UserCreationForm):
    class Meta:
        model = RegisterUser
        fields = '__all__'
