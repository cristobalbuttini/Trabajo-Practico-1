from dotenv import load_dotenv
import os

load_dotenv()    #metodo que carga las variables que defini en .env  En mi .env tengo la  URL de la base de datos

def get_database_url():
    return os.getenv("DEV_DATABASE_URI")
