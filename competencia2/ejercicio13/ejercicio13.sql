CREATE TABLE equipo (
    id_equipo SERIAL PRIMARY KEY,
    nombre_equipo VARCHAR(100) NOT NULL,
    ip VARCHAR(45) NOT NULL
);

CREATE TABLE alertas_seguridad (
    id_alerta SERIAL PRIMARY KEY,
    id_equipo INTEGER NOT NULL,
    tipo_alerta VARCHAR(100) NOT NULL,
    severidad VARCHAR(20) NOT NULL,
    fecha_alerta DATE NOT NULL
);