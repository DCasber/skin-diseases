from django import forms

class FormularioInicioSesion(forms.Form):
    
    nombre = forms.CharField(label = "Usuario", required=True, widget = forms.TextInput(attrs={'class':"form-control"}))
    
    password = forms.CharField(label = "Contraseña",widget=forms.PasswordInput(attrs={'class':"form-control"}))

class FormularioRegistro(forms.Form):
    
    nombre = forms.CharField(label = "Nombre de usuario", required=True, widget = forms.TextInput(attrs={'class':"form-control"}))
    
    email = forms.EmailField(label = "Email", required=True, widget = forms.EmailInput(attrs={'class':"form-control"}))
    
    password = forms.CharField(label = "Contraseña",widget=forms.PasswordInput(attrs={'class':"form-control"}))
    
    passwordConfirmed = forms.CharField(label = "Confirmar contraseña",widget=forms.PasswordInput(attrs={'class':"form-control"}))