
from django.contrib import admin

from .models import Estudiante

class AdminEstudiante(admin.ModelAdmin):
    list_display = ["cedula", "apellidos", "nombres","estado"]
    list_editable = ["apellidos", "nombres",]
    search_fields = ["cedula"]

    class Meta:
        model = Estudiante

admin.site.register(Estudiante, AdminEstudiante)
