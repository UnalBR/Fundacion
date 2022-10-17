#creacion de urls app//6
from django.urls import path

from GestionIPS.viewOficios import OficioView
from GestionIPS.viewEntidadSalud import Entidad_saludView
from GestionIPS.viewCondicion import CondicionView
from GestionIPS.viewTransaccion import TransaccionView
from GestionIPS.viewUsuarios import UsuariosView
from GestionIPS.viewAgendamiento import AgendamientoView
from GestionIPS.viewEmpleados import EmpleadosView
from GestionIPS.viewFrontendOfic import *
from GestionIPS.viewFrontendAgend import *
from GestionIPS.viewFrontendCondi import *
from GestionIPS.viewFrontendEmpleados import *
from GestionIPS.viewFrontendEntidadS import *
from GestionIPS.viewFrontendTransac import *
from GestionIPS.viewFrontendUsua import *

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
    path('Condiciones/<str:condic>',CondicionView.as_view(),name='BuscarCondiciones'),
    path('Usuarios/<str:usua>',UsuariosView.as_view(),name='BuscarUsuarios'),
    path('Agendamientos/<str:agend>',AgendamientoView.as_view(),name='BuscarAgendamientos'),
    path('Empleados/<str:emple>',EmpleadosView.as_view(),name='BuscarEmpleados'),
    path('', principal, name="index"),#
    path('listaOficios/', listaOficios, name='Lista'),
    path('listaAgendamientos/', listaAgendamientos, name='Lista'),
    path('listaCondiciones/', listaCondiciones, name='Lista'),
    path('listaEmpleados/', listaEmpleados, name='Lista'),
    path('listaEntidadesSalud/', listaEntidades, name='Lista'),
    path('listaTransacciones/', listaTransacciones, name='Lista'),
    path('listaUsuarios/', listaUsuarios, name='Lista'),#
    path('consultaOficio/',consultaOficio,name='consultarIdOficio'),
    path('consultaAgendamiento/',consultaAgendamiento,name='consultarIdOficio'),
    path('consultaCondicion/',consultaCondicion,name='consultarIdOficio'),
    path('consultaEmpleado/',consultaEmpleado,name='consultarIdOficio'),
    path('consultaEntidad/',consultaEntidad,name='consultarIdOficio'),
    path('consultaTransaccion/',consultaTransaccion,name='consultarIdOficio'),
    path('consultaUsuario/',consultaUsuario,name='consultarIdOficio'),
    path('formOficios/',formularioOficios, name="formulario"),#
    path('formAgendamientos/',formularioAgendamientos, name="formulario"),
    path('formCondiciones/',formularioCondiciones, name="formulario"),
    path('formEmpleados/',formularioEmpleados, name="formulario"),
    path('formEntidades_salud/',formularioEntidades, name="formulario"),
    path('formTransacciones/',formularioTransacciones, name="formulario"),
    path('formUsuarios/',formularioUsuarios, name="formulario"),
    path('guardarOficio/', guardarOficio, name='registrar'),#
    path('guardarAgendamiento/', guardarAgendamiento, name='registrar'),
    path('guardarCondicion/', guardarCondicion, name='registrar'),
    path('guardarEmpleado/', guardarEmpleado, name='registrar'),
    path('guardarEntidad/', guardarEntidad, name='registrar'),
    path('guardarTransaccion/', guardarTransaccion, name='registrar'),
    path('guardarUsuario/', guardarUsuario, name='registrar'),
    path('cargarOficio/<str:idOficio>',cargarOficio, name='formularioOficio'),#
    path('cargarAgendamiento/<str:idAgendamiento>',cargarAgendamiento, name='formularioAgendamiento'),
    path('cargarCondicion/<str:idCondicion>',cargarCondicion, name='formularioCondicion'),
    path('cargarEmpleado/<str:idEmpleados>',cargarEmpleado, name='formularioEmpleado'),
    path('cargarEntidad/<str:idEntidad>',cargarEntidad, name='formularioEntidad'),
    path('cargarTransaccion/<str:idTransaccion>',cargarTransaccion, name='formularioTransaccion'),
    path('cargarUsuario/<str:id_Usuario>',cargarUsuario, name='formularioUsuario'),
    path('actualizarOficio/', actualizarOficio, name='actualizarOficio'),#
    path('actualizarAgendamiento/', actualizarAgendamiento, name='actualizarAgendamiento'),
    path('actualizarCondicion/', actualizarCondicion, name='actualizarCondicion'),
    path('actualizarEmpleado/', actualizarEmpleado, name='actualizarEmpleado'),
    path('actualizarEntidad/', actualizarEntidad, name='actualizarEntidad'),
    path('actualizarTransaccion/', actualizarTransaccion, name='actualizarTransaccion'),
    path('actualizarUsuario/', actualizarUsuario, name='actualizarUsuario'),
    path('eliminarOficio/<str:idOficio>',eliminarOficio, name='eliminarOficio'),#
    path('eliminarAgendamiento/<str:idAgendamiento>',eliminarAgendamiento, name='eliminarAgendamiento'),
    path('eliminarCondicion/<str:idCondicion>',eliminarCondicion, name='eliminarCondicion'),
    path('eliminarEmpleado/<str:idEmpleados>',eliminarEmpleado, name='eliminarEmpleado'),
    path('eliminarEntidad/<str:idEntidad>',eliminarEntidad, name='eliminarEntidad'),
    path('eliminarTransaccion/<str:idTransaccion>',eliminarTransaccion, name='eliminarTransaccion'),
    path('eliminarUsuario/<str:id_Usuario>',eliminarUsuario, name='eliminarUsuario')
]
