from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('userList', views.selectUser),
    path('register', views.register),
    path('login', views.login)
]
