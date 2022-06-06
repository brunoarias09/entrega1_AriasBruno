from django import forms


class IntegrantesFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)

class InstrumentosFormulario(forms.Form):
    tipo=forms.CharField(max_length=30)
    musico=forms.CharField(max_length=30)
    valor=forms.IntegerField()

class CompactosFormulario(forms.Form):
    nombre=forms.CharField(max_length=30)
    año=forms.IntegerField()

class RecitalesFormularios(forms.Form):
    lugar=forms.CharField(max_length=30)
    cantidadPublico=forms.IntegerField()
