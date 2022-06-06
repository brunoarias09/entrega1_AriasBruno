from django.urls import path
from redondos_app.views import inicio, integrantes, instrumentos, compactos, recitales, integrantesFormulario

urlpatterns = [
   
    path('', inicio, name="Inicio"), 
    path('integrantes', integrantes, name="integrantes"),
    path('instrumentos', instrumentos, name="instrumentos"),
    path('compactos', compactos, name="compactos"),
    path('recitales', recitales, name="recitales"),

    path('integrantesFormulario', integrantesFormulario, name='integrantesFormulario'),
   
]