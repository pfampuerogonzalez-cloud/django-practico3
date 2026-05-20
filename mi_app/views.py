from django.shortcuts import render, redirect
from .forms import ContactoForm


def formulario_contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("exito")
    else:
        form = ContactoForm()
    return render(request, "mi_app/formulario.html", {"form": form})


def exito(request):
    return render(request, "mi_app/exito.html")

def acerca_de(request):
    datos = {
        "nombre_app": "Django Práctico 3",
        "version": "6.0.5",
        "caracteristicas": [
            "Herencia de plantillas",
            "Formularios con validación",
            "Patrón MTV",
            "Principio DRY",
        ],
        "mostrar_creditos": True,
    }
    return render(request, "mi_app/acerca_de.html", datos)



