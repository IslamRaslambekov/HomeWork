from django.urls import path
from RSP import views

urlpatterns = [
    path('', views.main_page, name='index'),
    path('title/', views.title_page, name='title'),
]