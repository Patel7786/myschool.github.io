from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    
    path('', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('faculty/', views.faculty, name='faculty'),
    path('college/', views.college, name='college'),
    path('admission/', views.admission, name='admission'),
    path('home/', views.home, name='home'),
   
]