
from django.shortcuts import render, redirect
from .forms import FormularioInicioSesion, FormularioRegistro
from django.views import View

from functools import update_wrapper
from django.http import Http404
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.http import HttpResponse

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

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

    if request.method == "GET":

        if request.user and request.user.is_authenticated:

            if request.user.is_superuser:
                return redirect("/admin/")
            else:
                return redirect("/home/")

        else:
            error = False

            formulario = FormularioInicioSesion()

            return render(request, "autenticación/inicioSesión.html", {"formulario": formulario, "error": error, "msg": " "})

    elif request.method == "POST":
        usuario = authenticate(request, username=request.POST.get(
            "nombre"), password=request.POST.get("password"))

        if usuario is not None:

            login(request, usuario)

            if usuario.is_superuser:
                return redirect("/admin/")
            else:
                return redirect("/home/")

        else:

            error = True

            msg = "No se ha encontrado un usuario con los datos introducidos"

            formulario = FormularioInicioSesion()

            return render(request, "autenticación/inicioSesión.html", {"formulario": formulario, "error": error, "msg": msg})


class Registro(View):

    def get(self, request):

        if request.user and request.user.is_authenticated:

            if request.user.is_superuser:
                return redirect("/admin/")
            else:
                return redirect("/home/")

        else:

            formulario = FormularioRegistro()

            return render(request, "autenticación/registro.html", {"formulario": formulario, 'error': False})

    def post(self, request):

        form = FormularioRegistro(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Confirmación de cuenta'
            message = render_to_string('autenticación/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request, 'autenticación/mensajeActivación.html', {'titulo': "Confirmar email", 'mensaje': "Por favor, confirme el registro a través de la cuenta de correo electrónico introducida.", "activacionConfirmada": False})

        else:
            print(form.instance.username)
            return render(request, 'autenticación/registro.html', {'formulario': form, 'error': True})


def cierreSesion(request):

    logout(request)

    return redirect("/")


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request, 'autenticación/mensajeActivación.html', {'titulo': "Activación válida", 'mensaje': "Gracias por confirmar su registro. Ahora podrá iniciar sesión.", "activacionConfirmada": True})
    else:
        return render(request, 'autenticación/mensajeActivación.html', {'titulo': "Activación inválida", 'mensaje': "El link de activación es inválido.", "activacionConfirmada": False})
