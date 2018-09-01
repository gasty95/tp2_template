from database import Database
from models import Samples
from sqlalchemy import func

import random
import time
import signal
import sys

class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True


def main(session,t):
    killer = GracefulKiller()
    while(1):
        t.temperature += random.randint(-3,3) #Modifica el valor de la ultima muestra tomada
        t.humidity += random.randint(-3,3)
        t.pressure += random.randint(-3,3)
        t.windspeed += random.randint(-3,3)
        #cant = session.query(func.count(Samples.id)) #Busca la ultima muestra tomada
        sample = Samples(temperature=t.temperature, pressure=t.pressure, humidity=t.humidity, windspeed=t.windspeed) #Crea una nueva fila en la base de datos con la nueva muestra
        session.add(sample)
        session.commit()
        #print(" Temperatura: %s | Humedad: %s | Presion: %s | Velocidad del viento: %s" % (t.temperature, t.humidity, t.pressure, t.windspeed))
        time.sleep(10)  #Lo puse cada 10 para que no genere tantos valores y poder debugearlo mejor
        if killer.kill_now:
            session.close()
            break

if __name__ == '__main__':   
    db = Database()
    session = db.get_session()
    cant = session.query(func.count(Samples.id)) #Busca la ultima muestra tomada
    t = session.query(Samples).filter_by(id = cant).first() # selecciona la ultima muestra tomada y la guarda en t
    main(session,t)
    