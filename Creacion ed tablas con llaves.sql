use fundacion;
CREATE TABLE Empleados(
    idEmpleados INT(20) AUTO_INCREMENT PRIMARY KEY,
    nombres_e VARCHAR(30),
    apellidos_e VARCHAR(30),
    documento_e INT(20),
    email_e VARCHAR(45),
    telefono_e INT(20),
    direccion_e VARCHAR(45),
    fecha_creacion DATETIME
    /*CONSTRAINT fk_Empleados_Agendamiento1 FOREIGN KEY (idEmpleados)
	*REFERENCES Agendamiento (idAgendamiento),
	*CONSTRAINT fk_Empleados_Oficio1 FOREIGN KEY (idEmpleados)
	* REFERENCES Oficio (idOficio)
	*/
);
Create table Agendamiento(
	idAgendamiento INT auto_increment primary key,
    horario_e VARCHAR(45)
	/*
    constraint fk_Agendamiento_Usuarios1 foreign key (idAgendamiento) references Empleados(idEmpleados),
    constraint fk_Agendamiento_Transaccion1 foreign key (idAgendamiento) references Transaccion(idTransaccion)
    */
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
    /*
	constraint fk_Usuarios_Entidad_salud1 foreign key (IDusuario) references Entidad_salud(idEntidad_salud),
	constraint fk_Condicion_idCondicion foreign key (IDusuario) references Entidad_salud(idEntidad_salud),
	constraint fk_Usuarios_Entidad_salud1 foreign key (IDusuario) references Entidad_salud(idEntidad_salud)
    */
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
    /*
	constraint fk_Usuarios_Entidad_salud1 foreign key (IDusuario) references Entidad_salud(idEntidad_salud),
	constraint fk_Condicion_idCondicion foreign key (IDusuario) references Entidad_salud(idEntidad_salud),
	constraint fk_Usuarios_Entidad_salud1 foreign key (IDusuario) references Entidad_salud(idEntidad_salud*/
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