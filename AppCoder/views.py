from django.shortcuts import render
from .models import Autos, Camionetas
from django.http import HttpResponse
from .forms import Autosform, Camionetasform
# Create your views here.

def crear_autos(request):
    
    marca_autos="HONDA"
    modelo_autos="civic"
    print("Buscando tu vehiculo")
    autos=Autos(marca=marca_autos,modelo=modelo_autos)
    autos.save()
    respuesta=f"Tu vehiculo: {autos.marca} - {autos.modelo}"
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
    if request.method=="POST":
        form=Camionetasform(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            marca=info["marca"]
            modelo=info["modelo"]
            camionetas=Camionetas(marca=marca,modelo=modelo)
            camionetas.save()
            return render(request,"AppCoder/CAMIONETAS.html", {"mensaje":"Camioneta creada"})
        else:
            return render(request,"AppCoder/CAMIONETAS.html", {"mensaje": "Datos invalidos"})
    else:    
        
        formulario_camionetas=Camionetasform()

    return render(request,"AppCoder/CAMIONETAS.html", {"formulario":formulario_camionetas})        

def motos(request):
    return render(request,"AppCoder/MOTOS.html")

def autos(request):
    if  request.method=="POST":
        form=Autosform(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            marca=info["marca"]
            modelo=info["modelo"]
            autos=Autos(marca=marca,modelo=modelo)
            autos.save()
            return render(request,"AppCoder/AUTOS.html", {"mensaje": "Auto creado"})
        return render(request,"AppCoder/AUTOS.html", {"mensaje": "Datos invalidos"})
    else:
        formulario_autos=Autosform()
        return render(request,"AppCoder/AUTOS.html", {"formulario": formulario_autos})