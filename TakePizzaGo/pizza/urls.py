from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
from . import views

urlpatterns = [

    path('menu', views.choose_pizza, name='home'),
    path('', views.about, name='about'),
    path('adauga_pizza/<int:pk>/', views.adauga_pizza, name='adauga'),
    path('elimina_pizza/<int:pk>/', views.elimina_pizza, name='elimina')
]