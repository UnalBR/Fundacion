from ast import Return
import datetime
from re import template
from django.http import HttpResponse
import datetime
from django.template import Template, Context # ,loader
from django.template.loader import get_template
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido
        pass
class Doctor(object):
    def __init__(self, Nombre, CC):
        self.nombre=Nombre
        self.CC=CC
        pass

def doctorinfo(request):
    DBName="Doctores"
    infoDoctor=Doctor("Doc Pepe el bueno","123456XXX")
    documento={"Base_Datos":DBName,"Namedoc":infoDoctor.nombre, "Cedula":infoDoctor.CC}
    return render(request, "Plantilladocinfo.html", documento)

def saludo(request):
    
    nombre="CICLO 3 GRUPO 6"
    Tripulante="Mision TIC 2022"
    personacreada=Persona("Camilo", "Falla")
    Tiempo=datetime.datetime.now()
    TareasJira=["Historias de usuario","Creacion y desarrollo del git","Creacion de backend con django","Diseño Base de Datos",
                "Scrum 1","Diseno de pagina","Caso de uso","Creacion de MOCKUP"]
    #doc_externo=open("C:/Users/camil/OneDrive/Documentos/MINTIC/django/pruebasIni/pruebasIni/plantillas/Miplantilla.html")
    
    #plantilla=Template(doc_externo.read())
    #doc_externo.close()
    
    #doc_externo=loader.get_template('Miplantilla.html')
    doc_externo=get_template("Miplantilla.html")
    
   # ctx=Context({"nombre_grupo":nombre,"Tipo_Grupo":Tripulante,"tiempo_ya":Tiempo,"CreadorNom":personacreada.nombre,
                 #"CreadorApell":personacreada.apellido, "Lista_de_asignaciones":TareasJira})
    documento=doc_externo.render({"nombre_grupo":nombre,"Tipo_Grupo":Tripulante,"tiempo_ya":Tiempo,"CreadorNom":personacreada.nombre,"CreadorApell":personacreada.apellido, "Lista_de_asignaciones":TareasJira})
    
    return HttpResponse(documento)

def despedida(request):
    
    return HttpResponse("Chao amigos curso Mintic")

def damefecha(request):
    
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    Esta es la fecha y hora actualizada %s
    </h1>
    </body>
    </html>""" %fecha_actual
    return HttpResponse(documento)

def calculaedad(request, edad, agno):
    periodo=agno-2022
    edadfutura=edad+periodo
    documento="""<html>
    <body>
    <h1>
    Mi edad será %s en el año %s
    </h1>
    </body>
    </html>""" %(edadfutura, agno)
    return HttpResponse(documento)