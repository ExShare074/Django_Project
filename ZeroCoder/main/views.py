from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('<h1>Это мой первый проект на django</h1>')

def new(request):
    return HttpResponse('<h1>Это вторая страница проекта на django</h1>')

def index_view(request):
    return render(request, 'main/index.html')