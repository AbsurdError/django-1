from django.shortcuts import render
from django.http import HttpResponse

def information(request, name, age, hobby):
    return HttpResponse(f'<h1>ФИО:</h1> <h2>{name}</h2>. <br><h1>Мне </h1><h2>{age} лет</h2>. <br><h1>Мои хобби:</h1> <h2>{hobby}</h2>')

def about(request, city, performance, love):
    return HttpResponse(f'<h2>Я приехал из {city}. <br>В школе я учился {performance}. <br>Мне {love} учиться</h2>')
def contacts(request, github, telegram):
    return HttpResponse(f'<h1>Мои контактные данные.</h1> <br><h2>Ссылка на GitHub:</h2> <br><h3>{github} <br><h2>Тег в Telegram:</h2> <br><h3>@{telegram}.</h3>')