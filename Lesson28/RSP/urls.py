from django.urls import path
from RSP import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('doctors/', views.Doctors.as_view(), name='doctors'),
    path('add_doctors/', views.AddDoctors.as_view(), name='add_doctors'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
]