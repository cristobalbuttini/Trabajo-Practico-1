import sys

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))        # Solucion al problema de importacion de modulos

from services.orientacion_service import OrientacionService
from repositories.orientacion_repository import OrientacionRepository
from models.orientacion import Orientacion

from db.session import Db, engine

def main():
    #Db.metadata.create_all(bind=engine)         # crea todas las tablas de cada xml                          

    # Crear solo la tabla de orientaciones
    Orientacion.__table__.create(bind=engine, checkfirst=True)

    print("Iniciando carga de Orientaciones desde XML")

    service = OrientacionService(OrientacionRepository())                 # Crea una instancia del servicio `OrientacionService`, inyectándole una instancia del repositorio `OrientacionRepository`.

    service.cargar_xml('xml_data/orientaciones.xml')                   #llamada al metodo de service

    print("PERSISTENCIA COMPLETADA.")



if __name__ == '__main__':
    main()
