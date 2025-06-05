import unittest
from repositories.orientacion_repository import OrientacionRepository
from services.orientacion_service import OrientacionService

from db.session import Db
from db.session import engine


class TestOrientacionService(unittest.TestCase):

    def tearDown(self):
        Db.metadata.drop_all(bind=engine)    #borra las tablas despues de cada test
    
    def test_service_carga(self):
        # Instancia el repositorio real
        repo = OrientacionRepository()

        # Instancia el service pasándole el repositorio
        service = OrientacionService(repo)

        try:
            # Intenta cargar datos desde el XML real
            service.cargar_xml('xml_data/orientaciones.xml')
        except Exception as e:
            self.fail(f"El método cargar_xml lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()
