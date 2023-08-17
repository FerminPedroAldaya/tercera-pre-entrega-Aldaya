from django.db import models
#LOS TRES MODELOS USADOS PARA EL PROYECTO CON SUS RESPECTIVOS DATOS PARA LA BASE DE DATOS

class Empleos(models.Model):
    cargo = models.CharField(max_length=50)
    detalles = models.TextField()
    ubicacion = models.CharField(max_length=50)
    sueldo = models.CharField(max_length=50)

class Curriculum(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    presentacion = models.TextField()
    experiencia = models.TextField()
    estudios = models.CharField(max_length=256)

class Empleador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    profesion = models.CharField(max_length=50)
    edad = models.IntegerField(max_length=50)
    nombreEmpresa = models.CharField(max_length=50)

