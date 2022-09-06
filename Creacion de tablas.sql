use fundacion;
CREATE TABLE Empleados(
    idEmpleados INT AUTO_INCREMENT PRIMARY KEY,
    nombres_e VARCHAR(30),
    apellidos_e VARCHAR(30),
    documento_e INT(20),
    email_e VARCHAR(45),
    telefono_e INT(20),
    direccion_e VARCHAR(45),
    fecha_creacion DATETIME
);
Create table Agendamiento(
	idAgendamiento INT auto_increment primary key,
    horario_e DATETIME
);

Create table Usuarios(
	ID_usuario INT auto_increment primary key,
    nombres_u VARCHAR(45),
    apellidos_u VARCHAR(45),
	documento_u VARCHAR(45),
    email_u VARCHAR(45),
    telefono_u VARCHAR(45),
    direccion_u VARCHAR(45),
    nombres_r VARCHAR(45),
    telefono_r VARCHAR(45),
    parentesco_r VARCHAR(45),
    documento_r VARCHAR(45),
    usuario_u VARCHAR(45),
    password_u VARCHAR(45)
);

create table Oficio(
	idOficio INT auto_increment primary key,
    oficio_o VARCHAR(45),
    indicativo_o VARCHAR(45)
);

create table Transaccion(
	idTransaccion INT auto_increment primary key,
    costo_t VARCHAR(45),
    fecha_t VARCHAR(45),
    descripcion_t VARCHAR(45)
);

create table Entidad_salud(
	idEntidad_salud INT auto_increment primary key,
    entidad_es VARCHAR(45),
    valor_es VARCHAR(45),
    nit_es VARCHAR(45),
    ciudad_es VARCHAR(45),
    direccion_es VARCHAR(45),
    telefono_es VARCHAR(45),
    sector_productivo_es VARCHAR(45),
    fecha_creacion_es DATETIME
);
create table Condicion(
	idCondicion INT auto_increment primary key,
    indicativo_c VARCHAR(45),
    condicion_c VARCHAR(45)
);