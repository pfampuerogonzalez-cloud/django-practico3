# Django Práctico 3

Proyecto Django 6 con SQLite3 que demuestra:

- **Herencia de plantillas** (`base.html` con header, navbar, footer)
- **Patrón MTV** (Model-Template-View)
- **Principio DRY** aplicado a templates y formularios
- **Formulario con validación backend** usando `ModelForm`
- **Entorno virtual** para dependencias aisladas

## Inicio rápido

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Documentación

Toda la documentación está en la carpeta [`docs/`](docs/):

| Archivo | Contenido |
|---------|-----------|
| [`GUIA_DIDACTICA.md`](docs/GUIA_DIDACTICA.md) | Tutorial completo: plantillas, herencia, DRY, MTV, validación |
| [`EJERCICIO.md`](docs/EJERCICIO.md) | Ejercicio práctico de herencia de plantillas |
| [`TAGS_REFERENCIA.md`](docs/TAGS_REFERENCIA.md) | Referencia completa de todos los tags del DTL |
