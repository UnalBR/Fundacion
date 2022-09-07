from django.contrib import admin

from GestionIPS.models import Empleados
from GestionIPS.models import Condicion
from GestionIPS.models import Usuarios
from GestionIPS.models import Agendamiento
from GestionIPS.models import Oficio
from GestionIPS.models import Transaccion
from GestionIPS.models import Entidad_salud

admin.site.register(Empleados)
admin.site.register(Condicion)
admin.site.register(Usuarios)
admin.site.register(Agendamiento)
admin.site.register(Oficio)
admin.site.register(Transaccion)
admin.site.register(Entidad_salud)
# Register your models here.
