from django.db import models


class Oficio(models.Model):
    idOficio=models.IntegerField(primary_key=True,auto_created=True)
    oficio_o=models.CharField(max_length=45,null=False)
    indicativo_o=models.CharField(max_length=45,null=False)
    
class Entidad_salud(models.Model):
    idEntidad_salud=models.IntegerField(primary_key=True,auto_created=True)
    empresa_es=models.CharField(max_length=45,null=False)
    valor_es=models.CharField(max_length=45,null=False)
    nit=models.CharField(max_length=45,null=False)
    sector_productivo=models.CharField(max_length=45,null=False)
    fecha_creacion=models.DateTimeField(null=False)
    ciudad=models.CharField(max_length=45)
    direccion=models.CharField(max_length=45)
    telefono=models.CharField(max_length=45)

    
class Condicion(models.Model):
    idCondicion=models.IntegerField(primary_key=True,auto_created=True)
    indicativo_c=models.CharField(max_length=45,null=False)
    condicion_c=models.CharField(max_length=45,null=False)   

class Transaccion(models.Model):
    idTransaccion=models.IntegerField(primary_key=True,auto_created=True)
    costo_t=models.CharField(max_length=45,null=False)
    Entidad_salud_idEntidad_salud=models.ForeignKey(Entidad_salud, on_delete=models.CASCADE)
    Oficio_idOficio=models.ForeignKey(Oficio, on_delete=models.CASCADE)
    fecha_t=models.CharField(max_length=45,null=False)
    descripcion_t=models.CharField(max_length=45,null=False)

class Usuarios(models.Model):
    id_Usuario=models.IntegerField(primary_key=True,auto_created=True)
    nombres_u=models.CharField(max_length=45,null=False)
    apellidos_u=models.CharField(max_length=45,null=False)
    documento_u=models.CharField(max_length=45,null=False,unique=True)
    email_u=models.EmailField(unique=True)
    telefono_u=models.CharField(max_length=45,null=False)
    direccion_u=models.CharField(max_length=45,null=False)
    nombre_r=models.CharField(max_length=45,null=False)
    telefono_r=models.CharField(max_length=45,null=False)
    parentesco_r=models.CharField(max_length=45,null=False)
    documento_r=models.CharField(max_length=45,null=False)
    usuario_u=models.CharField(max_length=45,null=False,unique=True)
    password_u=models.CharField(max_length=45,null=False)
    Entidad_salud_idEntidad_salud=models.ForeignKey(Entidad_salud, on_delete=models.CASCADE)
    Condicion_idCondicion=models.ForeignKey(Condicion,on_delete=models.CASCADE)
    Transaccion_idTransaccion=models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    

class Agendamiento(models.Model):
    idAgendamiento=models.IntegerField(primary_key=True,auto_created=True)
    horario_a=models.CharField(max_length=45,null=False)
    Usuarios_idUsuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    Transaccion_idTransaccion=models.ForeignKey(Transaccion, on_delete=models.CASCADE)

class Empleados(models.Model):
    idEmpleados=models.IntegerField(primary_key=True,auto_created=True)
    nombres_e=models.CharField(max_length=45,null=False)
    apellidos_e=models.CharField(max_length=45,null=False)
    documento_e=models.CharField(max_length=45,null=False,unique=True)
    email_e=models.EmailField(unique=True)
    telefono_e=models.CharField(max_length=45)
    direccion_e=models.CharField(max_length=45)
    tFecha_creacion=models.CharField(max_length=45,null=False)
    Agendamiento_ideAgendamiento=models.ForeignKey(Agendamiento, on_delete=models.CASCADE)
    Condicion_idCondicion=models.ForeignKey(Condicion,on_delete=models.CASCADE)
    Oficio_idOficio=models.ForeignKey(Oficio, on_delete=models.CASCADE)



