from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class FormularioRegistro(UserCreationForm):
    username = forms.CharField(max_length=30, label="Nombre", widget=forms.TextInput(
        attrs={'class': "form-control"}))
    email = forms.EmailField(max_length=200, label="Email", widget=forms.EmailInput(
        attrs={'class': "form-control"}))
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(
        attrs={'class': "form-control"}))
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(
        attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )


class FormularioInicioSesion(forms.Form):

    nombre = forms.CharField(label="Usuario", required=True, widget=forms.TextInput(
        attrs={'class': "form-control"}))

    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(
        attrs={'class': "form-control"}))
