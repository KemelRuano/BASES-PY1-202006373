import json
from Conexion.Conected import *
from collections import OrderedDict

consulta1 = '''
SELECT
    P.nombre AS PRESIDENTE,
    V.nombre AS VICEPRESIDENTE,
    PR.siglas AS PARTIDO
FROM proyecto1.candidatos P  
INNER  JOIN proyecto1.candidatos V ON P.id_partido = V.id_partido AND P.id_cargo = 1 AND V.id_cargo = 2
INNER JOIN proyecto1.partido PR ON P.id_partido = PR.id_partido;
'''
consulta2 = '''
SELECT
      PP.siglas AS PARTIDO,
      COUNT(C.id_candidato) AS CANTIDAD
FROM proyecto1.partido PP
INNER JOIN proyecto1.candidatos C ON PP.id_partido = C.id_partido 
WHERE C.id_cargo = 3 or C.id_cargo = 4 or C.id_cargo = 5
GROUP BY PP.siglas 
ORDER BY PP.siglas 	ASC;
'''

consulta3 = '''
SELECT
	  C.nombre AS NOMBRE,
      PP.nombrepartido AS PARTIDO
FROM proyecto1.partido PP
INNER JOIN proyecto1.candidatos C ON PP.id_partido = C.id_partido 
WHERE C.id_cargo = 6 
ORDER BY PP.nombrepartido ASC;
'''

consulta4 = '''
SELECT
      PP.nombrepartido AS PARTIDO,
      COUNT(C.id_candidato) AS CANTIDAD
FROM proyecto1.partido PP
INNER JOIN proyecto1.candidatos C ON PP.id_partido = C.id_partido 
WHERE  PP.id_partido != -1
GROUP BY PP.nombrepartido
'''
consulta5 = '''
SELECT
	DP.nombre AS DEPARTAMENTO,
    COUNT(VT.id_voto) AS CANTIDAD
FROM proyecto1.departamento DP
INNER JOIN proyecto1.mesa MS ON DP.id_departamento = MS.id_departamento
INNER JOIN proyecto1.voto VT ON MS.id_mesa = VT.id_mesa
GROUP BY DP.nombre
ORDER BY DP.nombre ASC;
'''
consulta6 = '''
SELECT
    COUNT(DISTINCT VT.id_dpi) AS NULO
FROM proyecto1.normavoto NV
INNER JOIN proyecto1.voto VT ON NV.id_voto = VT.id_voto
WHERE NV.id_candidato = -1
'''
consulta7 = '''
SELECT
    CD.edad AS EDAD,
    COUNT(VT.id_voto) AS CANTIDAD_DE_VOTOS
FROM proyecto1.ciudadano CD
INNER JOIN proyecto1.voto VT ON CD.dpi = VT.id_dpi
GROUP BY CD.edad
ORDER BY COUNT(VT.id_voto) DESC  LIMIT 10
'''
consulta8 = '''
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
'''
consulta9 = '''
SELECT 
   VT.id_mesa AS No_Mesa,
   DP.nombre AS  Nombre_DEPA,
   COUNT(VT.id_voto) AS VOTOPORMESA
FROM proyecto1.voto VT
INNER JOIN proyecto1.mesa MS ON VT.id_mesa = MS.id_mesa
INNER JOIN proyecto1.departamento DP ON MS.id_departamento = DP.id_departamento
GROUP BY VT.id_mesa
ORDER BY COUNT(VT.id_voto) DESC LIMIT 5;
'''
consulta10 = '''
SELECT 
    HOUR(VT.fecha_hora) AS Hora, 
    COUNT(VT.id_voto) AS VOTOS
FROM proyecto1.voto VT
GROUP BY HOUR(VT.fecha_hora)
ORDER BY COUNT(VT.id_voto) DESC LIMIT 5;
'''

consulta11 = '''
SELECT 
    CD.genero AS GENERO,
    COUNT(VT.id_voto) AS VOTACION
FROM proyecto1.ciudadano CD
INNER JOIN proyecto1.voto VT ON CD.dpi = VT.id_dpi
GROUP BY CD.genero
ORDER BY CD.genero ASC;
'''
def Response1():
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    
    cursor.execute(consulta1)
    
    ListResponse = cursor.fetchall()
    ListEnv = []
    for new in ListResponse:
        credenciales = OrderedDict()
        credenciales['Presidente'] = new[0]
        credenciales['Vicepresidente'] = new[1]
        credenciales['Partido'] = new[2]
        ListEnv.append(credenciales)
    cursor.close()
    connection.close()
    return json.dumps(ListEnv)
        
def Response2():
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    
    cursor.execute(consulta2)
    
    ListResponse = cursor.fetchall()
    ListEnv = []
    for new in ListResponse:
        credenciales = OrderedDict()
        credenciales['PARTIDO'] = new[0]
        credenciales['CANTIDAD'] = new[1]
        ListEnv.append(credenciales)
    cursor.close()
    connection.close()
    return json.dumps(ListEnv)


def Response3():
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    
    cursor.execute(consulta3)
    
    ListResponse = cursor.fetchall()
    ListEnv = []
    for new in ListResponse:
        credenciales = OrderedDict()
        credenciales['NOMBRE ALCALDE'] = new[0]
        credenciales['PARTIDO'] = new[1]
        ListEnv.append(credenciales)
    cursor.close()
    connection.close()
    return json.dumps(ListEnv)

def Response4():
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    
    cursor.execute(consulta4)
    
    ListResponse = cursor.fetchall()
    ListEnv = []
    for new in ListResponse:
        credenciales = OrderedDict()
        credenciales['PARTIDO'] = new[0]
        credenciales['CANTIDAD'] = new[1]
        ListEnv.append(credenciales)
    cursor.close()
    connection.close()
    return json.dumps(ListEnv)


def Response5():
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    
    cursor.execute(consulta5)
    
    ListResponse = cursor.fetchall()
    ListEnv = []
    for new in ListResponse:
        credenciales = OrderedDict()
        credenciales['DEPARTAMENTO'] = new[0]
        credenciales['CANTIDAD'] = new[1]
        ListEnv.append(credenciales)
    cursor.close()
    connection.close()
    return json.dumps(ListEnv)


def Response6():
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    
    cursor.execute(consulta6)
    
    credenciales = OrderedDict()
    for new in cursor.fetchall():
         credenciales['VOTOS NULOS'] = new[0]
    
    cursor.close()
    connection.close()
    return json.dumps(credenciales)

def Response7():
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    
    cursor.execute(consulta7)

    ListEnv = []
    cont = 1
    for new in cursor.fetchall():
        credenciales = OrderedDict()
        credenciales['TOP'] = cont
        credenciales['EDAD'] = new[0]
        credenciales['CANTIDAD'] = new[1]
        ListEnv.append(credenciales)
        cont = cont + 1
    
    cursor.close()
    connection.close()
    return json.dumps(ListEnv)

def Response8():
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    
    cursor.execute(consulta8)

    ListEnv = []
    cont = 1
    for new in cursor.fetchall():
        credenciales = OrderedDict()
        credenciales['TOP'] = cont
        credenciales['PRESIDENTE'] = new[0]
        credenciales['VICEPRESIDENTE'] = new[1]
        credenciales['VOTOS TOTALES'] = new[2]
        ListEnv.append(credenciales)
        cont = cont + 1
    
    cursor.close()
    connection.close()
    return json.dumps(ListEnv)


def Response9():
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    
    cursor.execute(consulta9)

    ListEnv = []
    cont = 1
    for new in cursor.fetchall():
        credenciales = OrderedDict()
        credenciales['TOP'] = cont
        credenciales['No. Mesa'] = new[0]
        credenciales['DEPARTAMENTO'] = new[1]
        credenciales['VOTOS POR MESA'] = new[2]
        ListEnv.append(credenciales)
        cont = cont + 1
    
    cursor.close()
    connection.close()
    return json.dumps(ListEnv)


def Response10():
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    
    cursor.execute(consulta10)

    ListEnv = []
    cont = 1
    for new in cursor.fetchall():
        credenciales = OrderedDict()
        credenciales['TOP'] = cont
        credenciales['HORA'] = new[0]
        credenciales['NO. VOTOS'] = new[1]
        ListEnv.append(credenciales)
        cont = cont  + 1
    
    cursor.close()
    connection.close()
    return json.dumps(ListEnv)


def Response11():
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    
    cursor.execute(consulta11)

    ListEnv = []
    for new in cursor.fetchall():
        credenciales = OrderedDict()
        credenciales['GENERO'] = new[0]
        credenciales['NO. VOTOS'] = new[1]
        ListEnv.append(credenciales)
    
    cursor.close()
    connection.close()
    return json.dumps(ListEnv)