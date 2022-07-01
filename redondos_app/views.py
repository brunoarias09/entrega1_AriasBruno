from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import loader
from redondos_app.models import Integrantes, Instrumentos, Compactos, Recitales
from redondos_app.forms import IntegrantesFormulario,UserRegistrationForm, InstrumentosFormulario, CompactosFormulario, RecitalesFormularios
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate, logout 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


def inicio(request):
    plantilla = loader.get_template('redondos_app/inicio.html')   #es importante que la pagina de inicio, tenga un loader.
    documento = plantilla.render()  
    return HttpResponse(documento)

#ACA VAN LOS FORMULARIOS DE CARGA DE DATOS
@login_required
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

class InstrumentosFormulario(ListView):
    model = Instrumentos
    template_name = 'redondos_app/instrumentosFormulario.html'
# def instrumentosFormulario(request):
#     if request.method == 'POST':
#         miFormulario=InstrumentosFormulario(request.POST)

#         if miFormulario.is_valid():
#             informacion=miFormulario.cleaned_data
#         tipo=informacion['tipo']
#         musico=informacion['musico']
#         valor=informacion['valor']
#         instrumento=Instrumentos(tipo=tipo, musico=musico, valor=valor)
#         instrumento.save()

#         return render(request, 'redondos_app/inicio.html')

#     else:
#         miFormulario=InstrumentosFormulario()

#     return render(request,'redondos_app/instrumentosFormulario.html', {'miFormulario':miFormulario})
@login_required
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


#----------------------FORMULARIOS DE BUSQUEDA()------------------------------

@login_required
def busquedaIntegrantes(request):
        return render(request, 'redondos_app/busquedaIntegrantes.html')

@login_required
# def buscarIntegrante(request):
#     if request.GET['nombre']:
#         busqueda=request.GET.get('nombre')
#         resultado=Integrantes.objects.filter(Q(nombre=busqueda) | Q(apellido=busqueda))#sino ponemos .get
#         return render(request, 'redondos_app/resultadosIntegrantes.html',{'nombre':resultado})#sino agregamos apellido.apellido
#     else:
#         respuesta='no se ingreso nombre correcto'    
#     return HttpResponse(respuesta)
def buscarIntegrante(request):
     if request.GET['nombre']:
         nombre=request.GET['nombre']
         apellido=Integrantes.objects.get(nombre=nombre)#sino ponemos .get
         return render(request, 'redondos_app/resultadosIntegrantes.html',{'nombre':nombre,'apellido':apellido.apellido})#sino agregamos apellido.apellido
     else:
         respuesta= render(request, 'redondos_app/inicio.html',{'mensaje':'ingrese el nombre correcto'})

     return HttpResponse(respuesta)

def busquedaCompactos(request):
        return render(request, 'redondos_app/busquedaCompactos.html')
@login_required
def buscarCompacto(request):
    if request.GET['nombre']:
        nombre=request.GET['nombre']
        año=Compactos.objects.get(nombre=nombre)#sino ponemos .get o filter
        return render(request, 'redondos_app/resultadosCompactos.html',{'nombre':nombre,'año':año})#sino agregamos o sacamos apellido.año
    else:
        respuesta=render(request, 'redondos_app/inicio.html',{'mensaje':'ingrese el nombre correcto'})
  
    return HttpResponse(respuesta)

#--------------------CRUD DE RECITALES----------------------------------------

class ListaRecitales(LoginRequiredMixin,ListView):
    model = Recitales
    template_name = 'redondos_app/recitales_list.html'
class DetalleRecitales(DetailView):
    model = Recitales
    template_name = 'redondos_app/recitales_detalle.html'
class CrearRecitales(CreateView):#hay q ver si anda asi, o probar como las diapositivas
    model = Recitales
    success_url = reverse_lazy('listaRecitales')
    fields = ['nombre','apellido', 'fecha', 'lugar', 'anecdota']
    
class EditarRecitales(UpdateView):
    model = Recitales
    success_url = reverse_lazy('listaRecitales')
    fields = ['nombre','apellido', 'fecha', 'lugar', 'anecdota']
    
class EliminarRecitales(DeleteView):
    model = Recitales 
    success_url = reverse_lazy('listaRecitales')

#-----------------SOBRE MI-----------------------
def SobreMi(request):
    return render(request, 'redondos_app/sobreMi.html')

    #..............LOGUIN LOGOUT----------------------------------------------------

def login_request(request):
    if request.method =='POST':
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            user=authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request,'redondos_app/inicio.html',{'mensaje':'Bienvenido'})
            else:
                return render(request,'redondos_app/inicio.html',{'mensaje':'Usuario o contraseña incorrectos'})


        else:
            return render(request, 'redondos_app/inicio.html',{'mensaje':'error, formulario erroneo'})
    else:
        form=AuthenticationForm()
        return render(request, 'redondos_app/login.html',{'form':form})


#----------------registro de usuario---------------

def register_request(request):
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request,'redondos_app/inicio.html', {'mensaje':'Usuario {username} creado'})
        else:
            return render(request,'redondos_app/inicio.html', {'mensaje':'error, no se pudo crear el usuario'})
    else:
        form=UserRegistrationForm()
        return render(request, 'redondos_app/register.html', {'form':form})


#----------------EDICION DE USUARIOS---------------------
@login_required
def editarUsuario(request):
    usuario=request.user
    if request.method == 'POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data

            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()
            
            return render(request,'redondos_app/inicio.html')
    else:
        form=UserRegistrationForm(initial={'email':usuario.email})
        
    return render(request, 'redondos_app/editarUsuario.html', {'form':form, 'usuario':usuario})

        



