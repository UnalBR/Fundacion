import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from GestionIPS.models import Condicion
from django.http import JsonResponse

class CondicionView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get ( self , request ,condic=""):
        if len(condic)>0:
            condicionNu=list(Condicion.objects.filter (idCondicion=condic) .values())
            if len(condicionNu)>0:
                datos={'Condiciones':condicionNu, 'Mensaje':'Resultado de la Busqueda.'}
            else:
                datos={'Error':"No se encontro la Condicio"}
        else:
            condiciones=list(Condicion.objects.values())
            if len(condiciones)>0: 
                datos={'Condiciones':condiciones}
            else:
                datos={'Error':"No se emcontraton Condciciones"}
        return JsonResponse ( datos )
    
    def post(self,request):
        data=json.loads(request.body)
        condicionTe=Condicion.objects.create(indicativo_c=data['indicativo_c'],condicion_c=data['condicion_c'])
        condicionTe.save()
        datos={'mensaje3.2':'Condicion resgistrada esxitosamente'}
        return JsonResponse(datos)
    
    def put(self,request,condic):
        data=json.loads(request.body)
        condicionMo=list(Condicion.objects.filter(idCondicion=condic).values())
        if len(condicionMo)>0:
            con=Condicion.objects.get(idCondicion=condic)
            con.indicativo_c=data['indicativo_c']
            con.condicion_c=data['condicion_c']
            con.save()
            mensaje={"mensaje3.3":"Condicion Actualizada exitosamente."}
        else:
            mensaje={"mensaje3.4":"No se encontro la Condicion."}
        return JsonResponse(mensaje)
    
    def delete(self,request,condic=""):
        condicionDe=list(Condicion.objects.filter(idCondicion=condic).values())
        if len(condicionDe)>0:
            Condicion.objects.filter(idCondicion=condic).delete()
            mensaje={"mensaje3.5":"Condicion Eliminada exitosamente."}
        else:
            mensaje={"mensaje3.6":"No se encontro la Condicion."}
        return JsonResponse(mensaje)

    def new_method(self, request):
        data=json.loads(request.body)