from curses.ascii import HT
from http.client import HTTPResponse
from django.shortcuts import render , HttpResponse
from django.template import loader #importamos el cargador
from familiares.models import Familiar

# Create your views here.
#definimos la vista usando funciones
def catalogo (request):
    familiar_1 = Familiar (nombre = "Damian Defederico" , edad = "28" , fecha = "15/02/1994")
    familiar_1.save()

    familiar_2 = Familiar (nombre = "Ezequiel Defederio" , edad = "30" , fecha = "15/02/1994")
    familiar_2.save()

    familiar_3 = Familiar (nombre = "Ailen Defederico" , edad = "21" , fecha = "15/02/1994")
    familiar_3.save()

    plantilla = loader.get_template("familiares.html")

    familiaresdiccionario = { "familiares": [familiar_1, familiar_2,familiar_3]}

    documento = plantilla.render(familiaresdiccionario)
    return HTTPResponse(documento)