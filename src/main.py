from collections import OrderedDict
from flask import Flask
import json
from CargarDatos import Carga
from Modelo.Consultas import *

app = Flask(__name__)


@app.route('/')
def Root():
    credenciales = OrderedDict()
    credenciales['Nombre'] = 'Kemel Josue Efrain Ruano Jeronimo'
    credenciales['Carnet'] = '202006373'
    credenciales['Curso'] = 'Sistemas de Bases de Datos 1'
    env = json.dumps(credenciales)
    return env

@app.route('/cargartabtemp')
def CargaMasiva():
    resivido = Carga.CargaMasiva("C:\\Users\\LENOVO\\Downloads\\TSEdatasets")
    print(resivido)
    return resivido

@app.route('/crearmodelo')
def CrearModelo():
    is_correct = Carga.GenerateModel()
    env = {}
    if is_correct:
        env = {"status": "Modelo Creado Exitosamente"}
    else:
        env = {"status": "Error al crear el modelo"}
    return json.dumps(env)
    
@app.route('/consulta1')
def  Consulta1():
    return Response1()

@app.route('/consulta2')
def  Consulta2():
    return Response2()

@app.route('/consulta3')
def  Consulta3():
    return Response3()

@app.route('/consulta4')
def  Consulta4():
    return Response4()

@app.route('/consulta5')
def  Consulta5():
    return Response5()

@app.route('/consulta6')
def  Consulta6():
    return Response6()

@app.route('/consulta7')
def  Consulta7():
    return Response7()

@app.route('/consulta8')
def  Consulta8():
    return Response8()

@app.route('/consulta9')
def  Consulta9():
    return Response9()

@app.route('/consulta10')
def  Consulta10():
    return Response10()

@app.route('/consulta11')
def  Consulta11():
    return Response11()

if __name__ == '__main__':
     app.run(debug=True)

