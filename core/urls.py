from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.employees, name="index"),
    path('create', views.employees_create, name="create_employee"),
]
