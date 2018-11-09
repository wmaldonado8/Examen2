from django.shortcuts import render, redirect
from modelo.models import Estudiante
from modelo.forms import FormularioEstudiante

# Create your views here.

def Principal(request):
    listaEstudiantes = Estudiante.objects.all().filter(estado=True)
    context = {
        'lista' : listaEstudiantes
    }
    return render(request, 'estudiante/principal_estudiante.html', context)

def crear(request):
    formulario = FormularioEstudiante(request.POST)
    if request.method == 'POST':
        if formulario.is_valid():
            datos = formulario.cleaned_data
            estudiante = Estudiante()
            estudiante.cedula = datos.get('cedula')
            estudiante.nombres = datos.get('nombres')
            estudiante.apellidos = datos.get('apellidos')
            estudiante.estado = datos.get('estado')
            estudiante.matricula = datos.get('matricula')
            estudiante.ciclo = datos.get('ciclo')
            estudiante.carrera = datos.get('carrera')
            estudiante.save()
            return redirect(Principal)

    context = {
        'f': formulario,
        'mensaje': 'Bienvenido',
    }
    return render(request, 'estudiante/crear_estudiante.html', context)