# Imports
from aux_pro import Process
from database import Database
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from models import Samples
import datetime
import os
  
app = Flask(__name__)
db = Database()
pro = Process()

# Define the route to enter in the browser
@app.route('/')
def index():
    return render_template('index.html') #simplemente redirecciona a index.

@app.route('/samples', methods = ["POST"]) #Obtiene de la base de datos un nuevo sample, tambien se le pasa una frecuencia desde el index. Devuelve a samples, el id del nuevo sample y tambien la frecuencia seleccionada en el index.
def start():
    
    if pro.is_running():
      return index()
    data= request.form
    d_m= data["frec"]
    id_sample = db.init_start() #proceso en database.py que devuelve un id
    pro.start_process() #proceso en aux_pro para comenzar el proceso
    return render_template('samples.html', id_sample=id_sample, frec= d_m)

@app.route('/samples/<id_sample>', methods = ["GET"]) #Obtiene un sample especifico (con un id que le fue pasado como parametro)
def get_sample(id_sample):
    sample = db.get_sample(id_sample) #proceso en database.py que devuelve un sample
    return jsonify(sample)  

@app.route('/samples/stop/<id_sample>', methods = ["GET"]) #detiene el proceso de obtencion de datos, una vez hecho esto vuelve al index
def stop_sample(id_sample):
    data = pro.stop_process() #proceso en aux_pro para detener el proceso
    return render_template('index.html', id_sample=id_sample)

@app.route('/promedios', methods = ["POST"]) #Obtiene el promedio de las ultimas 10 mediciones.
def average():
    avg = db.get_average() #proceso que se encarga de obtener los promedios en database.py
    return render_template('promedios.html', avg=avg)  #devuelve los promedios a promedios.html


if __name__ == "__main__":
    # Define HOST and port
    app.run(host='0.0.0.0', port=8888)


