from django.urls import path
from RSP import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('doctors/', views.doctors, name='doctors'),
]