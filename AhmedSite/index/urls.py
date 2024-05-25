from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

app_name="index"

urlpatterns = [
    path('', views.home, name="Home"),
    path('resume/', views.resume, name="Resume"),
    path('about/', views.aboutme, name="About")
]
