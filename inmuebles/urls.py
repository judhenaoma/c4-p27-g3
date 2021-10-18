from django.urls import path
from .views.registroUserView import registroUserView
from .views.detalleUserView import detalleUserView
from .views.ListaInmueblesView import ListaInmuebleesView
from .views.CrearInmuebleView import CrearInmuebleView
from .views.EliminarInmuebleView import EliminarInmuebleView
from .views.ListarInmublesHostView import ListarInmueblesHostView
from .views.DetalleInmuebleView import DetalleInmueble
from .views.ActualizarInmuebleView import ActualizarInmuebleView




urlpatterns = [
    path('usuario/registro/', registroUserView.as_view()),
    path('usuario/detalle-usuario/', detalleUserView.as_view()),
    path('lista-inmuebles/', ListaInmuebleesView.as_view()),
    path('crear-inmueble/', CrearInmuebleView.as_view()),
    path('eliminar-inmueble/<int:pk>/', EliminarInmuebleView.as_view()),
    path('lista-inmuebles-host/', ListarInmueblesHostView.as_view()),
    path('inmueble/<slug:url_id>/', DetalleInmueble.as_view()),
    path('lista-inmuebles-host/modificar/<int:inmueble_id>/', ActualizarInmuebleView.as_view())

]


