import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from GestionIPS.models import Oficio
from django.http import JsonResponse

class OficioView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,ofic="") :
        if len(ofic)>0:
            oficioNu=list(Oficio.objects.filter (idOficio=ofic).values())
            if len(oficioNu)>0:
                datos={'Oficios':oficioNu, 'Mensaje':'Resultado de la Busqueda.'}
            else:
                datos={'Error':"No se encontro el Oficio"}
        else:
            oficios=list(Oficio.objects.values())
            if len(oficios)>0: 
                datos={'Oficios':oficios}
            else:
                datos={'Error':"No se emcontraton Oficios"}
        return JsonResponse ( datos )
    
    def post(self,request):
        data=json.loads(request.body)
        oficioTe=Oficio.objects.create(oficio_o=data['oficio_o'],indicativo_o=data['indicativo_o'])
        oficioTe.save()
        datos={'mensaje1.2':'Oficio resgistrado esxitosamente'}
        return JsonResponse(datos)
    
    def put(self,request,ofic):
        data=json.loads(request.body)
        oficioMo=list(Oficio.objects.filter(idOficio=ofic).values())
        if len(oficioMo)>0:
            ofi=Oficio.objects.get(idOficio=ofic)
            ofi.oficio_o=data['oficio_o']
            ofi.indicativo_o=data['indicativo_o']
            ofi.save()
            mensaje={"mensaje1.3":"Oficio Actualizado exitosamente."}
        else:
            mensaje={"mensaje1.4":"No se encontro el Oficio."}
        return JsonResponse(mensaje)
    
    def delete(self,request,ofic):
        oficioDe=list(Oficio.objects.filter(idOficio=ofic).values())
        if len(oficioDe)>0:
            Oficio.objects.filter(idOficio=ofic).delete()
            mensaje={"mensaje1.5":"Oficio Eliminado exitosamente."}
        else:
            mensaje={"mensaje1.6":"No se encontro el Ofico."}
        return JsonResponse(mensaje)