from django.http import HttpResponse
import datetime
from datetime import datetime
from django.template import loader
from Aplicacion.models import Persona
from Aplicacion.views import guardar_DB


def mostrar_html(request):
    #Creo las 3 personas pedidas
    familiar_1=Persona(nombre='Juan',apellido='Perez',fecha_nacimiento=datetime(1989,12,25,17,35,43),dni=12345678,email='juan_perez@mail.com')
    familiar_2=Persona(nombre='Maria',apellido='Alcaraz',fecha_nacimiento=datetime(1992,5,21,19,4,15),dni=87654322,email='Maria_Alcaraz@mail.com')
    familiar_3=Persona(nombre='Pedro',apellido='Perez',fecha_nacimiento=datetime(2020,11,20,23,47,59),dni=56781234,email='')
    
    #Creo la lista para guardar en la base de datos
    lista_familiar=[familiar_1,familiar_2,familiar_3]
    guardar_DB(lista_familiar)

    #Creo el diccionario para enviar al template
    familiar={'Persona_1':familiar_1,'Persona_2':familiar_2,'Persona_3':familiar_3}
    template=loader.get_template('Mostrar_Nombres.html')
    return HttpResponse(template.render(familiar))
