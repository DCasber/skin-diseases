from django.shortcuts import render

# Create your views here.


def inicioSesion(request):
    
    return render(request, "autenticación/inicioSesión.html")