from django.forms.forms import Form
from django.shortcuts import render, redirect
from .forms import FormularioInicioSesion, FormularioRegistro
from django.views import View

from functools import update_wrapper
from django.http import Http404
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth import authenticate, login, logout

# Create your views here.


def admin_view(view, cacheable=False):
    """
    Overwrite the default admin view to return 404 for not logged in users.
    """
    def inner(request, *args, **kwargs):
        if not request.user.is_active and not request.user.is_staff or request.user.is_active and not request.user.is_staff:
            raise Http404()
        return view(request, *args, **kwargs)

    if not cacheable:
        inner = never_cache(inner)

    # We add csrf_protect here so this function can be used as a utility
    # function for any view, without having to repeat 'csrf_protect'.
    if not getattr(view, 'csrf_exempt', False):
        inner = csrf_protect(inner)

    return update_wrapper(inner, view)


def inicioSesion(request):

    if request.user and request.user.is_authenticated:

        if request.user.is_superuser:
            return redirect("/admin/")
        else:
            return redirect("/home/")

    else:
        error = False
        if request.GET.get('error'):
            error = True

        formulario = FormularioInicioSesion()

        return render(request, "autenticación/inicioSesión.html", {"formulario": formulario, "error": error})


class Registro(View):

    def get(self, request):

        if request.user and request.user.is_authenticated:

            if request.user.is_superuser:
                return redirect("/admin/")
            else:
                return redirect("/home/")

        else:

            formulario = FormularioRegistro()

            return render(request, "autenticación/registro.html", {"formulario": formulario})
        
    def post(self, request):
        ## TODO: Comprobaciones del formulario de registro (ejs: inyección sql, existe ya el usuario (nombre), contraseñas iguales)
    
        ## TODO: Inserción de nuevo usuario. Contraseña con salting. Mensaje de confirmación al email. Mensaje al usuario de si el registro a salido bien o no. De salir bien mensaje de que debe confirmar su cuenta a través de su email. Hasta que no lo haga no podrá logearse, (o bien se introduce primero con un campo boolean a falso o debemos pasar los datos de alguna manera) (como hacerlo automatico?)
    
        return render(request, "autenticación/inicioSesión.html")


def autenticacion(request):

    usuario = authenticate(request, username=request.POST.get(
        "nombre"), password=request.POST.get("password"))

    if usuario is not None:

        login(request, usuario)

        if usuario.is_superuser:
            return redirect("/admin/")
        else:
            return redirect("/home/")

    else:

        return redirect("/?error=1")


def cierreSesion(request):

    logout(request)

    return redirect("/")
