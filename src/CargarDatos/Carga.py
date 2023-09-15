import csv
from Modelo.CreateModel import*
from Conexion.Conected import*
import mysql.connector
from datetime import datetime


def CargaMasiva(carpeta) :
    
    connection = mysql.connector.connect(**db)
    cursor = connection.cursor()
    
    sql_commands = TablasTemporal.split(";")
    sql_commands = [command.strip() for command in sql_commands if command.strip()]

    for command in sql_commands:
         cursor.execute(command)
    
    #-----------------------------------------------  Cargar csv ciudadanos
    TuplaDate = []
    ReadCargo = open(carpeta + "\\ciudadanos.csv", "r",encoding='utf-8')
    SplitCargo = csv.reader(ReadCargo,delimiter = ",")
    next(SplitCargo,None)
    for line in SplitCargo:
        Dpi = line[0]
        Nombre = line[1]
        Apellido = line[2]
        Direccion = line[3]
        Telefono = line[4]
        Edad = line[5]
        Genero = line[6]
        NewDate = (Dpi,Nombre,Apellido,Edad,Genero,Direccion,Telefono)
        TuplaDate.append(NewDate)
    
    cursor.executemany("INSERT INTO proyecto1.temp_ciudadano (dpi,nombre,apellido,edad,genero,direccion,telefono) VALUES (%s,%s,%s,%s,%s,%s,%s)",TuplaDate) 
    cursor.execute("INSERT INTO proyecto1.ciudadano  (dpi,nombre,apellido,edad,genero,direccion,telefono) SELECT dpi,nombre,apellido,edad,genero,direccion,telefono  FROM proyecto1.temp_ciudadano")
    
    #--------------------------------------------------- Cargar csv departamento
    TuplaDate = []
    ReadDepa = open(carpeta + "\\departamentos.csv", "r",encoding='utf-8')
    SplitDepa = csv.reader(ReadDepa,delimiter = ",")
    next(SplitDepa,None)
    for line in SplitDepa:
        Id = line[0]
        Nombre = line[1]
        NewDate = (Id,Nombre)
        TuplaDate.append(NewDate)
    
    cursor.executemany("INSERT INTO proyecto1.temp_departamento (id_departamento,nombre) VALUES (%s,%s)",TuplaDate)
    cursor.execute("INSERT INTO proyecto1.departamento (id_departamento,nombre) SELECT id_departamento,nombre FROM proyecto1.temp_departamento")
    
    #-----------------------------------------------------  Cargar csv partido
    TuplaDate = []
    ReadPartido = open(carpeta + "\\partidos.csv", "r",encoding='utf-8')
    SplitPartido = csv.reader(ReadPartido,delimiter = ",")
    next(SplitPartido,None)
    for line in SplitPartido:
        Id = line[0]
        Nombre = line[1]
        Siglas = line[2]
        Fecha = line[3]
        NewDate = (Id,Nombre,Siglas,ConvertirFecha(Fecha))
        TuplaDate.append(NewDate)
        
    cursor.executemany("INSERT INTO proyecto1.temp_partido (id_partido,nombrepartido,siglas,fundacion) VALUES (%s,%s,%s,%s)",TuplaDate)
    cursor.execute("INSERT INTO proyecto1.partido (id_partido,nombrepartido,siglas,fundacion) SELECT id_partido,nombrepartido,siglas,fundacion FROM proyecto1.temp_partido")  
    
    #------------------------------------------------------ Cargar csv cargo
    TuplaDate = []
    ReadCargo = open(carpeta + "\\cargos.csv", "r",encoding='utf-8')
    SplitCargo = csv.reader(ReadCargo,delimiter = ",")
    next(SplitCargo,None)
    for line in SplitCargo:
        Id = line[0]
        Cargo = line[1]
        NewDate = (Id,Cargo)
        TuplaDate.append(NewDate)
    
    cursor.executemany("INSERT INTO proyecto1.temp_cargo (id_cargo,cargo) VALUES (%s,%s)",TuplaDate)
    cursor.execute("INSERT INTO proyecto1.cargo (id_cargo,cargo) SELECT id_cargo,cargo FROM proyecto1.temp_cargo")
        
    
    
        
    #------------------------------------------------------ Cargar csv mesa
    TuplaDate = []
    ReadMesa = open(carpeta + "\\mesas.csv", "r",encoding='utf-8')
    SplitMesa = csv.reader(ReadMesa,delimiter = ",")
    next(SplitMesa,None)
    for line in SplitMesa:
        IdMesa = line[0]
        IdDepartamento = line[1]
        NewDate = (IdMesa,IdDepartamento)
        TuplaDate.append(NewDate)
    
    cursor.executemany("INSERT INTO proyecto1.temp_mesa (id_mesa,id_departamento) VALUES (%s,%s)",TuplaDate)
    cursor.execute("INSERT INTO proyecto1.mesa (id_mesa,id_departamento) SELECT id_mesa,id_departamento FROM proyecto1.temp_mesa")
    
    
    #------------------------------------------------------ Cargar csv candidatos
    
    TuplaDate = []
    ReadCandidatos = open(carpeta + "\\candidatos.csv", "r",encoding='utf-8')
    SplitCandidatos = csv.reader(ReadCandidatos,delimiter = ",")
    next(SplitCandidatos,None)
    for line in SplitCandidatos:
        Id = line[0]
        Nombre = line[1]
        Fecha = ConvertirFecha(line[2])
        partido = line[3]
        cargo = line[4]
        NewDate = (Id,Nombre,Fecha,cargo,partido)
        TuplaDate.append(NewDate)
    
    cursor.executemany("INSERT INTO proyecto1.temp_candidatos (id_candidato,nombre,fechanacimiento,id_cargo,id_partido) VALUES (%s,%s,%s,%s,%s)",TuplaDate)
    cursor.execute("INSERT INTO proyecto1.candidatos (id_candidato,nombre,fechanacimiento,id_cargo,id_partido) SELECT id_candidato,nombre,fechanacimiento,id_cargo,id_partido FROM proyecto1.temp_candidatos")
    
    #------------------------------------------------------ Cargar csv voto
    
    TuplaDate = []
    TuplaDate2 = []
    ReadVoto = open(carpeta + "\\votaciones.csv", "r",encoding='utf-8')
    SplitVoto = csv.reader(ReadVoto,delimiter = ",")
    next(SplitVoto,None)
    contid = 0
    for line in SplitVoto:
        id_voto = line[0]
        id_candidate = line[1]
        dpi = line[2]
        mesa_id = line[3]
        fecha_hora = ConverDataTime(line[4])
        newVoto = (id_voto,fecha_hora,dpi,mesa_id)
        TuplaDate.append(newVoto)
        newNorma = (contid,id_candidate,id_voto)
        TuplaDate2.append(newNorma)
        contid += 1
        
    
    
    #Delete duplicados
    conjunto = set(TuplaDate)
    NewTuple = tuple(conjunto)
    cursor.executemany("INSERT INTO proyecto1.temp_voto ( id_voto,fecha_hora,id_dpi,id_mesa) VALUES (%s,%s,%s,%s)",NewTuple)
    cursor.execute("INSERT INTO proyecto1.voto ( id_voto,fecha_hora,id_dpi,id_mesa) SELECT id_voto,fecha_hora,id_dpi,id_mesa FROM proyecto1.temp_voto")
    
    cursor.executemany("INSERT INTO proyecto1.temp_normavoto (id_normavoto , id_candidato,id_voto) VALUES (%s,%s,%s)",TuplaDate2)
    cursor.execute("INSERT INTO proyecto1.normavoto (id_normavoto , id_candidato,id_voto) SELECT id_normavoto , id_candidato,id_voto FROM proyecto1.temp_normavoto")
   
    connection.commit()
    cursor.close()
    connection.close()
    
    return "Carga Masiva Exitosa"
    
    
    
    
def GenerateModel():
    sql_commands = NewModel.split(";")
    sql_commands = [command.strip() for command in sql_commands if command.strip()]
    for command in sql_commands:
        query(command)
        
    return True





def ConvertirFecha(fecha):
    fechaobj = datetime.strptime(fecha, "%d/%m/%Y")
    NewFecha = fechaobj.strftime("%Y-%m-%d")
    return NewFecha

def ConverDataTime(fecha):
    fechaobj = datetime.strptime(fecha, "%d/%m/%Y %H:%M")
    NewFecha = fechaobj.strftime("%Y-%m-%d %H:%M:%S")
    return NewFecha