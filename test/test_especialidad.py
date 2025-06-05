import unittest
from repositories.especialidad_repository import EspecialidadRepository
from services.especialidad_service import EspecialidadService


from db.session import Db
from db.session import engine


class TestEspecialidadService(unittest.TestCase):

    def tearDown(self):
        Db.metadata.drop_all(bind=engine)    #borra las tablas despues de cada test
    
    def test_service_carga(self):
        # Instancia el repositorio real
        repo = EspecialidadRepository()

        # Instancia el service pasándole el repositorio
        service = EspecialidadService(repo)

        try:
            # Intenta cargar datos desde el XML real
            service.cargar_xml('xml_data/especialidades.xml')
        except Exception as e:
            self.fail(f"El método cargar_xml lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()
