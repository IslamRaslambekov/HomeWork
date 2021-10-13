from django.urls import path
from RSP import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('doctors/', views.Doctors.as_view(), name='doctors'),
    path('add_doctors/', views.AddDoctors.as_view(), name='add_doctors'),
]