from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import Clase_Familia
import datetime
from django.http import HttpResponse
from django.template  import Context , Template , loader

# Create your views here.
def Clase_Familia(request):
    familiares= Clase_Familia(nombre="Damian",edad=28,fecha_nacimiento="1994-2-7")
    familiares.save()
    texto = f"Mi familiares son " [ Clase_Familia ]
    return HTTPResponse(texto) 

def diaDeHoy(request):
    dia = datetime.datetime.now()
    familia = Clase_Familia()
    documentodetexto= f"hoy es : <br> {dia} y mis familiares son {familia}"
    return HttpResponse(documentodetexto)
    
def probandoTemplate(self):
    diccionario = {Clase_Familia}
    plantilla=loader.get_template("template.html")   
    documento = plantilla.render(diccionario)
    return HttpResponse(documento, )