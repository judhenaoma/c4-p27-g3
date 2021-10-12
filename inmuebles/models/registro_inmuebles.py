from django.db import models
from django.db.models.fields import BooleanField, CharField, FloatField, IntegerField, SmallIntegerField
from django.db.models.fields.files import ImageField
from .user import User
from .inmueble import Inmueble


class RegistroInmueble(models.Model):

    id = models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, related_name='registro', on_delete= models.CASCADE)
    id_inmueble = models.ForeignKey(Inmueble, related_name='registro', on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()