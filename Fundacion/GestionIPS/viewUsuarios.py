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

class UsuariosView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get ( self , request , IDusuario=""):
        if len(IDusuario)>0:
            usuarioNu=list(Usuarios.objects.filter (id_Usuario = IDusuario) .values())
            if len(usuarioNu)>0:
                datos={'Usuario':usuarioNu}
            else:
                datos={'mensaje5':"No se encontro el Oficio"}
        else:
            usuariosTo=list(Usuarios.objects.values())
            if len(usuariosTo)>0: 
                datos={'Usuarios':usuariosTo}
            else:
                datos={'mensaje5.1':"No se emcontraton Oficios"}
        return JsonResponse ( datos )
    
    def post(self,request):
        data=json.loads(request.body)
        try:
            
            usuariosTe=Usuarios.objects.create(nombres_u=data['nombres_u'],apellidos_u=data['apellidos_u'],
                             documento_u=data['documento_u'],email_u=data['email_u'],telefono_u=data['telefono_u'],
                             direccion_u=data['direccion_u'],nombre_r=data['nombre_r'],telefono_r=data['telefono_r'],
                             parentesco_r=data['parentesco_r'],documento_r=data['documento_r'],usuario_u=data['usuario_u'],
                             password_u=data['password_u'],
                             idEntidad_salud= Entidad_salud.objects.get ( idEntidad_salud = data [ " IDentidad " ] ),
                             idCondicion=Condicion.objects.get (idCondicion=data['idCondicion'] ),
                             idTransaccion=Transaccion.objects.get ( idTransaccion=data['idTransaccion'] ))
            usuariosTe.save()
            datos={'mensaje5.2':'Libro resgistrado esxitosamente'}
            
        except Entidad_salud.DoesNotExist:
            datos={'mensaje4.2':'La Entidad no existe'}
        except Condicion.DoesNotExist:
            datos={'mensaje4.2':'La Condicion no existe'}
        except Transaccion.DoesNotExist:
            datos={'mensaje4.2':'La Transaccion no existe'}
        
        return JsonResponse(datos)
    
    def put(self,request,IDusuario):
        data=json.loads(request.body)
        usuariosMo=list(Usuarios.objects.filter(id_Usuario = IDusuario).values())
        if len(usuariosMo)>0:
            usu=Usuarios.objects.get(id_Usuario = IDusuario)
            usu.nombres_u=data['nombres_u']
            usu.apellidos_u=data['apellidos_u']
            usu.documento_u=data['documento_u']
            usu.email_u=data['email_u']
            usu.telefono_u=data['telefono_u']
            usu.direccion_u=data['direccion_u']
            usu.nombre_r=data['nombre_r']
            usu.telefono_r=data['telefono_r']
            usu.parentesco_r=data['parentesco_r']
            usu.documento_r=data['documento_r']
            usu.usuario_u=data['usuario_u']
            usu.password_u=data['password_u']
            usu.Entidad_salud_idEntidad_salud=data['Entidad_salud_idEntidad_salud']
            usu.Condicion_idCondicion=data['Condicion_idCondicion']
            usu.Transaccion_idTransaccion=data['ransaccion_idTransaccion']
            usu.save()
            mensaje={"mensaje5.3":"Libro Actualizado exitosamente."}
        else:
            mensaje={"mensaje5.4":"No se encontro el Libro."}
        
        return JsonResponse(mensaje)
    
    def delete(self,request, IDusuario):
        usuariosDe=list(Usuarios.objects.filter(id_Usuario = IDusuario).values())
        if len(usuariosDe)>0:
            Usuarios.objects.filter(id_Usuario = IDusuario).delete()
            mensaje={"mensaje5.5":"Libro Eliminado exitosamente."}
        else:
            mensaje={"mensaje5.6":"No se encontro el Libro."}
            
        return JsonResponse(mensaje)