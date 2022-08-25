from django.shortcuts import render, HttpResponse
from django.template import loader
from familiares.models import Familiar

# Create your views here.
def arbol_familiar(request):
    familiar_1 = Familiar (nombre = 'Maria', apellido = 'Gomez', relacion_familiar = 'Hermana', fecha_nacimiento = '1989-06-03')
    familiar_1.save()

    familiar_2 = Familiar (nombre = 'Claudia', apellido = 'Higuita', relacion_familiar = 'Madre', fecha_nacimiento = '1969-06-03')
    familiar_2.save()

    plantilla = loader.get_template ('grupofamiliar.html')

    familia = {'familiares': [familiar_1,familiar_2]}

    documento = plantilla.render(familia)

    return HttpResponse(documento)