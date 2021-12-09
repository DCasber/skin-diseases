from django.urls import path
from .views import inicioSesion, registro, autenticacion

urlpatterns = [
    path('', inicioSesion, name="inicioSesion"),
    path('registro/', registro, name="registro"),
    path('auth/', autenticacion, name="autenticación"),
]
