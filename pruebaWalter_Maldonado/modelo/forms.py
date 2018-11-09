from django import forms
from modelo.models import Estudiante

class FormularioEstudiante(forms.ModelForm):
    class Meta:
        model= Estudiante
        fields = ["cedula", "nombres", "apellidos", "estado", "matricula", "ciclo", "carrera"]