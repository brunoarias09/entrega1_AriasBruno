from django.urls import path
from redondos_app.views import inicio,busquedaIntegrantes, busquedaCompactos,buscarCompacto, integrantesFormulario, buscarIntegrante, compactosFormulario, instrumentosFormulario, recitalesFormulario

urlpatterns = [
   
    path('', inicio, name="Inicio"), 
    #FORMULARIOS DE CARGA DE DATOS
    path('integrantesFormulario/', integrantesFormulario, name='integrantesFormulario'),
    path('instrumentosFormulario/', instrumentosFormulario, name="instrumentosFormulario"),
    path('compactosFormulario/', compactosFormulario, name="compactosFormulario"),
    path('recitalesFormulario/', recitalesFormulario, name="recitalesFormulario"),
    #FORMULARIOS DE BUSQUEDA
    path('busquedaIntegrantes/', busquedaIntegrantes, name="busquedaIntegrantes"),
    path('busquedaCompactos/', busquedaCompactos, name="busquedaCompactos"),
    

   #LOS BUSCADORES
   path('buscarIntegrante/', buscarIntegrante, name='buscarIntegrante'),
   path('buscarCompacto/', buscarCompacto, name='buscarCompacto'),

]