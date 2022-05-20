from django.shortcuts import render

from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.contrib.auth.models import User

from django.core.mail import EmailMessage

import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

# Create your views here.


def contacto(request):

    formularioContacto = FormularioContacto()

    if request.method == "POST":
        formularioContacto = FormularioContacto(data=request.POST)

        if formularioContacto.is_valid():
            asunto = request.POST.get("asunto")
            contenido = request.POST.get("contenido")

            user = User.objects.get(id=request.user.id)

            email = EmailMessage(asunto, "Pregunta del usuario '" + str(request.user) + "':\n\n {}".format(
                contenido), to=[env('EMAIL_CONTACTO')], reply_to=[user.email])

            try:
                email.send()

                return redirect("/contacto/?validez")

            except:
                return redirect("/contacto/?error")

    return render(request, "contacto/contacto.html", {"formulario": formularioContacto})
