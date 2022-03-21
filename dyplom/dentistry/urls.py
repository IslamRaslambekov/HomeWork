from django.urls import path

from dentistry import views

urlpatterns = [
    path('', views.main_page),
]