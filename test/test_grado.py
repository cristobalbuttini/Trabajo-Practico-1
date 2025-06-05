import unittest
from repositories.grado_repository import GradoRepository
from services.grado_service import GradoService

from db.session import Db
from db.session import engine


class TestGradoService(unittest.TestCase):

    def tearDown(self):
        Db.metadata.drop_all(bind=engine)    #borra las tablas despues de cada test
    
    def test_service_carga(self):
        # Instancia el repositorio real
        repo = GradoRepository()

        # Instancia el service pasándole el repositorio
        service = GradoService(repo)

        try:
            # Intenta cargar datos desde el XML real
            service.cargar_xml('xml_data/grados.xml')
        except Exception as e:
            self.fail(f"El método cargar_xml lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()
