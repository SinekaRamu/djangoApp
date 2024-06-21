from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponse

# Create your views here.

def home(req):
    # return HttpResponse("Hello World!")
    return render(req, "home.html", {'name': 'sineka'})


def calc(req):
    return render(req, "result.html")

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def add (request):
    a = int(request.GET['num1'])
    b = int(request.GET['num2'])
    res = a + b
    return render(request, "result.html", {"result": res})