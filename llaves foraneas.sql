    /* Empleados */
Alter table Empleados
add FOREIGN KEY (idEmpleados)
	REFERENCES Agendamiento (idAgendamiento);
Alter table Empleados
add FOREIGN KEY (idEmpleados)
	REFERENCES Oficio (idOficio);
	
    /* Agendamiento */
Alter table Agendamiento
add FOREIGN KEY (idAgendamiento)
	REFERENCES Empleados(idEmpleados);
Alter table Agendamiento
add FOREIGN KEY (idAgendamiento)
	REFERENCES Transaccion(idTransaccion);
    
        /*Usuarios*/
Alter table Usuarios
add FOREIGN KEY (ID_usuario)
	REFERENCES Entidad_salud(idEntidad_salud);
Alter table Usuarios
add FOREIGN KEY (ID_usuario)
	REFERENCES Condicion(idCondicion);
Alter table Usuarios
add FOREIGN KEY (ID_usuario)
	REFERENCES transaccion(idTransaccion);
    
        /*Transaccion falta terminarlas*/
Alter table Transaccion
add FOREIGN KEY (idTransaccion)
	REFERENCES Entidad_salud(idEntidad_salud);
Alter table Transaccion
add FOREIGN KEY (idTransaccion)
	REFERENCES oficio(idOficio);