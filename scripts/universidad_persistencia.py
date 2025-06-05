import sys

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))        # Solucion al problema de importacion de modulos

from services.universidad_service import UniversidadService
from repositories.universidad_repository import UniversidadRepository
from models.universidad import Universidad

from db.session import Db, engine

def main():
    #Db.metadata.create_all(bind=engine)         # crea todas las tablas de cada xml                          

    # Crear solo la tabla de universidades
    Universidad.__table__.create(bind=engine, checkfirst=True)

    print("Iniciando carga de Universidades desde XML")

    service = UniversidadService(UniversidadRepository())                 # Crea una instancia del servicio `UniversidadService`, inyectándole una instancia del repositorio `UniversidadRepository`.

    service.cargar_xml('xml_data/universidad.xml')                   #llamada al metodo de service

    print("PERSISTENCIA COMPLETADA.")



if __name__ == '__main__':
    main()
