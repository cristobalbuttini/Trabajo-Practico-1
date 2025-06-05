from sqlalchemy import create_engine                                #importa el constructor del motor de base de datos (funciones para conectar con DB )
from sqlalchemy.orm import sessionmaker, declarative_base           #importa el constructor de sesiones y la clase base declarativa para los modelos de SQLAlchemy  (Herramientas para crear sesiones y definir modelos)
from config.config import get_database_url                                 #importa de config.py el metodo que obtiene la URL de la DB

DATABASE_URL = get_database_url()

engine = create_engine(DATABASE_URL, echo=True)                     #crea el motor de base de datos con la URL obtenida y habilita el modo de depuración (echo=True)
SessionLocal = sessionmaker(bind=engine)                            #prepara un creador de sessiones para que se pueda usar la BD
Db = declarative_base()                                             #crea una clase base declarativa para los modelos de SQLAlchemy
 





#la URL de la base de datos se obtiene mediante un metodos que esta en la configuracion.