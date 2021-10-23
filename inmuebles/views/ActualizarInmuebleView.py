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

            Inmueble.objects.filter(usuario_id = user.id, id= inmueble_id).update(
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
                imagen1 = imagen1)
                
            return Response({'mensaje':'El inmueble se ha actualizado correctamentee'},
                status=status.HTTP_200_OK)
            
        except Exception as err:
            return Response({'error':'Error inesperado en el servidor',
            'tipo_error':str(err)},
            status= status.HTTP_500_INTERNAL_SERVER_ERROR)