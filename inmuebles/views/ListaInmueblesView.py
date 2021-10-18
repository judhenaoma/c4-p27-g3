from django.db import reset_queries
from ..models.inmueble import Inmueble
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.InmuebleSerializer import InmuebleSerializer



class ListaInmuebleesView(APIView):

    def get(self, request, format = None):


        try:
            inmuebles = Inmueble.objects.all()
            serializador = InmuebleSerializer(inmuebles, many= True)


            return Response(
                {'inmuebles':serializador.data},
                status = status.HTTP_200_OK
            )
        
        except Exception as err:

            return Response(
                {f"Problema inesperado con el servidor. Error: {err}"}
            )

