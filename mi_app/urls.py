from django.urls import path
from . import views

urlpatterns = [
    path("", views.formulario_contacto, name="formulario"),
    path("exito/", views.exito, name="exito"),
    path("acerca-de/", views.acerca_de, name="acerca_de"),
]
    
