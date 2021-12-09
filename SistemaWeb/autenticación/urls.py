from django.urls import path
import views

urlpatterns = [
    path('', views.inicioSesion, name="inicioSesion"),
]
