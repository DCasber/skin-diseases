from django.shortcuts import render

# Create your views here.


def diagnostico(request):

    return render(request, "diagnostico/diagnostico.html")
