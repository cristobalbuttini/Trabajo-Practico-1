import unittest
from repositories.universidad_repository import UniversidadRepository
from services.universidad_service import UniversidadService

from db.session import Db
from db.session import engine


class TestUniversidadService(unittest.TestCase):

    def tearDown(self):
        Db.metadata.drop_all(bind=engine)    #borra las tablas despues de cada test
    
    def test_service_carga(self):
        # Instancia el repositorio real
        repo = UniversidadRepository()

        # Instancia el service pasándole el repositorio
        service = UniversidadService(repo)

        try:
            # Intenta cargar datos desde el XML real
            service.cargar_xml('xml_data/universidad.xml')
        except Exception as e:
            self.fail(f"El método cargar_xml lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()
