import unittest
from repositories.pais_repository import PaisRepository
from services.pais_service import PaisService

from db.session import Db
from db.session import engine


class TestPaisService(unittest.TestCase):

    def tearDown(self):
        Db.metadata.drop_all(bind=engine)    #borra las tablas despues de cada test
    
    def test_service_carga(self):
        # Instancia el repositorio real
        repo = PaisRepository()

        # Instancia el service pasándole el repositorio
        service = PaisService(repo)

        try:
            # Intenta cargar datos desde el XML real
            service.cargar_xml('xml_data/paises.xml')
        except Exception as e:
            self.fail(f"El método cargar_xml lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()
