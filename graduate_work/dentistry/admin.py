from django.contrib import admin
from .models import Schedule, Patient, Doctor, Title


# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'image')
    exclude = ['created_in', 'updated_in']
    empty_value_display = 'none'


admin.site.register(Schedule)
admin.site.register(Patient)
# admin.site.register(Doctor)
admin.site.register(Title)
