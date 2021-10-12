from django.db import models
from django.db.models.fields import BooleanField, CharField, FloatField, IntegerField, SmallIntegerField
from django.db.models.fields.files import ImageField
from user import User




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
    imagenes = ImageField()