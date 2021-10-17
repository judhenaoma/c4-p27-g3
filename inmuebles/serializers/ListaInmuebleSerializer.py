from rest_framework import serializers
from ..models.inmueble import Inmueble


class InmuebleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inmueble
        fields = ['usuario_id', 'departamento', 'municipio', 'imagenes1']
