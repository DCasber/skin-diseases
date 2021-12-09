from django.urls import path
from .views import inicioSesion, registro

urlpatterns = [
    path('', inicioSesion, name="inicioSesion"),
    path('registro', registro, name="registro")
]
