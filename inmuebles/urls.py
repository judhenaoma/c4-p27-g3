from django.urls import path
from .views.registroUserView import registroUserView
from .views.detalleUserView import detalleUserView




urlpatterns = [
    path('usuario/registro/', registroUserView.as_view()),
    path('usuario/detalle-usuario/', detalleUserView.as_view()),
]


