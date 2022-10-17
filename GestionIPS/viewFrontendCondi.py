import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

def principal(request):
    return render(request, "index.html")

def listaCondiciones(request):
    response=requests.get('http://localhost:8000/ingreso/Condiciones')
    condiciones=response.json()
    print(condiciones)
    return render(request, "condiciones.html",condiciones)

def consultaCondicion(request):
    dato=request.POST['idCondicion']
    response=requests.get('http://localhost:8000/ingreso/Condiciones/'+dato)
    condicion=response.json()
    print(condicion)
    return render(request,'condiciones.html',condicion)

def formularioCondiciones(request):
    return render(request, 'formCondiciones.html')

def guardarCondicion(request):
    datos={
        "idCondicion": request.POST['idCondicion'],
        "indicativo_c": request.POST['indicativo_c'],
        "condicion_c": request.POST['condicion_c'],
        "fecha": request.POST['fecha']
    
    }
    requests.post('http://localhost:8000/ingreso/Condiciones/',data=json.dumps(datos))
    return redirect('../listaCondiciones/')

def cargarCondicion(request,idCondicion):
    response=requests.get('http://localhost:8000/ingreso/Condiciones/'+idCondicion)
    condicion=response.json()
    print(condicion)
    return render(request,"formActCondiciones.html",condicion)

def actualizarCondicion(request):
    codigo=request.POST['idCondicion']
    datos={
        "indicativo_c": request.POST['indicativo_c'],
        "condicion_c": request.POST['condicion_c'],
        "fecha": request.POST['fecha']
    }
    requests.put('http://localhost:8000/ingreso/Condiciones/'+codigo,data=json.dumps(datos))
    return redirect('../listaCondiciones/')

def eliminarCondicion(request,idCondicion):
    response=requests.delete('http://localhost:8000/ingreso/Condiciones/'+idCondicion)
    oficio=response.json()
    print(oficio)
    return redirect('../listaCondiciones/')