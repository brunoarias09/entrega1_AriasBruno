from django.db import models

class Integrantes(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    
    
class Instrumentos(models.Model):
    tipo=models.CharField(max_length=30)
    musico=models.CharField(max_length=30)
    valor=models.IntegerField()

class Compactos(models.Model):
    nombre=models.CharField(max_length=30)
    año=models.IntegerField()

class Recitales(models.Model):
    lugar=models.CharField(max_length=30)
    cantidadPublico=models.IntegerField()
