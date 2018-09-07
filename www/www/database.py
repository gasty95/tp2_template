from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import Samples
from sqlalchemy import func
from sqlalchemy import and_
import os

class Database(object):
    session = None
    db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "root"
    db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "root"
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "db"
    db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "samples"
    db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"
    Base = declarative_base()
    
    def get_session(self):
        """Singleton of db connection
        Returns:
            [db connection] -- [Singleton of db connection]
        """
        if self.session == None:
            connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
            engine = create_engine(connection)
            connection = engine.connect()
            Session = sessionmaker(bind=engine)
            self.session = Session()
            self.Base.metadata.create_all(engine)
        return self.session

    def init_start(self): #Inicializa los valores de un sample que luego seran modificados en el py y los guarda en la base de datos. Además devuelve el Id.
        session = self.get_session()
        sample = Samples(temperature=22, pressure=1013, humidity=50, windspeed=10)
        session.add(sample)
        session.commit()
        sample_id = int(sample.id)
        session.close()     
        return sample_id


    def get_sample(self,id_sample): #Obtiene el sample del id pasado por parametro y lo devuelve con sus valores
        session = self.get_session()
        samples = session.query(Samples).filter_by(id = id_sample).first() # selecciona la ultima muestra tomada y la guarda en t
        session.close()
        sample = {
                    'temperature': samples.temperature,
                    'humidity': samples.humidity,
                    'pressure': samples.pressure,
                    'windspeed': samples.windspeed,
                }        
        return sample

    def get_average(self): #devuelve el promedio de los ultimos 10 samples (las ultimas 10 mediciones)
        session = self.get_session()
        cant = session.query(func.count(Samples.id)).scalar()
        total= session.query(Samples).first()
        total.temperature=0
        total.humidity=0
        total.pressure=0
        total.windspeed=0
        total.id=cant-1
        s=session.query(Samples).\
        filter(Samples.id > -10, Samples.id <= cant)
        session.close()
        aux=0
        while(aux<10):
            total.temperature = total.temperature + s[aux].temperature
            total.humidity = total.humidity + s[aux].humidity
            total.pressure = total.pressure + s[aux].pressure
            total.windspeed = total.windspeed + s[aux].windspeed
            aux=aux+1
        total.temperature = total.temperature/10
        total.humidity = total.humidity/10
        total.pressure = total.pressure/10
        total.windspeed = total.windspeed/10
        print(" Promedios Temperatura: %s | Humedad: %s | Presion: %s | Velocidad del viento: %s" % (total.temperature, total.humidity, total.pressure, total.windspeed))
        
        return total