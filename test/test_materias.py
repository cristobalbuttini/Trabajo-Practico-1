import unittest
from repositories.materia_repository import MateriaRepository
from services.materia_service import MateriaService

from db.session import Db
from db.session import engine


class TestMateriaService(unittest.TestCase):

    def tearDown(self):
        Db.metadata.drop_all(bind=engine)    #borra las tablas despues de cada test
    
    def test_service_carga(self):
        # Instancia el repositorio real
        repo = MateriaRepository()

        # Instancia el service pasándole el repositorio
        service = MateriaService(repo)

        try:
            # Intenta cargar datos desde el XML real
            service.cargar_xml('xml_data/materias.xml')
        except Exception as e:
            self.fail(f"El método cargar_xml lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()
