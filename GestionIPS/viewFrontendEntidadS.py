import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

def principal(request):
    return render(request, "index.html")

def listaEntidades(request):
    response=requests.get('http://localhost:8000/ingreso/Entidades_salud')
    entidades=response.json()
    print(entidades)
    return render(request, "entidades_salud.html",entidades)

def consultaEntidad(request):
    dato=request.POST['idEntidad_salud']
    response=requests.get('http://localhost:8000/ingreso/Entidades_salud/'+dato)
    entidad=response.json()
    print(entidad)
    return render(request,'entidades_salud.html',entidad)

def formularioEntidades(request):
    return render(request, 'formEntidades_salud.html')

def guardarEntidad(request):
    datos={
        "idEntidad_salud": request.POST['idEntidad_salud'],
        "empresa_es": request.POST['empresa_es'],
        "valor_es": request.POST['valor_es'],
        "nit": request.POST['nit'],
        "sector_productivo": request.POST['sector_productivo'],
        "ciudad": request.POST['ciudad'],
        "direccion": request.POST['direccion'],
        "telefono": request.POST['telefono'],
        "fecha": request.POST['fecha'],
    }
    requests.post('http://localhost:8000/ingreso/Entidades_salud/',data=json.dumps(datos))
    return redirect('../listaEntidades/')

def cargarEntidad(request,idEntidad_salud):
    response=requests.get('http://localhost:8000/ingreso/Entidades_salud/'+idEntidad_salud)
    entidad=response.json()
    print(entidad)
    return render(request,"formActEntidades_salud.html",entidad)

def actualizarEntidad(request):
    codigo=request.POST['idEntidad_salud']
    datos={
        "empresa_es": request.POST['empresa_es'],
        "valor_es": request.POST['valor_es'],
        "nit": request.POST['nit'],
        "sector_productivo": request.POST['sector_productivo'],
        "ciudad": request.POST['ciudad'],
        "direccion": request.POST['direccion'],
        "telefono": request.POST['telefono'],
        "fecha": request.POST['fecha']
    }
    requests.put('http://localhost:8000/ingreso/Entidades_salud/'+codigo,data=json.dumps(datos))
    return redirect('../listaEntidades/')

def eliminarEntidad(request,idEntidad_salud):
    response=requests.delete('http://localhost:8000/ingreso/Entidades_salud/'+idEntidad_salud)
    oficio=response.json()
    print(oficio)
    return redirect('../listaEntidades/')