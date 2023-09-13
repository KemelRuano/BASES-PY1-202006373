from collections import OrderedDict
from flask import Flask
import json
from CargarDatos import Carga

app = Flask(__name__)


@app.route('/')
def Root():
    credenciales = OrderedDict()
    credenciales['Nombre'] = 'Kemel Josue Efrain Ruano Jeronimo'
    credenciales['Carnet'] = '202006373'
    credenciales['Curso'] = 'Sistemas de Bases de Datos 1'
    env = json.dumps(credenciales)
    return env

@app.route('/CargaMasiva')
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
    


if __name__ == '__main__':
     app.run(debug=True)

