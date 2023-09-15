-- Autor: Kemel Josue Efraín Ruano Jerónimo
-- Fecha: 2023-09-15


-- ------------------------------------------------------------------
-- ------------------           MODELO             ------------------
-- ------------------------------------------------------------------
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

-- ------------------------------------------------------------------
-- ------------------   TABLAS TEMPORALES          ------------------
-- ------------------------------------------------------------------


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


-- ------------------------------------------------------------------
-- ------------------   CONSULTAS REALIZADAS       ------------------
-- ------------------------------------------------------------------

-- CONSULTA 1
SELECT
    P.nombre AS PRESIDENTE,
    V.nombre AS VICEPRESIDENTE,
    PR.siglas AS PARTIDO
FROM proyecto1.candidatos P  
INNER  JOIN proyecto1.candidatos V ON P.id_partido = V.id_partido AND P.id_cargo = 1 AND V.id_cargo = 2
INNER JOIN proyecto1.partido PR ON P.id_partido = PR.id_partido;

-- CONSULTA 2
SELECT
      PP.siglas AS PARTIDO,
      COUNT(C.id_candidato) AS CANTIDAD
FROM proyecto1.partido PP
INNER JOIN proyecto1.candidatos C ON PP.id_partido = C.id_partido 
WHERE C.id_cargo = 3 or C.id_cargo = 4 or C.id_cargo = 5
GROUP BY PP.siglas 
ORDER BY PP.siglas 	ASC;

-- CONSULTA 3
SELECT
	  C.nombre AS NOMBRE,
      PP.nombrepartido AS PARTIDO
FROM proyecto1.partido PP
INNER JOIN proyecto1.candidatos C ON PP.id_partido = C.id_partido 
WHERE C.id_cargo = 6 
ORDER BY PP.nombrepartido ASC;


-- CONSULTA 4
SELECT
      PP.nombrepartido AS PARTIDO,
      COUNT(C.id_candidato) AS CANTIDAD
FROM proyecto1.partido PP
INNER JOIN proyecto1.candidatos C ON PP.id_partido = C.id_partido 
WHERE  PP.id_partido != -1
GROUP BY PP.nombrepartido

-- CONSULTA 5
SELECT
	DP.nombre AS DEPARTAMENTO,
    COUNT(VT.id_voto) AS CANTIDAD
FROM proyecto1.departamento DP
INNER JOIN proyecto1.mesa MS ON DP.id_departamento = MS.id_departamento
INNER JOIN proyecto1.voto VT ON MS.id_mesa = VT.id_mesa
GROUP BY DP.nombre
ORDER BY DP.nombre ASC;

-- CONSULTA 6
SELECT
    COUNT(DISTINCT VT.id_dpi) AS NULO
FROM proyecto1.normavoto NV
INNER JOIN proyecto1.voto VT ON NV.id_voto = VT.id_voto
WHERE NV.id_candidato = -1

-- CONSULTA 7
SELECT
    CD.edad AS EDAD,
    COUNT(VT.id_voto) AS CANTIDAD_DE_VOTOS
FROM proyecto1.ciudadano CD
INNER JOIN proyecto1.voto VT ON CD.dpi = VT.id_dpi
GROUP BY CD.edad
ORDER BY COUNT(VT.id_voto) DESC  LIMIT 10

-- CONSULTA 8
SELECT
  GROUP_CONCAT( DISTINCT CN.nombre) AS PRESIDENTE,
  GROUP_CONCAT(DISTINCT VICE.nombre) AS VICE,
  COUNT(NV.id_voto) AS VOTOSTOTAL
FROM proyecto1.normavoto NV 
INNER JOIN proyecto1.candidatos CN ON NV.id_candidato = CN.id_candidato
INNER JOIN proyecto1.candidatos VICE ON CN.id_partido = VICE.id_partido AND CN.id_cargo = 1 AND VICE.id_cargo = 2
INNER JOIN proyecto1.partido PT ON CN.id_partido = PT.id_partido
GROUP BY PT.siglas
ORDER BY COUNT(NV.id_voto) DESC LIMIT 10;

-- CONSULTA 9
SELECT 
   VT.id_mesa AS No_Mesa,
   DP.nombre AS  Nombre_DEPA,
   COUNT(VT.id_voto) AS VOTOPORMESA
FROM proyecto1.voto VT
INNER JOIN proyecto1.mesa MS ON VT.id_mesa = MS.id_mesa
INNER JOIN proyecto1.departamento DP ON MS.id_departamento = DP.id_departamento
GROUP BY VT.id_mesa
ORDER BY COUNT(VT.id_voto) DESC LIMIT 5;

-- CONSULTA 10
SELECT 
    HOUR(VT.fecha_hora) AS Hora, 
    COUNT(VT.id_voto) AS VOTOS
FROM proyecto1.voto VT
GROUP BY HOUR(VT.fecha_hora)
ORDER BY COUNT(VT.id_voto) DESC LIMIT 5;

-- CONSULTA 11
SELECT 
    CD.genero AS GENERO,
    COUNT(VT.id_voto) AS VOTACION
FROM proyecto1.ciudadano CD
INNER JOIN proyecto1.voto VT ON CD.dpi = VT.id_dpi
GROUP BY CD.genero
ORDER BY CD.genero ASC;
