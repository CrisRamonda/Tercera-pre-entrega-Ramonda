from django.db import models

# Create your models here.
class Habitacion(models.Model):
    numero = models.IntegerField()
    tipo = models.CharField(max_length=30)
    disponible = models.BooleanField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.IntegerField()
    email = models.EmailField(max_length=300)

class Reserva(models.Model):
    estado = models.BooleanField()
    fechainicio = models.DateField()
    fechafin = models.DateField()
    
    
