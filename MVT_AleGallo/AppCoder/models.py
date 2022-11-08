from django.db import models
import datetime

# Create your models here.
class Persona(models.Model):

    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    # fecha_nacimiento = models.DateField(default=datetime.now)
    email = models.EmailField()