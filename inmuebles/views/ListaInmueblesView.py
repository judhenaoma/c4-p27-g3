from django.db import reset_queries
from ..models.inmueble import Inmueble
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.InmuebleSerializer import InmuebleSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView


class ListaInmueblesView(ListAPIView):
   
    queryset = Inmueble.objects. all()
    serializer_class = InmuebleSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['titulo', 'descripcion', 'municipio']
 


 # class ListaInmueblesView(APIView):

#     def get(self, request, format = None):


#         try:
#             inmuebles = Inmueble.objects.all()
#             serializador = InmuebleSerializer(inmuebles, many= True)
   


#             return Response(
#                 {'inmuebles':serializador.data},
#                 status = status.HTTP_200_OK
#             )
        
#         except Exception as err:

#             return Response(
#                 {f"Problema inesperado con el servidor. Error: {err}"}
#             )
