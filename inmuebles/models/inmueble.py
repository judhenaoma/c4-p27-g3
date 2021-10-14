from .user import User
from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, FloatField, IntegerField, SmallIntegerField
from django.db.models.fields.files import ImageField
from PIL import Image, ImageChops, ImageEnhance, ImageOps
from django.utils.timezone import now




class Inmueble(models.Model):
    TIPOS_INMUEBLES = [
    ('AP', 'Apartamento'),
    ('FC', 'Finca'),
    ('CS', 'Casa'),
    ('AS', 'Aparta-estudios'),
]
    id = models.BigAutoField(primary_key=True)
    usuario_id = models.ForeignKey(User, related_name='inmuebles',on_delete=models.CASCADE)
    departamento = CharField(max_length=50)
    municipio = CharField(max_length=50)
    tipo_inmueble = CharField(max_length=100, choices=TIPOS_INMUEBLES)
    descripcion = CharField(max_length=500, default="No hay descripción")
    precio = IntegerField(null = False)
    num_habitaciones = IntegerField(null = False)
    num_baños = IntegerField(null = False)
    area = CharField(max_length=20)
    aparcamiento = BooleanField(default=False)
    amoblado = BooleanField(default=False)
    piscina = BooleanField(default=False)
    direccion = CharField(max_length=100)
    latitud = FloatField(null = False)
    longitud = FloatField(null = False)
    seguridad = BooleanField(default=False)
    imagenesPrincipal = models.ImageField(upload_to = 'inmuebles/', null = True)
    imagenes1 = ImageField(upload_to = 'inmuebles/', null = True)
    imagenes2 = ImageField(upload_to = 'inmuebles/', null = True)
    imagenes3 = ImageField(upload_to = 'inmuebles/', null = True)
    fechacreacion = DateField(default=now)