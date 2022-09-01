use fundacionsherman;
create table login(
	ID_login int auto_increment primary key,
    correo_login varchar(45),
    usuario_app varchar(45),
    clave_app varchar(30),
    rol_login varchar(30),
    key index_correo_login(correo_login),
    key index_rol_login(rol_login)
);
create table usuarios(
	ID_usuario int primary key,
    nombres_usuario varchar(30),
    apellidos_usuario varchar(30),
    correo_usuario varchar(45),
    rol_usuario varchar(30),
    key index_nombres_usuario(nombres_usuario),
    key index_apellidos_usuario(apellidos_usuario),
    key index_correo_usuario(correo_usuario),
    constraint fk_login_id foreign key (ID_usuario) references login(ID_login),
    constraint fk_login_correo foreign key (correo_usuario) references login(correo_login),
    constraint fk_login_rol foreign key (rol_usuario) references login(rol_login)
);
create table entidades_salud(
	ID_entidad int auto_increment primary key,
    NIT_entidad int(11),
    nombre_entidad varchar(45),
    correo_entidad varchar(45),
    telefono_entidad int(20),
    direccion_entidad varchar(20),
    fecha_creacion_entidad varchar(10),
    key index_nombre_entidad(nombre_entidad)
);
create table clientes(
	ID_cliente int auto_increment primary key,
    documento_cliente int(11),
    nombres_cliente varchar (30),
    apellidos_cliente varchar (30),
    correo_cliente varchar (45),
    telefono_cliente int(20),
    direccion_cliente varchar(50),
    entidad_salud_cliente varchar(30),
    constraint fk_entidad_cliente_nombre foreign key(entidad_salud_cliente) references entidades_salud(nombre_entidad),
    constraint fk_usuario_cliente_nombres foreign key(nombres_cliente) references usuarios(nombres_usuario),
    constraint fk_usuario_cliente_apellidos foreign key(apellidos_cliente) references usuarios(apellidos_usuario),
    constraint fk_usuario_cliente_correo foreign key(correo_cliente) references usuarios(correo_usuario)
);
create table empleados(
	ID_empleado int auto_increment primary key,
    documento_empleado int(11),
    nombres_empleado varchar(30),
    apellidos_empleado varchar(30),
    correo_empleado varchar(45),
    telefono_empleado int(20),
    direccion_empleado varchar(20),
    cargo_empleado varchar(35),
    Key index_cargo_empleado(cargo_empleado),
    key index_nombres_empleado(nombres_empleado),
    key index_apellidos_empleado(apellidos_empleado),
    constraint fk_usuario_empleado_nombres foreign key(nombres_empleado) references usuarios(nombres_usuario),
    constraint fk_usuario_cempleado_apellidos foreign key(apellidos_empleado) references usuarios(apellidos_usuario),
    constraint fk_usuario_empleado_correo foreign key(correo_empleado) references usuarios(correo_usuario)
);
create table empresas_donadoras(
	ID_empresa int auto_increment primary key,
    NIT_empresa int(11),
    nombre_empresa varchar(45),
    correo_empresa varchar(45),
    telefono_empresa int(20),
    direccion_empresa varchar(20),
    regimen_tributario_empresa varchar(20),
    fecha_creacion_empresa varchar(10)
);
create table responsables_clientes(
	ID_responsable int auto_increment primary key,
    documento_responsable int(11),
    nombres_responsable varchar(30),
    apellidos_responsable varchar(30),
    correo_responsable varchar(45),
    telefono_responsable int(20),
    direccion_responsable varchar(30),
    relacion_responsable varchar(30),
	constraint fk_cliente_responsables_id foreign key(ID_responsable) references clientes(ID_cliente)
);
create table especialistas(
	ID_especialista int auto_increment primary key,
    nombres_especialista varchar(30),
    apellidos_especialista varchar(30),
    telefono_consultorio_especialista int(30),
    especialidad_especialista varchar(35),
    constraint fk_empleado_especialistas_cargo foreign key(especialidad_especialista) references empleados(cargo_empleado),
    constraint fk_empleado_especialistas_nombres foreign key(nombres_especialista) references empleados(nombres_empleado),
    constraint fk_empleado_especialistas_apellidos foreign key(apellidos_especialista) references empleados(apellidos_empleado)
);
create table auxiliar_contable(
	ID_auxiliar int auto_increment primary key,
    nombres_auxiliar varchar(30),
    apellidos_auxiliar varchar(30),
    area_auxiliar varchar (35),
    key index_nombres_auxiliar(nombres_auxiliar),
    key index_apellidos_auxiliar(apellidos_auxiliar),
    constraint fk_empleado_auxiliar_cargo foreign key(area_auxiliar) references empleados(cargo_empleado),
    constraint fk_empleado_auxiliar_nombres foreign key(nombres_auxiliar) references empleados(nombres_empleado),
    constraint fk_empleado_auxiliar_apellidos foreign key(apellidos_auxiliar) references empleados(apellidos_empleado)
);
create table transacciones_balance(
	ID int auto_increment primary key,
    cuenta_contable int(10),
    concepto_descripcion varchar(45),
    usuario_sujeto_operacion varchar(40),
    tipo_ingreso_egreso varchar(10),
    monto int,
    auxiliar_registro varchar(45),
    fecha_registro varchar(10)
);
create table citas_medicas_clientes(
	ID_cita int auto_increment primary key,
    ID_paciente int,
    ID_especialista int,
    fecha_cita varchar(10),
    hora_cita varchar(10),
    numero_orden int(10),
    fecha_registro_cita varchar(10),
    constraint fk_cliente_cita_id foreign key (ID_paciente) references clientes(ID_cliente),
    constraint fk_especialistas_cita_id foreign key (ID_especialista) references especialistas(ID_especialista)
);
create table examenes_medicos(
	ID_examen int auto_increment primary key,
    ID_paciente int,
    ID_especialista int,
    examen_realizado varchar(40),
    fecha_examen varchar(10),
    hora_examen varchar(10),
    resultados varchar(200),
    key index_examen_realizado(examen_realizado),
    constraint fk_cliente_examen_id foreign key (ID_paciente) references clientes(ID_cliente),
    constraint fk_especialistas_examen_id foreign key (ID_especialista) references especialistas(ID_especialista)
);
create table consultas_medicas(
	ID_consulta int auto_increment primary key,
    ID_paciente int,
    ID_especialista int,
    motivo varchar(200),
    examenes_realizados varchar(40),
    tratamiento varchar (200),
    fecha_consulta varchar(10),
    hora_consulta varchar(10),
    constraint fk_examen_consulta_id foreign key (examenes_realizados) references examenes_medicos(examen_realizado),
    constraint fk_cliente_consulta_id foreign key (ID_paciente) references clientes(ID_cliente),
    constraint fk_especialistas_consulta_id foreign key (ID_especialista) references especialistas(ID_especialista)
);
	