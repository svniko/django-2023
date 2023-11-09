from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Django. Lecture 1<h1>')

def hello(request, name):
    flag = True
    return render(request, 'lecture1/index.html',{
        "name":name.capitalize(),
        "flag":flag
    })