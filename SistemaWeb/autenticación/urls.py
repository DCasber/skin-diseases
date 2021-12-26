from django.urls import path
from .views import inicioSesion, Registro, cierreSesion

from django.conf.urls import url

from django.contrib import admin
from django.views.defaults import page_not_found
from .views import admin_view
admin.site.admin_view = admin_view

urlpatterns = [
    path('', inicioSesion, name="inicioSesion"),
    path('registro/', Registro.as_view(), name="registro"),
    path('logout/', cierreSesion, name="cierreSesionUsuario"),
    path('admin/logout/', cierreSesion, name="cierreSesionAdmin"),

    url(r'^admin/login/', page_not_found),
    url(r'^admin/', admin.site.urls),
]
