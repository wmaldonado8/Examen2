from django.db import models

# Create your models here.
class Estudiante(models.Model):

    cedula = models.CharField(max_length=10,unique=True, null=False)
    apellidos = models.CharField(max_length=70,  null=False)
    nombres = models.CharField(max_length=70,  null=False)
    estado = models.BooleanField(default=True)
    matricula=models.CharField(max_length=10,unique=True, null=False)
    ciclo=models.CharField(max_length=10,unique=True, null=False)
    carrera=models.CharField(max_length=70,unique=True, null=False)
