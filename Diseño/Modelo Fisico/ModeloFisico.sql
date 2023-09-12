-- Generado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   en:        2023-09-11 23:23:24 CST
--   sitio:      Oracle Database 12c
--   tipo:      Oracle Database 12c



DROP TABLE candidatos CASCADE CONSTRAINTS;

DROP TABLE cargo CASCADE CONSTRAINTS;

DROP TABLE ciudadano CASCADE CONSTRAINTS;

DROP TABLE departamento CASCADE CONSTRAINTS;

DROP TABLE mesa CASCADE CONSTRAINTS;

DROP TABLE normavoto CASCADE CONSTRAINTS;

DROP TABLE partido CASCADE CONSTRAINTS;

DROP TABLE voto CASCADE CONSTRAINTS;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE candidatos (
    id_candidato       INTEGER NOT NULL,
    nombre             VARCHAR2(30) NOT NULL,
    fechanacimiento    DATE NOT NULL,
    cargo_id_cargo     INTEGER NOT NULL,
    partido_id_partido INTEGER NOT NULL
);

ALTER TABLE candidatos ADD CONSTRAINT candidatos_pk PRIMARY KEY ( id_candidato );

CREATE TABLE cargo (
    id_cargo INTEGER NOT NULL,
    cargo    VARCHAR2(30) NOT NULL
);

ALTER TABLE cargo ADD CONSTRAINT cargo_pk PRIMARY KEY ( id_cargo );

CREATE TABLE ciudadano (
    dpi       VARCHAR2(13) NOT NULL,
    nombre    VARCHAR2(30) NOT NULL,
    apellido  VARCHAR2(25) NOT NULL,
    edad      INTEGER NOT NULL,
    genero    VARCHAR2(1) NOT NULL,
    direccion VARCHAR2(100) NOT NULL,
    telefono  VARCHAR2(10) NOT NULL
);

ALTER TABLE ciudadano ADD CONSTRAINT ciudadano_pk PRIMARY KEY ( dpi );

CREATE TABLE departamento (
    id_departamento INTEGER NOT NULL,
    nombre          VARCHAR2(14) NOT NULL
);

ALTER TABLE departamento ADD CONSTRAINT departamento_pk PRIMARY KEY ( id_departamento );

CREATE TABLE mesa (
    id_mesa                      INTEGER NOT NULL,
    departamento_id_departamento INTEGER NOT NULL
);

ALTER TABLE mesa ADD CONSTRAINT mesa_pk PRIMARY KEY ( id_mesa );

CREATE TABLE normavoto (
    candidatos_id_candidato INTEGER NOT NULL,
    voto_id_voto            INTEGER NOT NULL,
    id_normavoto            INTEGER NOT NULL
);

ALTER TABLE normavoto ADD CONSTRAINT normavoto_pk PRIMARY KEY ( id_normavoto );

CREATE TABLE partido (
    id_partido    INTEGER NOT NULL,
    nombrepartido VARCHAR2(50) NOT NULL,
    siglas        VARCHAR2(10) NOT NULL,
    fundacion     DATE NOT NULL
);

ALTER TABLE partido ADD CONSTRAINT partido_pk PRIMARY KEY ( id_partido );

CREATE TABLE voto (
    id_voto       INTEGER NOT NULL,
    fecha_hora    DATE NOT NULL,
    ciudadano_dpi VARCHAR2(13) NOT NULL,
    mesa_id_mesa  INTEGER NOT NULL
);

ALTER TABLE voto ADD CONSTRAINT voto_pk PRIMARY KEY ( id_voto );

ALTER TABLE candidatos
    ADD CONSTRAINT candidatos_cargo_fk FOREIGN KEY ( cargo_id_cargo )
        REFERENCES cargo ( id_cargo );

ALTER TABLE candidatos
    ADD CONSTRAINT candidatos_partido_fk FOREIGN KEY ( partido_id_partido )
        REFERENCES partido ( id_partido );

ALTER TABLE mesa
    ADD CONSTRAINT mesa_departamento_fk FOREIGN KEY ( departamento_id_departamento )
        REFERENCES departamento ( id_departamento );

ALTER TABLE normavoto
    ADD CONSTRAINT normavoto_candidatos_fk FOREIGN KEY ( candidatos_id_candidato )
        REFERENCES candidatos ( id_candidato );

ALTER TABLE normavoto
    ADD CONSTRAINT normavoto_voto_fk FOREIGN KEY ( voto_id_voto )
        REFERENCES voto ( id_voto );

ALTER TABLE voto
    ADD CONSTRAINT voto_ciudadano_fk FOREIGN KEY ( ciudadano_dpi )
        REFERENCES ciudadano ( dpi );

ALTER TABLE voto
    ADD CONSTRAINT voto_mesa_fk FOREIGN KEY ( mesa_id_mesa )
        REFERENCES mesa ( id_mesa );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                             8
-- CREATE INDEX                             0
-- ALTER TABLE                             15
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- TSDP POLICY                              0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
