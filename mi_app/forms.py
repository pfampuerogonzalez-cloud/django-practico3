from django import forms
from django.core.exceptions import ValidationError
from .models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ["nombre", "email", "mensaje"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Tu nombre"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "tu@email.com"}),
            "mensaje": forms.Textarea(attrs={"class": "form-control", "placeholder": "Escribí tu mensaje aquí...", "rows": 5}),
        }

    def clean_mensaje(self):
        mensaje = self.cleaned_data.get("mensaje")
        if len(mensaje) < 10:
            raise ValidationError("El mensaje debe tener al menos 10 caracteres.")
        return mensaje
