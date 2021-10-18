from rest_framework.views import APIView
from ..models.inmueble import Inmueble
from rest_framework.response import Response
from rest_framework import status
from ..serializers.InmuebleSerializer import InmuebleSerializer



class DetalleInmueble(APIView):

    def get(self, request, url_id, format = None):

        # Otra forma de obtener el slug pasado en la url es a través de:
        # request.query_params.get('slug')
        try:
            
            if not Inmueble.objects.filter(id_url = url_id).exists():
                return Response({'error':'El inmueble seleccionado no existe'},
                status = status.HTTP_404_NOT_FOUND)
            else:
                seleccionado = Inmueble.objects.get(id_url = url_id)
                serializador = InmuebleSerializer(seleccionado)
                return Response({
                    'data': serializador.data
                },
                status= status.HTTP_200_OK)


        except Exception as err:
            return Response({
                'error':'Algo inesperado sucedió en el servidor',
                'tipo_error':str(err)
            }, 
            status = status.HTTP_500_INTERNAL_SERVER_ERROR)
