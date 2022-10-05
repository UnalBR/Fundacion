import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

def principal(request):
    return render(request, "index.html")

def listaTransacciones(request):
    response=requests.get('http://localhost:8000/ingreso/Transacciones')
    transacciones=response.json()
    print(transacciones)
    return render(request, "transacciones.html",transacciones)

def consultaTransaccion(request):
    dato=request.POST['idTransaccion']
    response=requests.get('http://localhost:8000/ingreso/Transacciones/'+dato)
    transaccion=response.json()
    print(transaccion)
    return render(request,'transacciones.html',transaccion)

def formularioTransacciones(request):
    return render(request, 'formTransacciones.html')

def guardarTransaccion(request):
    datos={
        "idTransaccion":request.POST['idTransaccion'],
        "costo_t": request.POST['costo_t'],
        "idEntidad_salud": request.POST['idEntidad_salud'],
        "idOficio": request.POST['idOficio'],
        "descripcion_t": request.POST['descripcion_t'],
        "fecha": request.POST['fecha'],
    }
    requests.post('http://localhost:8000/ingreso/Transacciones/',data=json.dumps(datos))
    return redirect('../listaTransacciones/')

def cargarTransaccion(request,idTransaccion):
    response=requests.get('http://localhost:8000/ingreso/Transacciones/'+idTransaccion)
    transaccion=response.json()
    print(transaccion)
    return render(request,"formActTransacciones.html",transaccion)

def actualizarTransaccion(request):
    codigo=request.POST['idTransaccion']
    datos={
        "costo_t": request.POST['costo_t'],
        "idEntidad_salud_id": request.POST['idEntidad_salud_id'],
        "idOficio_id": request.POST['idOficio_id'],
        "descripcion_t": request.POST['descripcion_t'],
        "fecha": request.POST['fecha']
    }
    requests.put('http://localhost:8000/ingreso/Transacciones/'+codigo,data=json.dumps(datos))
    return redirect('../listaTransacciones/')

def eliminarTransaccion(request,idTransaccion):
    response=requests.delete('http://localhost:8000/ingreso/Transacciones/'+idTransaccion)
    oficio=response.json()
    print(oficio)
    return redirect('../listaTransacciones/')