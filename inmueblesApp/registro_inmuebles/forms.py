from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ContactFormForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(max_length=64, label='Nombre')
    message = forms.CharField(label='Mensaje')

class RegistroForm(UserCreationForm):
    nombres = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    rut = forms.CharField(max_length=12)
    direccion = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=15)
    correo_electronico = forms.EmailField()
    username = forms.CharField(max_length=150)

    class Meta:
        model = Usuario
        fields = ('nombres', 'apellidos', 'rut', 'direccion', 'telefono', 'correo_electronico', 'tipo_usuario')