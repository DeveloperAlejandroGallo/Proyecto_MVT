from django.contrib import admin
from django.urls import path
from AppCoder import views

urlpatterns = [
    path('mostrar_persona/',views.mostrar_personas)
]