from django.urls import path
from . import views

urlpatterns = [
    path ("", views.home, name="home"),
    path ("calc/", views.calc, name="calc"),
    path ("todo/", views.todos, name="todos"),
    path ("calc/add", views.add, name="result")
] 