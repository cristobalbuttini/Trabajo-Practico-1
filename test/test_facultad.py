import unittest
from repositories.facultad_repository import FacultadRepository
from services.facultad_service import FacultadService

from db.session import Db
from db.session import engine


class TestFacultadService(unittest.TestCase):
    
    def tearDown(self):
        Db.metadata.drop_all(bind=engine)    #borra las tablas despues de cada test
    
    def test_service_carga(self):
        # Instancia el repositorio real
        repo = FacultadRepository()

        # Instancia el service pasándole el repositorio
        service = FacultadService(repo)

        try:
            # Intenta cargar datos desde el XML real
            service.cargar_xml('xml_data/facultades.xml')
        except Exception as e:
            self.fail(f"El método cargar_xml lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()
