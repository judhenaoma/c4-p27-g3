from rest_framework.views import APIView
from ..models.inmueble import Inmueble
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

class EliminarInmuebleView(APIView):


    def get(self, request, pk, format=None):

        permission_classes = (permissions.IsAuthenticated)
        
        try:

            user = request.user

            if not user.is_host:

                return Response(
                    {'error':'Usted no tiene permisos para eliminar un inmueble'},
                    status= status.HTTP_401_UNAUTHORIZED
                )
            else:

                if Inmueble.objects.filter(id=pk).exists():
                    
                    Inmueble.objects.filter(id = pk).delete()
                    return Response({'éxito':f'El inmuble con id {pk} ha sido eliminado correctamente'})

                else:
                    return Response({'error':'El inmueble no existe'},
                    status= status.HTTP_404_NOT_FOUND) 

        except Exception as err:
            return Response(
                {'error':'Error interno del servidor',
                'error': str(err)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )