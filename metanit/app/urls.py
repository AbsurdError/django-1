
from django.contrib import admin
from django.urls import path, re_path
from app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about', kwargs={'name': 'Ann', 'work': 'teacher'}),
    # re_path(r'^about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts')
]
