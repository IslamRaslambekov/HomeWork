from django import forms
from django.contrib.auth.models import User

from .models import Title, Doctor, Patient, Schedule


class ReceptionForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['doctor', 'start_at', 'stop_at']
