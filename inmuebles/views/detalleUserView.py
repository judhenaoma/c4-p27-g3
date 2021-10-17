from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions
from ..serializers.detalleUserSerializer import DetalleUserSerializer, User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model


class detalleUserView(APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):

        try:
            User = get_user_model()
            
            user = request.user 
            user = DetalleUserSerializer(user)

            if user:
            
                return Response(
                    {'user': user.data},
                    status = status.HTTP_200_OK
                )
            else:
                return Response(
                    {'error:' 'No es valido la información solicitada con el get'},
                    status = status.HTTP_500_INTERNAL_SERVER_ERROR
                )


        except Exception as exc:
            return Response(
                {'error':'Algo estuvo mal con el servidor al recuperar la info del usuario',
                'tipo de error': str(exc)},

                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )
