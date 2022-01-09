from django.urls import path
from .views import diagnostico

urlpatterns = [

    path('', diagnostico, name="Diagnostico"),
]
