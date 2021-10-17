import re
from django.db import reset_queries
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from ..models.inmueble import Inmueble
from ..serializers.ListaInmuebleSerializer import InmuebleSerializer
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
            municipio = inmueble['municipio']
            direccion = inmueble['direccion']
            precio = inmueble['precio']
            num_habitaciones= inmueble['num_habitaciones']
            num_baños = inmueble['num_habitaciones']
            area = inmueble['area']
            longitud = inmueble['longitud']
            latitud = inmueble['latitud']
            fechacreacion = inmueble['fechacreacion']
            imagenes1 = inmueble['imagenes1']

            Inmueble.objects.create(usuario_id = user_instance, 
            departamento = departamento, 
            municipio=direccion, 
            precio= precio,
            num_habitaciones = num_habitaciones,
            num_baños = num_baños,
            area = area,
            longitud = longitud,
            latitud = latitud,
            fechacreacion = fechacreacion,
            imagenes1 = imagenes1)

            
    
            return Response(
                {'mensaje':'Se ha creado correctamente el inmueble'},
                status = status.HTTP_200_OK
            )

        except Exception as err:
            return Response({'error':'Problema inesperado en el servidor',
            'error': str(err)},
                    status = status.HTTP_500_INTERNAL_SERVER_ERROR)


