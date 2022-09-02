from django.shortcuts import render ,HttpResponse
from AppCoder.models import Familiar 
from django.template  import  loader
import datetime




# Create your views here.
def familiares(request):

    familiares = Familiar.objects.all()
    return render(request, "familiares.html", {'familiares':familiares},  )

def inicio(request):
    return render(request, "inicio.html",   )

