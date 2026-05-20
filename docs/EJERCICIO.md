# Ejercicio: Crear una página "Acerca de" con herencia de plantillas

## Objetivo

Crear una nueva página `/acerca-de/` que herede de `base.html` y practicar los tags `{% extends %}`, `{% block %}`, `{% for %}`, `{% if %}`, `{% url %}` y `{% include %}`.

## Paso a paso

### 1. Agregar la URL

Abrí `mi_app/urls.py` y agregá esta línea dentro de `urlpatterns`:

```python
path("acerca-de/", views.acerca_de, name="acerca_de"),
```

### 2. Agregar la vista

Abrí `mi_app/views.py` y agregá esta función:

```python
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
```

### 3. Crear la plantilla `acerca_de.html`

Creá `mi_app/templates/mi_app/acerca_de.html` con este contenido:

```html
{% extends "mi_app/base.html" %}

{% block title %}Acerca de{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-8 mx-auto">
        <h2>Acerca de {{ nombre_app }}</h2>
        <p>Versión: <strong>{{ version }}</strong></p>

        <h4>Características</h4>
        <ul>
            {% for c in caracteristicas %}
                <li>{{ c }}</li>
            {% endfor %}
        </ul>

        {% if mostrar_creditos %}
            <hr>
            <p class="text-muted">
                Desarrollado con Django {{ version }} · 
                <a href="{% url 'formulario' %}">Volver al formulario</a>
            </p>
        {% endif %}
    </div>
</div>
{% endblock %}
```

### 4. Probar

```bash
source .venv/bin/activate
python manage.py runserver
```

Abrí [http://127.0.0.1:8000/acerca-de/](http://127.0.0.1:8000/acerca-de/)

### 5. Bonus: experimentar

Probá estos cambios uno por uno para ver qué pasa:

| Cambio | Efecto |
|--------|--------|
| Borrar `{% extends "mi_app/base.html" %}` | La página pierde header, navbar y footer |
| Sacar `{% block title %}` | Aparece el title por defecto de base.html |
| Cambiar `mostrar_creditos: True` por `mostrar_creditos: False` en la vista | Desaparece el bloque de créditos |
| Poner `{% include "mi_app/otro_template.html" %}` dentro del bloque | Permite reutilizar un fragmento HTML |

### 6. Bonus 2: include

Creá `mi_app/templates/mi_app/creditos.html`:

```html
<p class="text-muted">© 2026 - Proyecto de práctica Django.</p>
```

Y en `acerca_de.html` reemplazá el hr + p por:

```html
{% include "mi_app/creditos.html" %}
```

---

## Consigna final

Cuando completes todo deberías ver una página `/acerca-de/` con el mismo header, navbar y footer de `base.html`, pero con contenido propio en el medio. Si ves eso, entendiste herencia de plantillas.
