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

class CondicionView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get ( self , request , IDCondicion=""):
        if len(IDCondicion)>0:
            condicionNu=list(Condicion.objects.filter (idCondicion = IDCondicion) .values())
            if len(condicionNu)>0:
                datos={'Condicion':condicionNu}
            else:
                datos={'mensaje3':"No se encontro el Oficio"}
        else:
            condiciones=list(Condicion.objects.values())
            if len(condiciones)>0: 
                datos={'Condiciones':condiciones}
            else:
                datos={'mensaje3.1':"No se emcontraton Oficios"}
        return JsonResponse ( datos )
    
    def post(self,request):
        data=json.loads(request.body)
        condicionTe=Condicion(indicativo_c=data['indicativo_c'],condicion_c=data['condicion_c'])
        condicionTe.save()
        datos={'mensaje3.2':'Libro resgistrado esxitosamente'}
        return JsonResponse(datos)
    
    def put(self,request,IDCondicion):
        data=json.loads(request.body)
        condicionMo=list(Condicion.objects.filter(idCondicion = IDCondicion).values())
        if len(condicionMo)>0:
            con=Condicion.objects.get(idCondicion = IDCondicion)
            con.indicativo_c=data['indicativo_c']
            con.condicion_c=data['condicion_c']
            con.save()
            mensaje={"mensaje3.3":"Libro Actualizado exitosamente."}
        else:
            mensaje={"mensaje3.4":"No se encontro el Libro."}
        return JsonResponse(mensaje)
    
    def delete(self,request,IDCondicion=""):
        condicionDe=list(Condicion.objects.filter(idCondicion = IDCondicion).values())
        if len(condicionDe)>0:
            Condicion.objects.filter(idCondicion = IDCondicion).delete()
            mensaje={"mensaje3.5":"Libro Eliminado exitosamente."}
        else:
            mensaje={"mensaje3.6":"No se encontro el Libro."}
        return JsonResponse(mensaje)

    def new_method(self, request):
        data=json.loads(request.body)