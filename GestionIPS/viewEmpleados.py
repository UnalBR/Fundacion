import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from GestionIPS.models import Oficio
from GestionIPS.models import Condicion
from GestionIPS.models import Agendamiento
from GestionIPS.models import Empleados
from django.http import JsonResponse

class EmpleadosView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get ( self , request ,emple=""):
        if len(emple)>0:
            empleadoNu=list(Empleados.objects.filter (idEmpleados=emple) .values())
            if len(empleadoNu)>0:
                datos={'Empleados':empleadoNu, 'Mensaje':'Resultado de la Busqueda.'}
            else:
                datos={'Error':"No se encontro el Empleado"}
        else:
            empleadosTo=list(Empleados.objects.values())
            if len(empleadosTo)>0: 
                datos={'Empleados':empleadosTo}
            else:
                datos={'Error':"No se emcontraton Empleados"}
        return JsonResponse ( datos )
    
    def post(self,request):
        data=json.loads(request.body)
        try:
            empleadosTe=Empleados.objects.create(nombres_e=data['nombres_e'],apellidos_e=data['apellidos_e'],
                              documento_e=data['documento_e'],email_e=data['email_e'],telefono_e=data['telefono_e'],
                              direccion_e=data['direccion_e'],
                              idAgendamiento_id=Agendamiento.objects.get(idAgendamiento_id=data['idAgendamiento_id']),
                              idCondicion_id=Condicion.objects.get(idCondicion_id=data['idCondicion_id']),
                              idOficio_id=Oficio.objects.get(idOficio_id=data['idOficio_id']))
            empleadosTe.save()
            datos={'mensaje7.2':'Empleado resgistrado esxitosamente'}
            
        except Agendamiento.DoesNotExist:
            datos={'mensaje4.2':'El Agendamiento no existe'}
        except Condicion.DoesNotExist:
            datos={'mensaje4.2':'La Condicion no existe'}
        except Oficio.DoesNotExist:
            datos={'mensaje4.2':'El Oficio no existe'}
        
        return JsonResponse(datos)
    
    def put(self,request,emple):
        data=json.loads(request.body)
        empleadosMo=list(Empleados.objects.filter(idEmpleados=emple).values())
        if len(empleadosMo)>0:
            emp=Empleados.objects.get(idEmpleados=emple)
            emp.nombres_e=data['nombres_e']
            emp.apellidos_e=data['apellidos_e']
            emp.documento_e=data['documento_e']
            emp.email_e=data['email_e']
            emp.telefono_e=data['telefono_e']
            emp.direccion_e=data['direccion_e']
            emp.idAgendamiento=Agendamiento.objects.get(idAgendamiento_id=data['idAgendamiento_id'])
            emp.idCondicion=Condicion.objects.get(idCondicion_id=data['idCondicion_id'])
            emp.idOficio=Oficio.objects.get(idOficio_id=data['idOficio_id'])
            emp.save()
            mensaje={"mensaje7.3":"Empleado Actualizado exitosamente."}
        else:
            mensaje={"mensaje7.4":"No se encontro el Empleado."}
        
        return JsonResponse(mensaje)
    
    def delete(self,request,emple):
        empleadosDe=list(Empleados.objects.filter(idEmpleados=emple).values())
        if len(empleadosDe)>0:
            Empleados.objects.filter(idEmpleados=emple).delete()
            mensaje={"mensaje7.5":"Empleado Eliminado exitosamente."}
        else:
            mensaje={"mensaje7.6":"No se encontro el Empleado."}
            
        return JsonResponse(mensaje)
