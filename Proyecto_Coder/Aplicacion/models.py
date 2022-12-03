from django.db import models

#genero la clase Persona que uso en el programa
class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    dni=models.IntegerField()
    email=models.EmailField(max_length=50)

