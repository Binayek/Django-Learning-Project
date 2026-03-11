from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('hello/', views.say_hello, name='say_hello'),
    path('contact/', views.contact_view, name='contact_view'),
    path('home/', views.home1, name='home1'),

    ]