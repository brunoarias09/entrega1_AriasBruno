from re import template
from django import views
from django.urls import path
from redondos_app.views import login_request,ListaRecitales, DetalleRecitales, CrearRecitales, EditarRecitales, EliminarRecitales, register_request
from redondos_app.views import inicio,busquedaIntegrantes, SobreMi,busquedaCompactos,buscarCompacto, integrantesFormulario, buscarIntegrante, compactosFormulario, instrumentosFormulario
from django.contrib.auth.views import LogoutView

urlpatterns = [
   
    path('', inicio, name="Inicio"), 
    #FORMULARIOS DE CARGA DE DATOS
    path('integrantesFormulario/', integrantesFormulario, name='integrantesFormulario'),
    path('instrumentosFormulario/', instrumentosFormulario, name="instrumentosFormulario"),
    path('compactosFormulario/', compactosFormulario, name="compactosFormulario"),
    #path('recitalesFormulario/', recitalesFormulario, name="recitalesFormulario"),
    #FORMULARIOS DE BUSQUEDA
    path('busquedaIntegrantes/', busquedaIntegrantes, name="busquedaIntegrantes"),
    path('busquedaCompactos/', busquedaCompactos, name="busquedaCompactos"),
    

   #LOS BUSCADORES
   path('buscarIntegrante/', buscarIntegrante, name='buscarIntegrante'),
   path('buscarCompacto/', buscarCompacto, name='buscarCompacto'),
  
   #CRUD RECITALES BLOG
   path('listaRecitales/', ListaRecitales.as_view(), name='listaRecitales'),
   path('detalleRecitales/<pk>/', DetalleRecitales.as_view(), name='detalleRecitales'),#recitales/detail/<int:pk>/
   path('crearRecitales/', CrearRecitales.as_view(), name='crearRecitales'),
   path('editarRecitales/<pk>/', EditarRecitales.as_view(), name='editarRecitales'),
   path('eliminarRecitales/<pk>/', EliminarRecitales.as_view(), name='eliminarRecitales'),

   #login
   path('login', login_request, name='login'),
   path('register', register_request, name='registro'),
   path('sobreMi/', SobreMi, name='sobreMi'),
   path('logout/', LogoutView.as_view(template_name='redondos_app/logout.html'), name='logout'),



]
