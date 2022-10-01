#creacion modelos de tablas//2
from django.db import models


class Oficio(models.Model):
    idOficio=models.AutoField(primary_key=True)
    oficio_o=models.CharField(max_length=45,null=False)
    indicativo_o=models.CharField(max_length=45,null=False)
    fecha=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.idOficio
    
class Entidad_salud(models.Model):
    idEntidad_salud=models.AutoField(primary_key=True)
    empresa_es=models.CharField(max_length=45,null=False)
    valor_es=models.CharField(max_length=45,null=False)
    nit=models.CharField(max_length=45,null=False)
    sector_productivo=models.CharField(max_length=45,null=False)
    #fecha_creacion=models.DateTimeField(null=False)
    ciudad=models.CharField(max_length=45)
    direccion=models.CharField(max_length=45)
    telefono=models.CharField(max_length=45)
    fecha=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.idEntidad_salud

    
class Condicion(models.Model):
    idCondicion=models.AutoField(primary_key=True)
    indicativo_c=models.CharField(max_length=45,null=False)
    condicion_c=models.CharField(max_length=45,null=False)
    fecha=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.idCondicion 

class Transaccion(models.Model):
    idTransaccion=models.AutoField(primary_key=True)
    costo_t=models.CharField(max_length=45,null=False)
    idEntidad_salud=models.ForeignKey(Entidad_salud, on_delete=models.CASCADE)#
    idOficio=models.ForeignKey(Oficio, on_delete=models.CASCADE)#
    #fecha_t=models.CharField(max_length=45,null=False)
    descripcion_t=models.CharField(max_length=45,null=False)
    fecha=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.idTransaccion

class Usuarios(models.Model):
    id_Usuario=models.AutoField(primary_key=True)
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
    idEntidad_salud=models.ForeignKey(Entidad_salud, on_delete=models.CASCADE)#
    idCondicion=models.ForeignKey(Condicion,on_delete=models.CASCADE)#
    idTransaccion=models.ForeignKey(Transaccion, on_delete=models.CASCADE)#
    fecha=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.id_Usuario
    

class Agendamiento(models.Model):
    idAgendamiento=models.AutoField(primary_key=True)
    horario_a=models.CharField(max_length=45,null=False)
    id_Usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)#
    idTransaccion=models.ForeignKey(Transaccion, on_delete=models.CASCADE)#
    fecha=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.idAgendamiento

class Empleados(models.Model):
    idEmpleados=models.AutoField(primary_key=True)
    nombres_e=models.CharField(max_length=45,null=False)
    apellidos_e=models.CharField(max_length=45,null=False)
    documento_e=models.CharField(max_length=45,null=False,unique=True)
    email_e=models.EmailField(unique=True)
    telefono_e=models.CharField(max_length=45)
    direccion_e=models.CharField(max_length=45)
    #tFecha_creacion=models.CharField(max_length=45,null=False)
    idAgendamiento=models.ForeignKey(Agendamiento, on_delete=models.CASCADE)#
    idCondicion=models.ForeignKey(Condicion,on_delete=models.CASCADE)#
    idOficio=models.ForeignKey(Oficio, on_delete=models.CASCADE)#
    fecha=models.DateField(auto_now=True)
