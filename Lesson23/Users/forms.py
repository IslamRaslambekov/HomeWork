from django import forms
from django.contrib.auth.forms import UserCreationForm

from .views import Login


class RegistrationUSerForm(UserCreationForm):
    class Meta:
        model = Login
        fields = '__all__'
