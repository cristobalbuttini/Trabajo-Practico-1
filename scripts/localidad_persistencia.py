import sys

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))        # Solucion al problema de importacion de modulos

from services.localidad_service import LocalidadService
from repositories.localidad_repository import LocalidadRepository
from models.localidad import Localidad

from db.session import Db, engine

def main():
    #Db.metadata.create_all(bind=engine)         # crea todas las tablas de cada xml                          

    # Crear solo la tabla de localidades
    Localidad.__table__.create(bind=engine, checkfirst=True)



    print("Iniciando carga de Localidades desde XML")

    service = LocalidadService(LocalidadRepository())                 # Crea una instancia del servicio `LocalidadService`, inyectándole una instancia del repositorio `LocalidadRepository`.

    service.cargar_xml('xml_data/localidades.xml')                   #llamada al metodo de service

    print("PERSISTENCIA COMPLETADA.")



if __name__ == '__main__':
    main()
