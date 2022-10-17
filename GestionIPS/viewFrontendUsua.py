import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

def principal(request):
    return render(request, "index.html")

def listaUsuarios(request):
    response=requests.get('http://localhost:8000/ingreso/Usuarios')
    usuarios=response.json()
    print(usuarios)
    return render(request, "usuarios.html",usuarios)

def consultaUsuario(request):
    dato=request.POST['id_Usuario']
    response=requests.get('http://localhost:8000/ingreso/Usuarios/'+dato)
    usuario=response.json()
    print(usuario)
    return render(request,'usuarios.html',usuario)

def formularioUsuarios(request):
    return render(request, 'formUsuarios.html')

def guardarUsuario(request):
    datos={
        "id_Usuario": request.POST['id_Usuario'],
        "nombres_u": request.POST['nombres_u'],
        "apellidos_u": request.POST['apellidos_u'],
        "documento_u": request.POST['documento_u'],
        "email_u": request.POST['email_u'],
        "telefono_u": request.POST['telefono_u'],
        "direccion_u": request.POST['direccion_u'],
        "nombre_r": request.POST['nombre_r'],
        "telefono_r": request.POST['telefono_r'],
        "parentesco_r": request.POST['parentesco_r'],
        "documento_r": request.POST['documento_r'],
        "usuario_u": request.POST['usuario_u'],
        "password_u": request.POST['password_u'],
        "idEntidad_salud": request.POST['idEntidad_salud'],
        "idCondicion": request.POST['idCondicion'],
        "idTransaccion": request.POST['idTransaccion'],
        "fecha": request.POST['fecha'],
    }
    requests.post('http://localhost:8000/ingreso/Usuarios/',data=json.dumps(datos))
    return redirect('../listaUsuarios/')

def cargarUsuario(request,id_Usuario):
    response=requests.get('http://localhost:8000/ingreso/Usuarios/'+id_Usuario)
    usuario=response.json()
    print(usuario)
    return render(request,"formActUsuarios.html",usuario)

def actualizarUsuario(request):
    codigo=request.POST['id_Usuario']
    datos={
        "nombres_u": request.POST['nombres_u'],
        "apellidos_u": request.POST['apellidos_u'],
        "documento_u": request.POST['documento_u'],
        "email_u": request.POST['email_u'],
        "telefono_u": request.POST['telefono_u'],
        "direccion_u": request.POST['direccion_u'],
        "nombre_r": request.POST['nombre_r'],
        "telefono_r": request.POST['telefono_r'],
        "parentesco_r": request.POST['parentesco_r'],
        "documento_r": request.POST['documento_r'],
        "usuario_u": request.POST['usuario_u'],
        "password_u": request.POST['password_u'],
        "idEntidad_salud_id": request.POST['idEntidad_salud_id'],
        "idCondicion_id": request.POST['idCondicion_id'],
        "idTransaccion_id": request.POST['idTransaccion_id'],
        "fecha": request.POST['fecha']
    }
    requests.put('http://localhost:8000/ingreso/Usuarios/'+codigo,data=json.dumps(datos))
    return redirect('../listaUsuarios/')

def eliminarUsuario(request,id_Usuario):
    response=requests.delete('http://localhost:8000/ingreso/Usuarios/'+id_Usuario)
    oficio=response.json()
    print(oficio)
    return redirect('../listaUsuarios/')