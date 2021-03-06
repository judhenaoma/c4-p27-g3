from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()

class registroUserView(APIView):

    def post(self, request):

        try:
            
            data = request.data
            username = data['username']
            password = data['password']
            confirm_password = data['confirm_password']
            email = data['email']
            name = data['nombre']
            last_name = data['apellido']
            is_host = data['is_host']

            if is_host == "True":
                is_host = True
            elif is_host == "False":
                is_host = False
            else:
                return Response(
                    {'error':'Se debe especificar True o Falsee'},
                    status = status.HTTP_400_BAD_REQUEST
                )
            
            
            if password == confirm_password:
                if len(password) > 6:
                    if not User.objects.filter(username= username).exists() and not User.objects.filter(email=email):
                        if not is_host:
                            User.objects.create_user(username = username, 
                            password = password, 
                            email = email,
                            name = name,
                            last_name = last_name)

                            return Response(
                                {'Felicitaciones':'La cuenta de arrendatario se ha creeado correctamentee'},
                                status= status.HTTP_200_OK
                            )
                        else:
                            User.objects.create_userhost(username = username, 
                            password = password, 
                            email = email,
                            name = name,
                            last_name = last_name)
                            return Response(
                                {'Felicitaciones':'La cuenta de arrendador se ha creeado correctamentee'},
                                status= status.HTTP_200_OK
                            )
                    
                    else:
                        return Response(
                            {'error':'El usuario ya existe con el username o email dado'},
                            status = status.HTTP_400_BAD_REQUEST
                        )
                else:
                    return Response(
                        {'error':'Las contrase??as deben de tener m??s de 6 car??cterees'},
                        status = status.HTTP_400_BAD_REQUEST
                    )

            else:
                return Response({
                    'error':'Las contrase??as no coinciden'
                })


        except Exception as exc:
            return Response(
                {'error': 'Error inesperado desde el servidor',
                'tipo': str(exc)
                },
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )




        



        

