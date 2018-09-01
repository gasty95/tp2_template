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
    return render_template('index.html')

@app.route('/samples', methods = ["POST"])
def start():
    
    if pro.is_running():
      return index()
    id_sample = db.init_start()
    pro.start_process()
    return render_template('samples.html', id_sample=id_sample)

@app.route('/samples/<id_sample>', methods = ["GET"])
def get_sample(id_sample):
    sample = db.get_sample(id_sample)
    return jsonify(sample)  



@app.route('/promedios', methods = ["POST"])
def average():
    avg = db.get_average()
    return render_template('promedios.html', avg=avg)  


if __name__ == "__main__":
    # Define HOST and port
    app.run(host='0.0.0.0', port=8888)


