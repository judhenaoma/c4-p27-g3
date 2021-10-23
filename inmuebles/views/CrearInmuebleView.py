import re
from django.db import reset_queries
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from ..models.inmueble import Inmueble
from ..serializers.InmuebleSerializer import InmuebleSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions

class CrearInmuebleView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        try:
            
            user = request.user

            if not user.is_host:
                return Response(
                    {'error':'Este usuario no tiene permisos para crear un inmueble'},
                    status = status.HTTP_401_UNAUTHORIZED
                )

            inmueble = request.data
            User = get_user_model()
            user_instance = User.objects.get(id = user.id)

            departamento = inmueble['departamento']
            titulo = inmueble['titulo']
            descripcion = inmueble['descripcion']
            municipio = inmueble['municipio']
            direccion = inmueble['direccion']
            tipo_inmueble = inmueble['tipo_inmueble']
            precio = inmueble['precio']
            num_habitaciones= inmueble['num_habitaciones']
            num_baños = inmueble['num_habitaciones']
            area = inmueble['area']
            longitud = inmueble['longitud']
            latitud = inmueble['latitud']
            aparcamiento = inmueble['aparcamiento']
            amoblado = inmueble['amoblado']
            piscina = inmueble['piscina']
            imagen_principal = inmueble['imagen_principal']
            imagen1 = inmueble['imagen1']
            imagen2 = inmueble['imagen2']
            imagen3 = inmueble['imagen3']




            Inmueble.objects.create(usuario_id = user_instance, 
            departamento = departamento,
            descripcion = descripcion,
            tipo_inmueble = tipo_inmueble, 
            direccion = direccion,
            municipio=municipio, 
            precio= precio,
            num_habitaciones = num_habitaciones,
            num_baños = num_baños,
            area = area,
            longitud = longitud,
            latitud = latitud,
            titulo = titulo,
            aparcamiento = aparcamiento,
            amoblado = amoblado,
            piscina = piscina,
            imagenPrincipal = imagen_principal,
            imagen2 = imagen2,
            imagen3 = imagen3,
            imagen1 = imagen1
            
            )

            
    
            return Response(
                {'mensaje':'Se ha creado correctamente el inmueble'},
                status = status.HTTP_200_OK
            )

        except Exception as err:
            return Response({'error':'Problema inesperado en el servidor',
            'error': str(err)},
                    status = status.HTTP_500_INTERNAL_SERVER_ERROR)


