from django.http import HttpResponse
from django.shortcuts import render
from .models import Persona
from django.db import *



def mostrar_personas(response):
    personas = Persona.objects.all()
    return render(response,'personas.html',{'personas':personas})

# def inicio(response):
#     return render(response,'index.html') #Acepta diccionarios

# def funcion_con_parametros(response):
#     return render(response, 'prueba.html',{'nombre': 'Coco', 'lista':[1,2,3,4]})