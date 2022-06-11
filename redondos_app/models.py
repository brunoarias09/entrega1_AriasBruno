from django.db import models

class Integrantes(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return self.nombre + " " + self.apellido
    
class Instrumentos(models.Model):
    tipo=models.CharField(max_length=30)
    musico=models.CharField(max_length=30)
    valor=models.IntegerField()

    def __str__(self) -> str:
        return self.tipo + " " + self.musico

class Compactos(models.Model):
    nombre=models.CharField(max_length=30)
    año=models.IntegerField()

    def __str__(self) -> str:
        return self.nombre + " " + str(self.año)

class Recitales(models.Model):
    lugar=models.CharField(max_length=30)
    cantidadPublico=models.IntegerField()

    def __str__(self) -> str:
        return self.lugar + " " + str(self.cantidadPublico)
