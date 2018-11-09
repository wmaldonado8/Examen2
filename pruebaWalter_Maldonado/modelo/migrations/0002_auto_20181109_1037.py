# Generated by Django 2.1.3 on 2018-11-09 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10, unique=True)),
                ('apellidos', models.CharField(max_length=70)),
                ('nombres', models.CharField(max_length=70)),
                ('estado', models.BooleanField(default=True)),
                ('numMatricula', models.CharField(max_length=10, unique=True)),
                ('ciclo', models.CharField(max_length=10, unique=True)),
                ('carrera', models.CharField(max_length=70, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
