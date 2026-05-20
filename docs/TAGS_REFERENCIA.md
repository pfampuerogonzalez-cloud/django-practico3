# Django Template Language — Referencia completa de Tags

## 1. Tags de estructura

### `{% extends %}`
Hace que una plantilla herede de otra. **Debe ser el primer tag del archivo.**
```html
{% extends "mi_app/base.html" %}
```

### `{% block %}`
Define una sección que puede ser reemplazada por una plantilla hija.
```html
{% block nombre_del_bloque %}
  Contenido por defecto (opcional)
{% endblock %}
```

### `{% include %}`
Inserta el contenido de otra plantilla en la posición actual.
```html
{% include "mi_app/creditos.html" %}
```

---

## 2. Tags de variables

### `{{ }}`
Imprime el valor de una variable.
```html
{{ nombre }}
{{ usuario.edad }}
{{ lista.0 }}
```

### Filtros (se usan con `|`)
```html
{{ texto|upper }}           <!-- MAYÚSCULAS -->
{{ texto|lower }}           <!-- minúsculas -->
{{ texto|title }}           <!-- Primera Letra De Cada Palabra -->
{{ texto|capfirst }}        <!-- Primera letra de la frase -->
{{ texto|length }}          <!-- Cantidad de caracteres -->
{{ texto|truncatechars:30 }}<!-- Corta a 30 caracteres -->
{{ texto|default:"N/A" }}   <!-- Valor por defecto si está vacío -->
{{ numero|floatformat:2 }}  <!-- 3.1416 → 3.14 -->
{{ fecha|date:"d/m/Y" }}    <!-- 2026-05-19 → 19/05/2026 -->
{{ variable|safe }}          <!-- No escapa HTML (¡cuidado!) -->
```

---

## 3. Tags de control

### `{% if %}`, `{% elif %}`, `{% else %}`, `{% endif %}`
```html
{% if edad >= 18 %}
  <p>Mayor de edad</p>
{% elif edad >= 13 %}
  <p>Adolescente</p>
{% else %}
  <p>Menor</p>
{% endif %}
```

Operadores disponibles: `==`, `!=`, `<`, `>`, `<=`, `>=`, `in`, `not in`, `and`, `or`, `not`

### `{% for %}`, `{% endfor %}`
```html
{% for item in lista %}
  <li>{{ item }}</li>
{% empty %}
  <li>No hay elementos</li>
{% endfor %}
```

#### Variables especiales dentro del for
```html
{% for item in lista %}
  {{ forloop.counter }}      <!-- 1, 2, 3... -->
  {{ forloop.counter0 }}     <!-- 0, 1, 2... -->
  {{ forloop.first }}        <!-- True si es el primero -->
  {{ forloop.last }}         <!-- True si es el último -->
  {{ forloop.revcounter }}   <!-- Cuenta regresiva -->
{% endfor %}
```

### Combinación if + for
```html
{% for c in caracteristicas %}
  {% if forloop.first %}
    <strong>{{ c }}</strong>
  {% else %}
    {{ c }}
  {% endif %}
{% endfor %}
```

---

## 4. Tags de URLs

### `{% url %}`
Genera una URL a partir del nombre de la ruta.
```html
<a href="{% url 'formulario' %}">Formulario</a>
<a href="{% url 'acerca_de' %}">Acerca de</a>
```

Con parámetros:
```python
# urls.py
path("usuario/<int:id>/", views.perfil, name="perfil")
```
```html
<a href="{% url 'perfil' id=5 %}">Perfil</a>
```

---

## 5. Tags de formularios

### `{% csrf_token %}`
Token obligatorio dentro de todo `<form method="post">`. Protege contra CSRF.
```html
<form method="post">
  {% csrf_token %}
  ...
</form>
```

---

## 6. Tags de carga

### `{% load %}`
Carga librerías de tags personalizadas o de terceros.
```html
{% load static %}
{% load humanize %}
```

### `{% static %}`
Genera URL para archivos estáticos (CSS, JS, imágenes).
```html
{% load static %}
<img src="{% static 'img/logo.png' %}">
```

---

## 7. Otros tags útiles

### `{% comment %}`
Comentarios que no se renderizan.
```html
{% comment %}
  Esto no aparece en el HTML final
{% endcomment %}
```

### `{% now %}`
Imprime la fecha/hora actual.
```html
{% now "d/m/Y H:i" %}
```

### `{% autoescape %}`
Controla el escape automático de HTML.
```html
{% autoescape off %}
  {{ variable_con_html }}
{% endautoescape %}
```

---

## 8. Combinaciones prácticas

```html
{% extends "mi_app/base.html" %}

{% block title %}Mi Página{% endblock %}

{% block content %}
  <h1>Bienvenido, {{ user.nombre|default:"Invitado" }}</h1>

  {% if user.is_authenticated %}
    <p>Email: {{ user.email }}</p>
    <ul>
      {% for item in user.items.all %}
        <li>{{ forloop.counter }}. {{ item.nombre }}</li>
      {% empty %}
        <li>Sin items</li>
      {% endfor %}
    </ul>
  {% else %}
    <a href="{% url 'login' %}">Iniciar sesión</a>
  {% endif %}

  {% include "mi_app/creditos.html" %}
{% endblock %}
```

---

## Resumen rápido

| Tag | Para qué sirve |
|-----|---------------|
| `{{ var }}` | Imprime variable |
| `{% if %}` | Condicional |
| `{% for %}` | Bucle |
| `{% extends %}` | Herencia (1° línea) |
| `{% block %}` | Sección reemplazable |
| `{% include %}` | Inserta otro template |
| `{% url %}` | Link dinámico |
| `{% csrf_token %}` | Seguridad en forms |
| `{% load %}` | Carga librerías |
| `{% comment %}` | Comentario |
| `{% now %}` | Fecha actual |
| `{{ var|filtro }}` | Transforma variable |

> 💡 **Tip:** Todos los tags se cierran con `{% end... %}` (excepto `extends`, `include`, `load`, `csrf_token`, `comment` y `now` que son auto-contenidos).
