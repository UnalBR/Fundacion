import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

def principal(request):
    return render(request, "index.html")

def listaOficios(request):
    response=requests.get('http://localhost:8000/ingreso/Oficios')
    oficios=response.json()
    print(oficios)
    return render(request, "oficios.html",oficios)

def consultaOficio(request):
    dato=request.POST['idOficio']
    response=requests.get('http://localhost:8000/ingreso/Oficios/'+dato)
    oficio=response.json()
    print(oficio)
    return render(request,'oficios.html',oficio)

def formularioOficios(request):
    return render(request, 'formOficios.html')

def guardarOficio(request):
    datos={
        "idOficio": request.POST['idOficio'],
        "oficio_o": request.POST['oficio_o'],
        "indicativo_o": request.POST['indicativo_o'],
        "fecha": request.POST['fecha']
    }
    requests.post('http://localhost:8000/ingreso/Oficios/',data=json.dumps(datos))
    return redirect('../listaOficios/')

def cargarOficio(request,idOficio):
    response=requests.get('http://localhost:8000/ingreso/Oficios/'+idOficio)
    oficio=response.json()
    print(oficio)
    return render(request,"formActOficios.html",oficio)

def actualizarOficio(request):
    codigo=request.POST['idOficio']
    datos={
        "oficio_o": request.POST['oficio_o'],
        "indicativo_o": request.POST['indicativo_o'],
        "fecha": request.POST['fecha']
    }
    requests.put('http://localhost:8000/ingreso/Oficios/'+codigo,data=json.dumps(datos))
    return redirect('../listaOficios/')

def eliminarOficio(request,idOficio):
    response=requests.delete('http://localhost:8000/ingreso/Oficios/'+idOficio)
    oficio=response.json()
    print(oficio)
    return redirect('../listaOficios/')