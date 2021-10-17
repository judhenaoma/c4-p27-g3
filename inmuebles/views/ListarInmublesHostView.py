from django.db import reset_queries
from ..models.inmueble import Inmueble
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.ListaInmuebleSerializer import InmuebleSerializer
from django.contrib.auth import get_user_model
from rest_framework import permissions


# class ListarInmueblesHostView(APIView):

#     permission_classes = (permissions.IsAuthenticated)

#     def get(self, request, format=None):

#         try:
#             if not request.user.is_host:
#                 return Response(
#                     {'error': 'Usted no tiene permisos suficientes para estar aquií'},
#                     status = status.HTTP_401_UNAUTHORIZED
#                 )
            
#             User = get_user_model()
#             inmuebles = User.objects.all()
#             if not User.objects.filter(username = request.user.username).exists():
#                 return Response(
#                     {'eror':'No hay información para este usuario'},
#                     status = status.HTTP_404_NOT_FOUND
#                 )
#             else:
#                 inmuebles_host = User.objects.filter(username = request.user.username).order_by('-fechacreacion')
#                 serializador = InmuebleSerializer(inmuebles_host, many=True)
#                 return Response(
                    
#                     {'data': serializador.data},
#                     status = status.HTTP_200_OK

#                 )

        
#         except:
#             return Response(
#                 {'error':'Hubo un error en el servidor'},
#                 status= status.HTTP_500_INTERNAL_SERVER_ERROR
#             )

