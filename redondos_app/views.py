from django.shortcuts import render, HttpResponse

from django.http import HttpResponse
from django.template import loader
from redondos_app.models import Integrantes, Instrumentos, Compactos, Recitales
from redondos_app.forms import IntegrantesFormulario, InstrumentosFormulario, CompactosFormulario, RecitalesFormularios


def inicio(request):
    return render(request,'redondos_app/inicio.html')

def integrantes(request):
    return render(request,'redondos_app/busquedaIntegrantes.html')

def instrumentos(request):
    return render(request,'redondos_app/instrumentos.html')

def compactos(request):
    return render(request,'redondos_app/compactos.html')

def recitales(request):
    return render(request,'redondos_app/recitales.html')

#tengo q crear las clases formulario

def integrantesFormulario(request):
    if request.method == 'POST':
        miFormulario=IntegrantesFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre=informacion['nombre']
        apellido=informacion['apellido']
        integrantes=Integrantes(nombre=nombre, apellido=apellido)
        integrantes.save()

        return render(request, 'redondos_app/inicio.html')

    else:
        miFormulario=IntegrantesFormulario()

    return render(request,'redondos_app/integrantesFormulario.html', {'miFormulario':miFormulario})


def busquedaIntegrantes(request):
        return render(request, 'redondos_app/busquedaIntegrantes.html')


def buscar(request):
    #respuesta= {request.GET['camada']} para probar q andaba
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        apellido=Integrantes.objects.get(nombre=nombre)
    
        return render(request, 'redondos_app/resultadosBusqueda.html',{'nombre':nombre,'apellido':apellido.apellido})
    else:
        respuesta='no se ingreso nombre correcto'    
    return HttpResponse(respuesta)
