from django.db import reset_queries
from ..models.inmueble import Inmueble
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.InmuebleSerializer import InmuebleSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions


class ListarInmueblesHostView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):

        try:
            if not request.user.is_host:
                return Response(
                    {'error': 'Usted no tiene permisos suficientes para estar aquií'},
                    status = status.HTTP_401_UNAUTHORIZED
                )
            
            User = get_user_model()
            user_log = request.user

            id_usuario_log = User.objects.get(id= user_log.id)
            inmuebles = Inmueble.objects.all()
            if not Inmueble.objects.filter(usuario_id = id_usuario_log).exists():
                return Response(
                    {'error':'No hay información para este usuario'},
                    status = status.HTTP_404_NOT_FOUND
                )
            else:
                inmuebles_host = Inmueble.objects.filter(usuario_id = id_usuario_log)
                serializador = InmuebleSerializer(inmuebles_host, many=True)
                return Response(
                    
                    {'inmuebles': serializador.data},
                    status = status.HTTP_200_OK

                )

        
        except Exception as err:
            return Response(
                {'error':'Hubo un error en el servidor',
                'tipo-error': str(err)},
                status= status.HTTP_500_INTERNAL_SERVER_ERROR
            )

