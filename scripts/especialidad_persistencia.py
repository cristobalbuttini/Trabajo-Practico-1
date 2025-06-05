import sys

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))        # Solucion al problema de importacion de modulos

from services.especialidad_service import EspecialidadService
from repositories.especialidad_repository import EspecialidadRepository
from models.especialidad import Especialidad

from db.session import Db, engine

def main():
    #Db.metadata.create_all(bind=engine) # crea todas las tablas de cada xml                             #crea la tabla si no existe

    # Crear solo la tabla de especialidad
    Especialidad.__table__.create(bind=engine, checkfirst=True)

    print("Iniciando carga de especialidades desde XML")                 

    service = EspecialidadService(EspecialidadRepository())                 # Crea una instancia del servicio `FacultadService`, inyectándole una instancia del repositorio `FacultadRepository`.
    
    service.cargar_xml('xml_data/especialidades.xml')                   #llamada al metodo de service
    
    print("PERSISTENCIA COMPLETADA.")



if __name__ == '__main__':
    main()
