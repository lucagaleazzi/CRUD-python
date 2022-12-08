from django.db import models

# Create your models here.
class familiar (models.Model):
    nombre = models.CharField (max_length = 25)
    apellido = models.CharField (max_length = 25)
    telefono = models.CharField (max_length = 13)
    fecha_nacimiento = models.DateField ()