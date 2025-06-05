import sys

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))        # Solucion al problema de importacion de modulos

from services.grado_service import GradoService
from repositories.grado_repository import GradoRepository
from models.grado import Grado

from db.session import Db, engine

def main():
    #Db.metadata.create_all(bind=engine)         # crea todas las tablas de cada xml                          
    
    # Crear solo la tabla de grados 
    Grado.__table__.create(bind=engine, checkfirst=True)



    print("Iniciando carga de Grados desde XML")                 

    service = GradoService(GradoRepository())                 # Crea una instancia del servicio `GradoService`, inyectándole una instancia del repositorio `GradoRepository`.
    
    service.cargar_xml('xml_data/grados.xml')                   #llamada al metodo de service
    
    print("PERSISTENCIA COMPLETADA.")



if __name__ == '__main__':
    main()
