#creacion de urls app//6
from django.urls import path

from GestionIPS.viewOficios import OficioView
from GestionIPS.viewEntidadSalud import Entidad_saludView
from GestionIPS.viewCondicion import CondicionView
from GestionIPS.viewTransaccion import TransaccionView
from GestionIPS.viewUsuarios import UsuariosView
from GestionIPS.viewAgendamiento import AgendamientoView
from GestionIPS.viewEmpleados import EmpleadosView

urlpatterns =[
    path('Oficios/',OficioView.as_view(),name='ListarOficios'),
    path('Oficios/<str:ofic>',OficioView.as_view(),name='BuscarOficios'),
    path('Entidades_salud/',Entidad_saludView.as_view(),name='ListarEntidades'),
    path('Condiciones/',CondicionView.as_view(),name='ListarCondiciones'),
    path('Transacciones/',TransaccionView.as_view(),name='ListarTransacciones'),
    path('Transacciones/<str:Transac>',TransaccionView.as_view(),name='BuscarTransacciones'),
    path('Usuarios/',UsuariosView.as_view(),name='ListarUsuarios'),
    path('Agendamientos/',AgendamientoView.as_view(),name='ListarAgendamientos'),
    path('Empleados/',EmpleadosView.as_view(),name='ListarEmpleados'),
    path('Entidades_salud/<str:IDentidad>',Entidad_saludView.as_view(),name='BuscarEntidades'),
    path('CondicionesN/<str:IDCondicion>',CondicionView.as_view(),name='BuscarCondiciones'),
    path('UsuariosN/<str:IDUsuario>',UsuariosView.as_view(),name='BuscarUsuarios'),
    path('AgendamientosN/<str:IDAgendamiento>',AgendamientoView.as_view(),name='BuscarAgendamientos'),
    path('EmpleadosN/<str:IDEmpleados>',EmpleadosView.as_view(),name='BuscarEmpleados')
]
