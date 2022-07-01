
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    fecha=forms.DateField()
    lugar=forms.CharField(max_length=30)
    anecdota=forms.CharField(max_length=400)


class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)
    password1=forms.CharField(label="contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="confirmar contraseña",widget=forms.PasswordInput)

class Meta:
    model= User
    fields=['username','email','password1','password2']
    help_texts = {k:"" for k in fields }


class UserEditForm(UserCreationForm):
    email=forms.EmailField(required=True)
    password1=forms.CharField(label="contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="confirmar contraseña",widget=forms.PasswordInput)

class Meta:
    model= User
    fields=['username','email','password1','password2']
    help_texts = {k:"" for k in fields }
