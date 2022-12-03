from django.shortcuts import render
from .models import Persona


#Solo guardo en la base de datos la lista de personas 
def guardar_DB(lista):
    for elemento in lista:
        #elemento.save() Comentado para no guardar muchas veces lo mismo
        pass
