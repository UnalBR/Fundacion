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

class EmpleadosView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get ( self , request , IDempleados=""):
        if len(IDempleados)>0:
            empleadoNu=list(Empleados.objects.filter (idEmpleados = IDempleados) .values())
            if len(empleadoNu)>0:
                datos={'Empleado':empleadoNu}
            else:
                datos={'mensaje7':"No se encontro el Oficio"}
        else:
            empleadosTo=list(Empleados.objects.values())
            if len(empleadosTo)>0: 
                datos={'Empleados':empleadosTo}
            else:
                datos={'mensaje7.1':"No se emcontraton Oficios"}
        return JsonResponse ( datos )
    
    def post(self,request):
        data=json.loads(request.body)
        try:
            empleadosTe=Empleados.objects.create(nombres_e=data['nombres_e'],apellidos_e=data['apellidos_e'],
                              documento_e=data['documento_e'],email_e=data['email_e'],telefono_e=data['telefono_e'],
                              direccion_e=data['direccion_e'],
                              ideAgendamiento=Agendamiento.objects.get ( idAgendamiento=data['idAgendamiento'] ),
                              idCondicion=Condicion.objects.get (idCondicion=data['idCondicion'] ),
                              idOficio=Oficio.objects.get ( idOficio=data['idOficio'] ))
            empleadosTe.save()
            datos={'mensaje7.2':'Libro resgistrado esxitosamente'}
            
        except Agendamiento.DoesNotExist:
            datos={'mensaje4.2':'El Agendamiento no existe'}
        except Condicion.DoesNotExist:
            datos={'mensaje4.2':'La Condicion no existe'}
        except Oficio.DoesNotExist:
            datos={'mensaje4.2':'El Oficio no existe'}
        
        return JsonResponse(datos)
    
    def put(self,request,IDempleados):
        data=json.loads(request.body)
        empleadosMo=list(Empleados.objects.filter(idEmpleados = IDempleados).values())
        if len(empleadosMo)>0:
            emp=Empleados.objects.get(idEmpleados = IDempleados)
            emp.nombres_e=data['nombres_e']
            emp.apellidos_e=data['apellidos_e']
            emp.documento_e=data['documento_e']
            emp.email_e=data['email_e']
            emp.telefono_e=data['telefono_e']
            emp.direccion_e=data['direccion_e']
            emp.idAgendamiento=Agendamiento.objects.get ( idAgendamiento=data['idAgendamiento'] )
            emp.idCondicion=Condicion.objects.get (idCondicion=data['idCondicion'] )
            emp.idOficio=Oficio.objects.get ( idOficio=data['idOficio'] )
            emp.save()
            mensaje={"mensaje7.3":"Libro Actualizado exitosamente."}
        else:
            mensaje={"mensaje7.4":"No se encontro el Libro."}
        
        return JsonResponse(mensaje)
    
    def delete(self,request,IDempleados):
        empleadosDe=list(Empleados.objects.filter(idEmpleados = IDempleados).values())
        if len(empleadosDe)>0:
            Empleados.objects.filter(idEmpleados = IDempleados).delete()
            mensaje={"mensaje7.5":"Libro Eliminado exitosamente."}
        else:
            mensaje={"mensaje7.6":"No se encontro el Libro."}
            
        return JsonResponse(mensaje)
