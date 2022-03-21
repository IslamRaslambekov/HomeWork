from django.urls import path

from dentist import views

urlpatterns = [
    path('', views.main_page),
]