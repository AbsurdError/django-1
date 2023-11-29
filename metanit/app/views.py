from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    text = '<h1>Tretyakov </h1>' \
            '<p>my info</p>'
    return HttpResponse(text)

def about(request, name, work):
    return HttpResponse(f'About my site. <br> My name is {name}. <br> I work a {work}')

def contacts(request):
    return HttpResponse('My contacts')