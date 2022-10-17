import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from GestionIPS.models import Oficio
from GestionIPS.models import Entidad_salud
from GestionIPS.models import Condicion
from GestionIPS.models import Transaccion
from GestionIPS.models import Usuarios
from GestionIPS.models import Agendamiento
from GestionIPS.models import Empleados
from django.http import JsonResponse

class AgendamientoView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get ( self , request , IDagendamiento=""):
        if len(IDagendamiento)>0:
            agendamientoNu=list(Agendamiento.objects.filter (idAgendamiento = IDagendamiento) .values())
            if len(agendamientoNu)>0:
                datos={'Agendamiento':agendamientoNu}
            else:
                datos={'mensaje6':"No se encontro el Oficio"}
        else:
            agendamientos=list(Agendamiento.objects.values())
            if len(agendamientos)>0: 
                datos={'Agendamientos':agendamientos}
            else:
                datos={'mensaje6.1':"No se emcontraton Oficios"}
        return JsonResponse ( datos )
    
    def post(self,request):
        data=json.loads(request.body)
        try:
            agendamientoTe=Agendamiento.objects.create(horario_a=data['horario_a'],
                                 id_Usuario=Usuarios.objects.get (id_Usuario=data['id_Usuario'] ),
                                 idTransaccion=Transaccion.objects.get ( idTransaccion=data['idTransaccion'] ))
            agendamientoTe.save()
            datos={'mensaje6.2':'Libro resgistrado esxitosamente'}
        
        except Usuarios.DoesNotExist:
            datos={'mensaje4.2':'El Usuario no existe'}
        except Transaccion.DoesNotExist:
            datos={'mensaje4.2':'La Transaccion no existe'}
            
        return JsonResponse(datos)
    
    def put(self,request,IDagendamiento):
        data=json.loads(request.body)
        agendamientoMo=list(Agendamiento.objects.filter(idAgendamiento = IDagendamiento).values())
        if len(agendamientoMo)>0:
            agen=Agendamiento.objects.get(idAgendamiento = IDagendamiento)
            agen.horario_a=data['horario_a']
            agen.id_Usuario=Usuarios.objects.get (id_Usuario=data['id_Usuario'] )
            agen.idTransaccion=Transaccion.objects.get ( idTransaccion=data['idTransaccion'] )
            agen.save()
            mensaje={"mensaje6.3":"Libro Actualizado exitosamente."}
        else:
            mensaje={"mensaje6.4":"No se encontro el Libro."}
        
        return JsonResponse(mensaje)
    
    def delete(self,request,IDagendamiento):
        agendamientoDe=list(Agendamiento.objects.filter(idAgendamiento = IDagendamiento).values())
        if len(agendamientoDe)>0:
            Agendamiento.objects.filter(idAgendamiento = IDagendamiento).delete()
            mensaje={"mensaje6.5":"Libro Eliminado exitosamente."}
        else:
            mensaje={"mensaje6.6":"No se encontro el Libro."}
            
        return JsonResponse(mensaje)