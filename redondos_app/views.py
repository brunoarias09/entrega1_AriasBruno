from django.shortcuts import render, HttpResponse

from django.http import HttpResponse
from django.template import loader
from redondos_app.models import Integrantes, Instrumentos, Compactos, Recitales
from redondos_app.forms import IntegrantesFormulario, InstrumentosFormulario, CompactosFormulario, RecitalesFormularios


def inicio(request):
    plantilla = loader.get_template('redondos_app/inicio.html')   #es importante que la pagina de inicio, tenga un loader.
    documento = plantilla.render()  
    return HttpResponse(documento)

#ACA VAN LOS FORMULARIOS DE CARGA DE DATOS

def integrantesFormulario(request):
    if request.method == 'POST':
        miFormulario=IntegrantesFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre=informacion['nombre']
        apellido=informacion['apellido']
        integrante=Integrantes(nombre=nombre, apellido=apellido)
        integrante.save()

        return render(request, 'redondos_app/inicio.html')

    else:
        miFormulario=IntegrantesFormulario()

    return render(request,'redondos_app/integrantesFormulario.html', {'miFormulario':miFormulario})

def instrumentosFormulario(request):
    if request.method == 'POST':
        miFormulario=InstrumentosFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        tipo=informacion['tipo']
        musico=informacion['musico']
        valor=informacion['valor']
        instrumento=Instrumentos(tipo=tipo, musico=musico, valor=valor)
        instrumento.save()

        return render(request, 'redondos_app/inicio.html')

    else:
        miFormulario=InstrumentosFormulario()

    return render(request,'redondos_app/instrumentosFormulario.html', {'miFormulario':miFormulario})

def compactosFormulario(request):
    if request.method == 'POST':
        miFormulario=CompactosFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        nombre=informacion['nombre']
        año=informacion['año']
        compacto=Compactos(nombre=nombre, año=año)
        compacto.save()

        return render(request, 'redondos_app/inicio.html')

    else:
        miFormulario=CompactosFormulario()

    return render(request,'redondos_app/compactosFormulario.html', {'miFormulario':miFormulario})

def recitalesFormulario(request):
    if request.method == 'POST':
        miFormulario=RecitalesFormularios(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
        lugar=informacion['lugar']
        cantidadPublico=informacion['cantidadPublico']
        recital=Recitales(lugar=lugar, cantidadPublico=cantidadPublico)
        recital.save()

        return render(request, 'redondos_app/inicio.html')

    else:
        miFormulario=RecitalesFormularios()

    return render(request,'redondos_app/recitalesFormulario.html', {'miFormulario':miFormulario})

#----------------------FORMULARIOS DE BUSQUEDA------------------------------
def busquedaIntegrantes(request):
        return render(request, 'redondos_app/busquedaIntegrantes.html')


def buscarIntegrante(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        apellido=Integrantes.objects.get(nombre=nombre)#sino ponemos .get
        return render(request, 'redondos_app/resultadosIntegrantes.html',{'nombre':nombre,'apellido':apellido.apellido})#sino agregamos apellido.apellido
    else:
        respuesta='no se ingreso nombre correcto'    
    return HttpResponse(respuesta)

def busquedaCompactos(request):
        return render(request, 'redondos_app/busquedaCompactos.html')

def buscarCompacto(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        año=Compactos.objects.get(nombre=nombre)#sino ponemos .get o filter
        return render(request, 'redondos_app/resultadosCompactos.html',{'nombre':nombre,'año':año})#sino agregamos o sacamos apellido.año
    else:
        respuesta='no se ingreso nombre correcto'    
    return HttpResponse(respuesta)
