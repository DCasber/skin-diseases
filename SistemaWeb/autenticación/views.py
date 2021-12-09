from django.forms.forms import Form
from django.shortcuts import render
from .forms import FormularioInicioSesion

# Create your views here.


def inicioSesion(request):
    
    formulario = FormularioInicioSesion()
    
    error = False
    
    return render(request, "autenticación/inicioSesión.html", {"formulario": formulario, "error": error})


def registro(request):
    return