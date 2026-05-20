# Guía Didáctica — Django: Plantillas, Herencia y el Patrón MTV

## Índice

1. [¿Qué son las plantillas (templates)?](#1-qué-son-las-plantillas-templates)
2. [El motor de plantillas de Django (Django Template Language)](#2-el-motor-de-plantillas-de-django-django-template-language)
3. [Herencia de plantillas](#3-herencia-de-plantillas)
4. [block, extends e include](#4-block-extends-e-include)
5. [Estructura de base.html: header, navbar y footer](#5-estructura-de-basehtml-header-navbar-y-footer)
6. [Patrón MTV: Model-Template-View](#6-patrón-mtv-model-template-view)
7. [Principio DRY aplicado a plantillas](#7-principio-dry-aplicado-a-plantillas)
8. [Validación de formularios en backend con Django](#8-validación-de-formularios-en-backend-con-django)
9. [Paso a paso: Levantamiento del proyecto](#9-paso-a-paso-levantamiento-del-proyecto)
10. [Estructura final del proyecto](#10-estructura-final-del-proyecto)

---

## 1. ¿Qué son las plantillas (templates)?

Las **plantillas** (o *templates*) son archivos HTML que contienen **marcadores especiales** (llamados *tags* y *variables*) que Django interpreta para generar páginas HTML dinámicas.

En el patrón **MTV** (Model-Template-View), la **T** es la plantilla. Es la capa encargada de la **presentación**: cómo se ve la información que el usuario ve en el navegador.

Una plantilla puede contener:

- HTML común (estructura, estilos, scripts)
- **Variables**: `{{ variable }}` — se reemplazan con datos enviados desde la vista
- **Tags**: `{% tag %}` — controlan la lógica (bucles, condicionales, herencia)
- **Filtros**: `{{ variable|filtro }}` — modifican el valor de una variable (ej: `{{ texto|upper }}`)

### Ejemplo básico

```html
<!-- plantilla simple -->
<h1>Hola, {{ nombre }}</h1>
{% if edad >= 18 %}
    <p>Eres mayor de edad.</p>
{% endif %}
```

---

## 2. El motor de plantillas de Django (Django Template Language)

Django incluye su propio motor de plantillas: el **Django Template Language (DTL)**. No necesitas instalar nada adicional.

Características principales:

- **Variables con doble llave**: `{{ variable }}`
- **Tags con llave + porcentaje**: `{% tag %}`
- **Herencia**: `{% extends %}` y `{% block %}`
- **Reutilización**: `{% include %}`
- **Bucles**: `{% for item in lista %} ... {% endfor %}`
- **Condicionales**: `{% if condicion %} ... {% endif %}`
- **Filtros**: `{{ texto|lower }}`, `{{ fecha|date:"d/m/Y" }}`
- **URLs dinámicas**: `{% url 'nombre_ruta' %}`

> Las plantillas se buscan en `mi_app/templates/` (por cada app) gracias a `APP_DIRS = True` en `settings.py`.

---

## 3. Herencia de plantillas

La **herencia de plantillas** es el mecanismo más poderoso del DTL. Permite definir una plantilla **base** con la estructura común del sitio y luego **extenderla** desde otras plantillas que solo definen el contenido específico de cada página.

### Analogía

Imaginá una casa:

- **base.html** = los cimientos, paredes, techo (estructura general)
- **formulario.html** = el living amueblado (hereda la estructura, cambia el contenido)
- **exito.html** = el dormitorio (hereda la misma estructura, cambia el contenido)

### Ventajas

- **DRY**: No repetís header, navbar y footer en cada página
- **Consistencia**: Cambiás el header una sola vez y se refleja en todas las páginas
- **Mantenibilidad**: Menos código, menos errores

---

## 4. block, extends e include

### `{% extends %}`

Indica que una plantilla **hereda** de otra. Debe ser el **primer tag** en el archivo.

```html
{% extends "mi_app/base.html" %}
```

### `{% block %}`

Define **secciones reemplazables** en la plantilla base. Las plantillas hijas llenan esos bloques con su contenido.

**En base.html (padre):**
```html
{% block content %}
{% endblock %}
```

**En formulario.html (hija):**
```html
{% block content %}
    <h2>Formulario</h2>
    ...
{% endblock %}
```

Si una hija no define un bloque, se usa el contenido por defecto del padre (si lo tiene).

### `{% include %}}

Inserta el contenido de otra plantilla dentro de la actual. Útil para componentes reutilizables.

```html
{% include "mi_app/menu.html" %}
```

A diferencia de `extends`, `include` **no crea herencia**, solo copia el contenido en ese punto.

---

## 5. Estructura de base.html: header, navbar y footer

`base.html` es la **plantilla raíz** de todo el sitio. Contiene los elementos que se repiten en todas las páginas:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Mi Sitio{% endblock %}</title>
</head>
<body>

    <!-- HEADER: aparece arriba en todas las páginas -->
    <header>
        <h1>Mi Proyecto Django</h1>
        <p>Aprendiendo el patrón MTV</p>
    </header>

    <!-- NAVBAR: menú de navegación -->
    <nav>
        <a href="{% url 'formulario' %}">Formulario</a>
        <a href="{% url 'exito' %}">Éxito</a>
    </nav>

    <!-- CONTENT: bloque que cada página hija llena -->
    <main>
        {% block content %}
        {% endblock %}
    </main>

    <!-- FOOTER: aparece abajo en todas las páginas -->
    <footer>
        <p>&copy; 2026 Django Práctico 3</p>
    </footer>

</body>
</html>
```

### ¿Por qué van en base.html?

| Elemento | Motivo |
|----------|--------|
| **header** | El título y logo del sitio son iguales en todas las páginas |
| **navbar** | El menú de navegación debe ser idéntico para mantener la UX |
| **footer** | Copyright, links legales y créditos van al pie siempre |
| **{% block content %}** | Es el "hueco" que cada página llena con su contenido específico |

---

## 6. Patrón MTV: Model-Template-View

Django sigue el patrón **MTV**, una variación del clásico MVC (Model-View-Controller).

| Capa | Archivo | Rol |
|------|---------|-----|
| **Model** | `models.py` | Define la estructura de datos (base de datos) |
| **Template** | `templates/` | Define la presentación (HTML) |
| **View** | `views.py` | Define la lógica de negocio (qué datos mostrar y cómo procesarlos) |

### Flujo de una petición

```
Usuario → URL (urls.py) → View (views.py) → Model (models.py) → DB
                                                      ↓
                                              Template (HTML)
                                                      ↓
                                              Respuesta al usuario
```

### Ejemplo con nuestro proyecto

1. El usuario visita `/` → `urls.py` dirige a `formulario_contacto`
2. La vista crea un `ContactoForm()` (que se basa en el modelo `Contacto`)
3. La vista renderiza `formulario.html` pasando el formulario como contexto
4. El usuario completa y envía → POST → la vista valida con `form.is_valid()`
5. Si es válido → `form.save()` guarda en DB → redirige a `/exito/`
6. Si no es válido → vuelve a mostrar el formulario con errores

---

## 7. Principio DRY aplicado a plantillas

**DRY = Don't Repeat Yourself (No te repitas)**

### Cómo aplicamos DRY en este proyecto

| Sin DRY (mal) | Con DRY (bien) |
|---------------|----------------|
| Cada página HTML tiene su propio header, navbar y footer repetidos | El header, navbar y footer están **una sola vez** en `base.html` |
| Si cambiás el menú, tenés que editar 3+ archivos | Cambiás una sola línea en `base.html` |
| El formulario HTML se escribe a mano en cada template | Usás `{{ form }}` o iterás `{% for field in form %}` |
| La validación se escribe en JS + backend duplicado | Django `ModelForm` genera los campos y la validación desde el modelo |

```python
# El formulario se define UNA vez desde el modelo
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto  # <-- aquí está el DRY: usamos el modelo existente
        fields = ["nombre", "email", "mensaje"]
```

---

## 8. Validación de formularios en backend con Django

La validación **en backend** significa que los datos se verifican **en el servidor** (no solo en el navegador con JavaScript). Esto es obligatorio por seguridad: el usuario podría desactivar JS o manipular la petición.

### Validación automática (ModelForm)

Django `ModelForm` ya valida automáticamente:

- **Tipos de datos**: un `EmailField` solo acepta emails válidos
- **Campos requeridos**: si un campo es obligatorio en el modelo, el form lo exige
- **Longitud máxima**: `CharField(max_length=100)` rechaza textos más largos

### Validación personalizada

Agregamos nuestro propio validador en `forms.py`:

```python
def clean_mensaje(self):
    mensaje = self.cleaned_data.get("mensaje")
    if len(mensaje) < 10:
        raise ValidationError("El mensaje debe tener al menos 10 caracteres.")
    return mensaje
```

- El método `clean_<campo>()` se ejecuta automáticamente al llamar `form.is_valid()`
- Si lanza `ValidationError`, el error se asocia al campo y se muestra en el template
- Nunca llega a la base de datos si no pasa la validación

### Mostrar errores en el template

```html
{% for field in form %}
    {{ field }}
    {% if field.errors %}
        {% for error in field.errors %}
            <small class="text-danger">{{ error }}</small>
        {% endfor %}
    {% endif %}
{% endfor %}
```

### Flujo completo de validación

```
POST / → form = ContactoForm(request.POST)
            ↓
       form.is_valid() ?
         ↓       ↓
       TRUE    FALSE
         ↓       ↓
    form.save()  → vuelve al template con errores
    redirect()
```

---

## 9. Paso a paso: Levantamiento del proyecto

### Requisitos

- Python 3.10+
- pip (gestor de paquetes)

### Paso 1: Clonar el repositorio

```bash
git clone <repo-url> django-practico3
cd django-practico3
```

### Paso 2: Crear y activar el entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate      # Linux/Mac
# .venv\Scripts\activate       # Windows
```

### Paso 3: Instalar dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Migrar la base de datos

```bash
python manage.py makemigrations
python manage.py migrate
```

### Paso 5: (Opcional) Crear superusuario para admin

```bash
python manage.py createsuperuser
```

### Paso 6: Iniciar el servidor

```bash
python manage.py runserver
```

### Paso 7: Abrir en el navegador

- Formulario: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### Paso 8: Probar la validación

1. Enviar el formulario vacío → ver errores de campos requeridos
2. Ingresar un email inválido → error de validación de email
3. Escribir un mensaje de menos de 10 caracteres → error personalizado
4. Completar todo correctamente → redirige a la página de éxito

---

## 10. Estructura final del proyecto

```
django-practico3/
├── .venv/                         # Entorno virtual (no se sube al repo)
├── django_project/                # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py                # Config: apps, BD, templates, idioma
│   ├── urls.py                    # URLs raíz (incluye las de mi_app)
│   ├── asgi.py
│   └── wsgi.py
├── mi_app/                        # Aplicación principal
│   ├── __init__.py
│   ├── admin.py                   # Registro del modelo en admin
│   ├── apps.py
│   ├── forms.py                   # Formulario con validación backend
│   ├── models.py                  # Modelo Contacto
│   ├── urls.py                    # Rutas de la app (/, /exito)
│   ├── views.py                   # Vistas (lógica de negocio)
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   └── templates/
│       └── mi_app/
│           ├── base.html          # Plantilla base con header, navbar, footer
│           ├── formulario.html    # Formulario (hereda base.html)
│           └── exito.html         # Confirmación (hereda base.html)
├── manage.py                      # Utilidad de gestión de Django
├── requirements.txt               # Dependencias del proyecto
├── GUIA_DIDACTICA.md              # Esta guía
└── README.md                      # Resumen del proyecto
```

---

## Conclusión

Este proyecto demuestra:

- **Herencia de plantillas** con `base.html` → formulario y éxito
- **DRY**: header, navbar y footer escritos una sola vez
- **Patrón MTV**: Model (`Contacto`), Template (`.html`), View (funciones)
- **Validación backend**: con `ModelForm` + `clean_mensaje()` personalizado
- **Entorno virtual**: dependencias aisladas
- **SQLite3**: base de datos embebida, sin configuración adicional

Todo el código sigue las mejores prácticas de Django 6 y está listo para ser extendido.
