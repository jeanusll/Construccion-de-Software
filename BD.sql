CREATE TABLE grupo_usuarios (
	id_grupo_usuario INT  PRIMARY KEY AUTO_INCREMENT,
	restricciones VARCHAR(100),
	accesos VARCHAR(100)
);

CREATE TABLE usuarios(
	id_usuario INT PRIMARY KEY AUTO_INCREMENT,
	id_grupo_usuario INT,
	email VARCHAR(50) not null unique,
	contra VARCHAR(100) not null,

	FOREIGN KEY (id_grupo_usuario) REFERENCES grupo_usuarios (id_grupo_usuario)

);

CREATE TABLE administradores (
	id_administrador INT PRIMARY KEY AUTO_INCREMENT,
	id_usuario INT,
	FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
);

CREATE TABLE alumnos (
  dni_alumno VARCHAR(8) PRIMARY KEY,
  id_usuario INT not null unique,
  nombre VARCHAR(50),
  apellido VARCHAR(50),
  fecha_nacimiento DATE,
  foto text,
  vector text,
  FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
);

CREATE TABLE cursos(
	id_curso INT PRIMARY KEY AUTO_INCREMENT,
	nombre_curso VARCHAR(50),
	semestre INTEGER CHECK (semestre > 0 AND semestre < 13),
	horas_academicas INTEGER NOT NULL,
	total_estudiantes INTEGER DEFAULT 0
);

CREATE TABLE profesores (
	profesor_dni varchar(8) PRIMARY KEY NOT NULL,
	profesor_nombre varchar(100),
	profesor_apellido varchar(100),
	profesor_fecha_nac DATE,
	id_usuario int not null unique,
  	FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario)
);

CREATE TABLE profesor_curso (
	profesor_dni varchar(8),
	id_curso INT,
	FOREIGN KEY (profesor_dni) REFERENCES profesores (profesor_dni),
	FOREIGN KEY (id_curso) REFERENCES cursos (id_curso)
);

CREATE TABLE horarios (
	id_horario INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	id_curso INT,
	hora_inicio VARCHAR(10),
	hora_final VARCHAR(10),
	dia VARCHAR(10),
	aula VARCHAR(15),
	FOREIGN KEY (id_curso) REFERENCES cursos (id_curso)
);

CREATE TABLE secciones (
	id_seccion INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	nombre_seccion varchar(50),
	id_curso int,
	CONSTRAINT fk_secciones_cursos
	FOREIGN KEY (id_curso) REFERENCES cursos (id_curso)
);

CREATE TABLE asistencias (
	id_asistencia INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	dni_alumno VARCHAR(8),
	id_curso INT,
	fecha DATE,
	hora_asistencia VARCHAR(10),
	tema_realizado VARCHAR(30),
	asistio BOOLEAN,
	FOREIGN KEY (dni_alumno) REFERENCES alumnos (dni_alumno),
	FOREIGN KEY (id_curso) REFERENCES cursos (id_curso)
);

CREATE TABLE solicitudes (
	id_solicitud INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	id_asistencia INT unique,
	documento VARCHAR(20),
	estado BOOLEAN,
	justificación VARCHAR(60),
	FOREIGN KEY (id_asistencia) REFERENCES asistencias (id_asistencia)
);

CREATE TABLE participaciones (
	id_participacion INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	dni_alumno VARCHAR(8),
	id_curso INT,
	total_puntos INT,
	FOREIGN KEY (dni_alumno) REFERENCES alumnos (dni_alumno)
);

create table listas (
	id_lista int PRIMARY KEY NOT NULL AUTO_INCREMENT,
	id_curso int unique,
	dni_alumno varchar(8),
	estado BOOLEAN,
	FOREIGN KEY (dni_alumno) REFERENCES alumnos (dni_alumno),
	FOREIGN KEY (id_curso) REFERENCES cursos (id_curso)
);
