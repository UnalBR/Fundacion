import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

def principal(request):
    return render(request, "index.html")

def listaEmpleados(request):
    response=requests.get('http://localhost:8000/ingreso/Empleados')
    empleados=response.json()
    print(empleados)
    return render(request, "empleados.html",empleados)

def consultaEmpleado(request):
    dato=request.POST['idEmpleados']
    response=requests.get('http://localhost:8000/ingreso/Empleados/'+dato)
    empleado=response.json()
    print(empleado)
    return render(request,'empleados.html',empleado)

def formularioEmpleados(request):
    return render(request, 'formEmpleados.html')

def guardarEmpleado(request):
    datos={
        "idEmpleados": request.POST['idEmpleados'],
        "nombres_e": request.POST['nombres_e'],
        "apellidos_e": request.POST['apellidos_e'],
        "documento_e": request.POST['documento_e'],
        "email_e": request.POST['email_e'],
        "telefono_e": request.POST['telefono_e'],
        "direccion_e": request.POST['direccion_e'],
        "idAgendamiento": request.POST['idAgendamiento'],
        "idCondicion": request.POST['idCondicion'],
        "idOficio":request.POST['idOficio'],
        "fecha": request.POST['fecha']
    }
    requests.post('http://localhost:8000/ingreso/Empleados/',data=json.dumps(datos))
    return redirect('../listaEmpleados/')

def cargarEmpleado(request,idEmpleados):
    response=requests.get('http://localhost:8000/ingreso/Empleados/'+idEmpleados)
    empleado=response.json()
    print(empleado)
    return render(request,"formActEmpleados.html",empleado)

def actualizarEmpleado(request):
    codigo=request.POST['idEmpleados']
    datos={
        "nombres_e": request.POST['nombres_e'],
        "apellidos_e": request.POST['apellidos_e'],
        "documento_e": request.POST['documento_e'],
        "email_e": request.POST['email_e'],
        "telefono_e": request.POST['telefono_e'],
        "direccion_e": request.POST['direccion_e'],
        "idAgendamiento_id": request.POST['idAgendamiento_id'],
        "idCondicion_id": request.POST['idCondicion_id'],
        "idOficio_id":request.POST['idOficio_id'],
        "fecha": request.POST['fecha']
    }
    requests.put('http://localhost:8000/ingreso/Empleados/'+codigo,data=json.dumps(datos))
    return redirect('../listaEmpleados/')

def eliminarEmpleado(request,idEmpleados):
    response=requests.delete('http://localhost:8000/ingreso/Empleados/'+idEmpleados)
    oficio=response.json()
    print(oficio)
    return redirect('../listaEmpleados/')