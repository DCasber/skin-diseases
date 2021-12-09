from django import forms

class FormularioInicioSesion(forms.Form):
    
    nombre = forms.CharField(label = "Usuario", required=True, widget = forms.TextInput(attrs={'class':"form-control"}))
    
    password = forms.CharField(label = "Contraseña",widget=forms.PasswordInput(attrs={'class':"form-control"}))
