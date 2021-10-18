from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.inmueble import Inmueble
from rest_framework import permissions


class ActualizarInmuebleView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, inmueble_id):

        try:
            user = request.user

            if not user.is_host:
                return Response({
                    'error':'Usted no tiene permisos para estar aquí'
                }, status = status.HTTP_401_UNAUTHORIZED)
            
            if not Inmueble.objects.filter(id= inmueble_id, usuario_id = user.id).exists():
                return Response({'error':'El inmueble no existe para usted'},
                status = status.HTTP_400_BAD_REQUEST)

            
            inmueble = request.data


            departamento = inmueble['departamento']
            titulo = inmueble['titulo']
            municipio = inmueble['municipio']
            direccion = inmueble['direccion']
            precio = inmueble['precio']
            num_habitaciones= inmueble['num_habitaciones']
            num_baños = inmueble['num_habitaciones']
            area = inmueble['area']
            longitud = inmueble['longitud']
            latitud = inmueble['latitud']
            fechacreacion = inmueble['fechacreacion']
            imagen1 = inmueble['imagen1']

            Inmueble.objects.filter(usuario_id = user.id, id= inmueble_id).update(
                departamento = departamento, 
                municipio=direccion, 
                precio= precio,
                num_habitaciones = num_habitaciones,
                num_baños = num_baños,
                area = area,
                longitud = longitud,
                latitud = latitud,
                fechacreacion = fechacreacion,
                imagen1 = imagen1,
                titulo = titulo)
            return Response({'mensaje':'El inmueble se ha actualizado correctamentee'},
            status=status.HTTP_200_OK)
            

        except:
            return Response({'error':'Error inesperado en el servidor'},
            status= status.HTTP_500_INTERNAL_SERVER_ERROR)