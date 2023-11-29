
from django.contrib import admin
from django.urls import path, re_path
from MyInfo import views


urlpatterns = [
    re_path(r'^$', views.information, name='home', kwargs={'name': 'Третьяков Андрей Анатольевич', 'age': '17', 'hobby': 'Шахматы, шашки, видео игры, фильмы и музыка'}),
    re_path(r'^about', views.about, name='about', kwargs={'city': 'Посёлка городского типа Суксун(с марийского "Талая вода")', 'performance': 'неплохо', 'love': 'нравиться'}),
    re_path(r'^contacts', views.contacts, name='contacts', kwargs={'github': 'https://github.com/AbsurdError', 'telegram': 'Anidab_cuba77'})
]
