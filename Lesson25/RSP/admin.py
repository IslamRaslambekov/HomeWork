from django.contrib import admin
from .models import *


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'name', 'middle_name', 'image')
    search_fields = ('last_name',)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'name', 'middle_name', 'number')
    search_fields = ('last_name',)


admin.site.register(Title, TitleAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Client, ClientAdmin)
