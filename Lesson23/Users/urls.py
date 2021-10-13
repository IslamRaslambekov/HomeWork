from django.urls import path
from Users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('registration/', views.RegisterUser.as_view(), name='registration'),
]