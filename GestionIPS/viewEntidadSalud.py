import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from GestionIPS.models import Entidad_salud
from django.http import JsonResponse

class Entidad_saludView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get ( self , request , IDentidad=""):
        if len(IDentidad)>0:
            entidadSalud=list(Entidad_salud.objects.filter (idEntidad_salud = IDentidad) .values())
            if len(entidadSalud)>0:
                datos={'Entidades':entidadSalud, 'Mensaje':'Resultado de la Busqueda.'}
            else:
                datos={'Entidades':"No se encontro la Entidad"}
        else:
            entidades=list(Entidad_salud.objects.values())
            if len(entidades)>0: 
                datos={'Entidades':entidades}
            else:
                datos={'Entidades':"No se emcontraton Entidades"}
        return JsonResponse ( datos )
    
    def post(self,request):
        data=json.loads(request.body)
        entidadTe=Entidad_salud.objects.create(empresa_es=data['empresa_es'],
                                valor_es=data['valor_es'],nit=data['nit'],sector_productivo=data['sector_productivo']
                                ,ciudad=data['ciudad'],direccion=data['direccion'],telefono=data['telefono'])
        entidadTe.save()
        datos={'mensaje2.2':'Entidad resgistrada esxitosamente'}
        return JsonResponse(datos)
    
    def put(self,request,IDentidad):
        data=json.loads(request.body)
        entidadMo=list(Entidad_salud.objects.filter(idEntidad_salud = IDentidad).values())
        if len(entidadMo)>0:
            ent=Entidad_salud.objects.get(idEntidad_salud = IDentidad)
            ent.empresa_es=data['empresa_es']
            ent.valor_es=data['valor_es']
            ent.nit=data['nit']
            ent.sector_productivo=data['sector_productivo']
            ent.ciudad=data['ciudad']
            ent.direccion=data['direccion']
            ent.telefono=data['telefono']
            ent.save()
            mensaje={"mensaje2.3":"Entidad Actualizada exitosamente."}
        else:
            mensaje={"mensaje2.4":"No se encontro la Entidad."}
        
        return JsonResponse(mensaje)
    
    def delete(self,request,IDentidad):
        entidadDe=list(Entidad_salud.objects.filter(idEntidad_salud = IDentidad).values())
        if len(entidadDe)>0:
            Entidad_salud.objects.filter(idEntidad_salud = IDentidad).delete()
            mensaje={"mensaje2.5":"Entidad Eliminada exitosamente."}
        else:
            mensaje={"mensaje2.6":"No se encontro la Entidad."}
        
        return JsonResponse(mensaje)