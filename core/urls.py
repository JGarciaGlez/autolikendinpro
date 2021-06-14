from os import name
from re import template
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView

app_name='core'
urlpatterns = [
    path('',LoginView.as_view(template_name='layouts/login.html'), name='login'),
    path('home',views.home,name='home'),
    path('scrapear',views.scrapping,name='recolectar'),
    path('logout',LogoutView.as_view(template_name='layouts/logout.html'), name='logout'),
    path('buscarlikendin', views.busqueda, name="busqueda"),
    path('visitar',views.visitar,name="visitar"),
    path("register", views.register, name="register")
]
