from django.db import models
from django.contrib.auth.models import User

# Create your models here.

"""
    Create Table Usuarios( nombre varchar,apellido varcahr() )


    python manage.py makemigrations
    python manage.py migrate
    python manage.py 

"""

class Tarea(models.Model):
    nombre = models.CharField(max_length=500,)
    estado = models.BooleanField(default=False)
    #usuario = models.ForeignKey(User,)