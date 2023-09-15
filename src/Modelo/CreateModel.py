

NewModel = '''
DROP DATABASE proyecto1;

CREATE DATABASE proyecto1;


CREATE TABLE proyecto1.ciudadano (
    dpi       VARCHAR(13)   NOT NULL,
    nombre    VARCHAR(30)   NOT NULL,
    apellido  VARCHAR(25)   NOT NULL,
    edad      INTEGER       NOT NULL,
    genero    VARCHAR(1)    NOT NULL,
    direccion VARCHAR(100)  NOT NULL,
    telefono  VARCHAR(10)   NOT NULL
);
ALTER TABLE proyecto1.ciudadano ADD CONSTRAINT ciudadano_pk PRIMARY KEY (dpi);


CREATE TABLE proyecto1.departamento (
    id_departamento INTEGER     NOT NULL,
    nombre          VARCHAR(14) NOT NULL
);
ALTER TABLE proyecto1.departamento ADD CONSTRAINT departamento_pk PRIMARY KEY ( id_departamento );


CREATE TABLE proyecto1.partido (
    id_partido    INTEGER NOT   NULL,
    nombrepartido VARCHAR(50)   NOT NULL,
    siglas        VARCHAR(10)   NOT NULL,
    fundacion     DATE          NOT NULL
);
ALTER TABLE proyecto1.partido ADD CONSTRAINT partido_pk PRIMARY KEY ( id_partido );


CREATE TABLE proyecto1.cargo (
    id_cargo INTEGER        NOT NULL,
    cargo    VARCHAR(50)   NOT NULL
);
ALTER TABLE proyecto1.cargo ADD CONSTRAINT cargo_pk PRIMARY KEY ( id_cargo );



CREATE TABLE proyecto1.mesa (
    id_mesa                      INTEGER NOT NULL,
    id_departamento              INTEGER NOT NULL
);

ALTER TABLE proyecto1.mesa ADD CONSTRAINT mesa_pk PRIMARY KEY ( id_mesa );
ALTER TABLE proyecto1.mesa ADD CONSTRAINT mesa_departamento_fk FOREIGN KEY ( id_departamento ) REFERENCES proyecto1.departamento ( id_departamento );


CREATE TABLE proyecto1.candidatos (
    id_candidato        INTEGER     NOT NULL,
    nombre              VARCHAR(50) NOT NULL,
    fechanacimiento     DATE        NOT NULL,
    id_cargo            INTEGER     NOT NULL,
    id_partido          INTEGER     NOT NULL
);

ALTER TABLE proyecto1.candidatos ADD CONSTRAINT candidatos_pk PRIMARY KEY ( id_candidato );
ALTER TABLE proyecto1.candidatos ADD CONSTRAINT candidatos_cargo_fk FOREIGN KEY ( id_cargo ) REFERENCES proyecto1.cargo ( id_cargo );
ALTER TABLE proyecto1.candidatos ADD CONSTRAINT candidatos_partido_fk FOREIGN KEY ( id_partido ) REFERENCES proyecto1.partido ( id_partido );


CREATE TABLE proyecto1.voto (
    id_voto     INTEGER     NOT NULL,
    fecha_hora  DATETIME    NOT NULL,
    id_dpi      VARCHAR(13) NOT NULL,
    id_mesa     INTEGER     NOT NULL
);

ALTER TABLE proyecto1.voto ADD CONSTRAINT voto_pk PRIMARY KEY ( id_voto );
ALTER TABLE proyecto1.voto ADD CONSTRAINT voto_ciudadano_fk FOREIGN KEY ( id_cargo )   REFERENCES proyecto1.ciudadano ( dpi );
ALTER TABLE proyecto1.voto ADD CONSTRAINT voto_mesa_fk      FOREIGN KEY ( id_partido ) REFERENCES proyecto1.mesa ( id_mesa );


CREATE TABLE proyecto1.normavoto (
    id_normavoto         INTEGER NOT NULL,
    id_candidato         INTEGER NOT NULL,
    id_voto              INTEGER NOT NULL
);

ALTER TABLE proyecto1.normavoto ADD CONSTRAINT normavoto_pk PRIMARY KEY ( id_normavoto );

ALTER TABLE proyecto1.normavoto ADD CONSTRAINT normavoto_candidatos_fk FOREIGN KEY (id_candidato) REFERENCES proyecto1.candidatos ( id_candidato );

ALTER TABLE proyecto1.normavoto ADD CONSTRAINT normavoto_voto_fk FOREIGN KEY (id_voto) REFERENCES proyecto1.voto ( id_voto );

'''

TablasTemporal = ''' 
CREATE TEMPORARY TABLE proyecto1.temp_ciudadano (
    dpi       VARCHAR(13)   NOT NULL,
    nombre    VARCHAR(30)   NOT NULL,
    apellido  VARCHAR(25)   NOT NULL,
    edad      INTEGER       NOT NULL,
    genero    VARCHAR(1)    NOT NULL,
    direccion VARCHAR(100)  NOT NULL,
    telefono  VARCHAR(10)   NOT NULL
);

CREATE TEMPORARY TABLE proyecto1.temp_departamento (
    id_departamento INTEGER     NOT NULL,
    nombre          VARCHAR(14) NOT NULL
);

CREATE TEMPORARY TABLE proyecto1.temp_partido (
    id_partido    INTEGER NOT   NULL,
    nombrepartido VARCHAR(50)   NOT NULL,
    siglas        VARCHAR(10)   NOT NULL,
    fundacion     DATE          NOT NULL
);

CREATE TEMPORARY TABLE proyecto1.temp_cargo (
    id_cargo INTEGER        NOT NULL,
    cargo    VARCHAR(50)   NOT NULL
);

CREATE TEMPORARY TABLE proyecto1.temp_mesa (
    id_mesa                      INTEGER NOT NULL,
    id_departamento              INTEGER NOT NULL
);

CREATE TEMPORARY TABLE proyecto1.temp_candidatos (
    id_candidato        INTEGER     NOT NULL,
    nombre              VARCHAR(50) NOT NULL,
    fechanacimiento     DATE        NOT NULL,
    id_cargo            INTEGER     NOT NULL,
    id_partido          INTEGER     NOT NULL
);

CREATE TEMPORARY TABLE proyecto1.temp_voto (
    id_voto     INTEGER     NOT NULL,
    fecha_hora  DATETIME    NOT NULL,
    id_dpi      VARCHAR(13) NOT NULL,
    id_mesa     INTEGER     NOT NULL
);

CREATE TEMPORARY TABLE proyecto1.temp_normavoto (
    id_normavoto         INTEGER NOT NULL,
    id_candidato         INTEGER NOT NULL,
    id_voto              INTEGER NOT NULL
);
'''


