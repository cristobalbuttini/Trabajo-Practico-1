import sys

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))        # Solucion al problema de importacion de modulos

from services.facultad_service import FacultadService
from repositories.facultad_repository import FacultadRepository
from models.facultad import Facultad 

from db.session import Db, engine

def main():
    #Db.metadata.create_all(bind=engine)         # crea todas las tablas de cada xml                             #crea la tabla si no existe
    
    # Crear solo la tabla de facultades
    Facultad.__table__.create(bind=engine, checkfirst=True)                           

    print("Iniciando carga de facultades desde XML")                 

    service = FacultadService(FacultadRepository())                 # Crea una instancia del servicio `FacultadService`, inyectándole una instancia del repositorio `FacultadRepository`.
    
    service.cargar_xml('xml_data/facultades.xml')                   #llamada al metodo de service
    
    print("PERSISTENCIA COMPLETADA.")



if __name__ == '__main__':
    main()
