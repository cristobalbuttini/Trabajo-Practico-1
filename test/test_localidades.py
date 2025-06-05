import unittest
from repositories.localidad_repository import LocalidadRepository
from services.localidad_service import LocalidadService

from db.session import Db
from db.session import engine


class TestLocalidadService(unittest.TestCase):

    def tearDown(self):
        Db.metadata.drop_all(bind=engine)    #borra las tablas despues de cada test
    
    def test_service_carga(self):
        # Instancia el repositorio real
        repo = LocalidadRepository()

        # Instancia el service pasándole el repositorio
        service = LocalidadService(repo)

        try:
            # Intenta cargar datos desde el XML real
            service.cargar_xml('xml_data/localidades.xml')
        except Exception as e:
            self.fail(f"El método cargar_xml lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()
