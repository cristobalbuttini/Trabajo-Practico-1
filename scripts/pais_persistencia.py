import sys

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))        # Solucion al problema de importacion de modulos

from services.pais_service import PaisService
from repositories.pais_repository import PaisRepository
from models.pais import Pais

from db.session import Db, engine

def main():
    #Db.metadata.create_all(bind=engine)         # crea todas las tablas de cada xml                          

    # Crear solo la tabla de paises
    Pais.__table__.create(bind=engine, checkfirst=True)

    print("Iniciando carga de Paises desde XML")

    service = PaisService(PaisRepository())                 # Crea una instancia del servicio `PaisService`, inyectándole una instancia del repositorio `PaisRepository`.

    service.cargar_xml('xml_data/paises.xml')                   #llamada al metodo de service

    print("PERSISTENCIA COMPLETADA.")



if __name__ == '__main__':
    main()
