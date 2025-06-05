import sys

from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))        # Solucion al problema de importacion de modulos

from services.materia_service import MateriaService
from repositories.materia_repository import MateriaRepository
from models.materia import Materia

from db.session import Db, engine

def main():
    #Db.metadata.create_all(bind=engine)         # crea todas las tablas de cada xml                          

    # Crear solo la tabla de materias
    Materia.__table__.create(bind=engine, checkfirst=True)

    print("Iniciando carga de Materias desde XML")

    service = MateriaService(MateriaRepository())                 # Crea una instancia del servicio `MateriaService`, inyectándole una instancia del repositorio `MateriaRepository`.

    service.cargar_xml('xml_data/materias.xml')                   #llamada al metodo de service

    print("PERSISTENCIA COMPLETADA.")



if __name__ == '__main__':
    main()
