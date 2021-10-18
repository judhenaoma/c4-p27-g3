from .user import User
from django.db import models
from django.db.models.fields import BooleanField, CharField, DateField, FloatField, IntegerField, SmallIntegerField
from django.db.models.fields.files import ImageField
from django.utils.timezone import now
from django.utils.text import slugify
from autoslug import AutoSlugField


class Inmueble(models.Model):
    TIPOS_INMUEBLES = [
    ('AP', 'Apartamento'),
    ('FC', 'Finca'),
    ('CS', 'Casa'),
    ('AS', 'Aparta-estudios'),
]
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=60, null=True)
    
    id_url = AutoSlugField(populate_from = 'titulo', unique = True, null=True)
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
    imagenPrincipal = models.ImageField(upload_to = 'inmuebles/', null = True)
    imagen1 = ImageField(upload_to = 'inmuebles/', null = True)
    imagen2 = ImageField(upload_to = 'inmuebles/', null = True)
    imagen3 = ImageField(upload_to = 'inmuebles/', null = True)
    fechacreacion = DateField(default=now())
    usuario_id = models.ForeignKey(User, related_name='inmuebles',on_delete=models.CASCADE)
