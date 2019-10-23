from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/listarSensores', methods = ['GET'])
def listarSensores():
    sensores_list = requests.get('http://127.0.0.1:5000/tipoSensores').json()
    return render_template('listarSensores.html', sensores=sensores_list)

@app.route('/crearSensores', methods = ['GET'])
def crearSensores():
    return render_template('crearSensor.html')

@app.route('/guardarSensores', methods = ['POST'])
def guardarSensores():
    sensor = {
        "fecha":str(request.form['fecha']),
        "origen":str(request.form['origen']),
        "valor":str(request.form['valor']),
        "codigoSensor":str(request.form['codigoSensor']),
        "observacion":str(request.form['observacion'])
    }
    print(sensor)
    requests.post('http://127.0.0.1:5000/tipoSensores', json=sensor)
    return render_template('crearSensor.html')

app.run(port=8000, debug=True)
