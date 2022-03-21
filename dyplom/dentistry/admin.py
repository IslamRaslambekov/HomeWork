from django.contrib import admin
from .models import Schedule, Patient, Doctor, Title

# Register your models here.


# class ScheduleAdmin(admin.ModelAdmin):
#     list_display = ('id', 'doctor', '')

admin.site.register(Schedule)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Title)
