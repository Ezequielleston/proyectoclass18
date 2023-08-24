from django.shortcuts import render
from .models import Autos
from django.http import HttpResponse
# Create your views here.

def crear_autos(request):
    
    marca_autos="HONDA"
    modelo_autos=999000
    print("Buscando tu vehiculo")
    autos=Autos(marca=marca_autos,modelo=modelo_autos)
    autos.save()
    respuesta=f"Tu vehiculo:{autos.marca} - {autos.modelo}"
    return HttpResponse(respuesta)


def listar_autos(request):
    autos=Autos.objects.all()
    respuesta=""
    for autos in Autos:
        respuesta+=f"{autos.marca} - {autos.modelo}<br>"
    return HttpResponse(respuesta)    


def inicio(request):
    return render(request,"AppCoder/inicio.html")

def camionetas(request):
    return render(request,"AppCoder/CAMIONETAS.html")

def motos(request):
    return render(request,"AppCoder/MOTOS.html")

def autos(request):
    autos=Autos.objects.all()
    return render(request,"AppCoder/AUTOS.html", {"autos":autos})