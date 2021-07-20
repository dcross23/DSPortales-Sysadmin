CREATE USER 'admin'@'localhost' IDENTIFIED BY '123456';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;

CREATE DATABASE dsportales;


CREATE TABLE dsportales.cola_eliminar(
        usuario varchar(10) NOT NULL PRIMARY KEY
);

CREATE TABLE dsportales.cola_pag_personales(
        usuario varchar(10) NOT NULL PRIMARY KEY
);

CREATE TABLE dsportales.cola_modificar(
        usuario varchar(10) NOT NULL PRIMARY KEY,
        passwd varchar(80) NOT NULL
);

CREATE TABLE dsportales.datos_usuarios(
        usuario varchar(10) NOT NULL PRIMARY KEY,
        nombre varchar(40) NOT NULL,
        apellidos varchar(50) NOT NULL,
        email varchar(50) NOT NULL,
        direccion varchar(50) NOT NULL
);

CREATE TABLE dsportales.registros(
        usuario varchar(10) NOT NULL PRIMARY KEY,
        passwd varchar(80) NOT NULL,
        nombre varchar(40) NOT NULL,
        apellidos varchar(50) NOT NULL,
        email varchar(50) NOT NULL,
        direccion varchar(50) NOT NULL
);
