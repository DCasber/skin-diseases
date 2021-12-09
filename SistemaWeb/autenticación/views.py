from django.forms.forms import Form
from django.shortcuts import render, redirect
from .forms import FormularioInicioSesion, FormularioRegistro

# Create your views here.


def inicioSesion(request):
    
    formulario = FormularioInicioSesion()
    
    error = False
    
    return render(request, "autenticación/inicioSesión.html", {"formulario": formulario, "error": error})


def registro(request):
    
    if request.method == "GET":
        formulario = FormularioRegistro()
    
        error = False
    
        return render(request, "autenticación/registro.html", {"formulario": formulario, "error": error})
        
    elif request.method == "POST":
        return redirect("")
        
    

def autenticacion(request):
    return