import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from GestionIPS.models import Oficio
from GestionIPS.models import Entidad_salud
from GestionIPS.models import Transaccion
from django.http import JsonResponse


class TransaccionView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get (self,request,Transac=""):
        if len(Transac)>0:
            transaccionNu=list(Transaccion.objects.filter(idTransaccion=Transac).values())
            if len(transaccionNu)>0:
                datos={'Transacciones':transaccionNu, 'Mensaje':'Resultado de la Busqueda.'}
            else:
                datos={'Error':"No se encontro la Transaccion"}
        else:
            transacciones=list(Transaccion.objects.values())
            if len(transacciones)>0: 
                datos={'Transacciones':transacciones}
            else:
                datos={'Error':"No se emcontraton Transacciones"}
        return JsonResponse ( datos )
    
    def post(self,request):
        data=json.loads(request.body)
    
        try:
            transaccionTe=Transaccion.objects.create(costo_t=data['costo_t'],idEntidad_salud=Entidad_salud.objects.get(idEntidad_salud=data['idEntidad_salud']),
                                                     idOficio=Oficio.objects.get(idOficio=data['idOficio']),descripcion_t=data['descripcion_t'])
            transaccionTe.save()
            datos={'mensaje4.2':'Transaccion resgistrada esxitosamente'}
        
        except Entidad_salud.DoesNotExist:
            datos={'mensaje4.2':'La Entidad no existe'}
        except Oficio.DoesNotExist:
            datos={'mensaje4.2':'El Oficio no existe'}
            
        return JsonResponse(datos)

    
    
    def put(self,request,Transac):
        data=json.loads(request.body)
        transaccionMo=list(Transaccion.objects.filter(idTransaccion=Transac).values())
        if len(transaccionMo)>0:
            tra=Transaccion.objects.get(idTransaccion=Transac)
            tra.costo_t=data['costo_t']
            tra.idEntidad_salud=Entidad_salud.objects.get(idEntidad_salud=data['idEntidad_salud'])
            tra.idOficio=Oficio.objects.get(idOficio=data['idOficio'])
            tra.descripcion_t=data['descripcion_t']
            tra.save()
            mensaje={"mensaje4.3":"Transaccion Actualizado exitosamente."}
        else:
            mensaje={"mensaje4.4":"No se encontro la Transaccion."}
        
        return JsonResponse(mensaje)
    
    def delete(self,request,Transac):
        transaccionDe=list(Transaccion.objects.filter(idTransaccion=Transac).values())
        if len(transaccionDe)>0:
            Transaccion.objects.filter(idTransaccion=Transac).delete()
            mensaje={"mensaje4.5":"Transaccion Eliminada exitosamente."}
        else:
            mensaje={"mensaje4.6":"No se encontro la Transaccion."}
            
        return JsonResponse(mensaje)