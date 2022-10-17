import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

def principal(request):
    return render(request, "index.html")

def listaAgendamientos(request):
    response=requests.get('http://localhost:8000/ingreso/Agendamientos')
    agendamientos=response.json()
    print(agendamientos)
    return render(request, "agendamientos.html",agendamientos)

def consultaAgendamiento(request):
    dato=request.POST['idAgendamiento']
    response=requests.get('http://localhost:8000/ingreso/Agendamientos/'+dato)
    agendamiento=response.json()
    print(agendamiento)
    return render(request,'agendamientos.html',agendamiento)

def formularioAgendamientos(request):
    return render(request, 'formAgendamientos.html')

def guardarAgendamiento(request):
    datos={
        "idAgendamiento": request.POST['idAgendamiento'],
        "horario_a": request.POST['horario_a'],
        "id_Usuario": request.POST['id_Usuario'],
        "idTransaccion": request.POST['idTransaccion'],
        "fecha": request.POST['fecha'],
    }
    requests.post('http://localhost:8000/ingreso/Agendamientos/',data=json.dumps(datos))
    return redirect('../listaAgendamientos/')

def cargarAgendamiento(request,idAgendamiento):
    response=requests.get('http://localhost:8000/ingreso/Agendamientos/'+idAgendamiento)
    agendamiento=response.json()
    print(agendamiento)
    return render(request,"formActAgendamientos.html",agendamiento)

def actualizarAgendamiento(request):
    codigo=request.POST['idAgendamiento']
    datos={
        "horario_a": request.POST['horario_a'],
        "id_Usuario_id": request.POST['id_Usuario_id'],
        "idTransaccion_id": request.POST['idTransaccion_id'],
        "fecha": request.POST['fecha']
    }
    requests.put('http://localhost:8000/ingreso/Agendamientos/'+codigo,data=json.dumps(datos))
    return redirect('../listaAgendamientos/')

def eliminarAgendamiento(request,idAgendamiento):
    response=requests.delete('http://localhost:8000/ingreso/Agendamientos/'+idAgendamiento)
    oficio=response.json()
    print(oficio)
    return redirect('../listaAgendamientos/')