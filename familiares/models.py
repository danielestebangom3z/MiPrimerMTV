from turtle import textinput
from django.db import models

# Create your models here.
class Familiar (models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.TextField(max_length=30)
    relacion_familiar = models.TextField(max_length=30)
    fecha_nacimiento = models.DateField(textinput)


