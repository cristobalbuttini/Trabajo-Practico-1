import sys

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))        # Solucion al problema de importacion de modulos

from services.plan_service import PlanService
from repositories.plan_repository import PlanRepository
from models.plan import Plan

from db.session import Db, engine

def main():
    #Db.metadata.create_all(bind=engine)         # crea todas las tablas de cada xml                          

    # Crear solo la tabla de planes
    Plan.__table__.create(bind=engine, checkfirst=True)

    print("Iniciando carga de Planes desde XML")

    service = PlanService(PlanRepository())                 # Crea una instancia del servicio `PlanService`, inyectándole una instancia del repositorio `PlanRepository`.

    service.cargar_xml('xml_data/planes.xml')                   #llamada al metodo de service

    print("PERSISTENCIA COMPLETADA.")



if __name__ == '__main__':
    main()
