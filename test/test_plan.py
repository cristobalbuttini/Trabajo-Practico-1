import unittest
from repositories.plan_repository import PlanRepository
from services.plan_service import PlanService   

from db.session import Db
from db.session import engine


class TestPlanService(unittest.TestCase):

    def tearDown(self):
        Db.metadata.drop_all(bind=engine)    #borra las tablas despues de cada test
    
    def test_service_carga(self):
        # Instancia el repositorio real
        repo = PlanRepository()

        # Instancia el service pasándole el repositorio
        service = PlanService(repo)

        try:
            # Intenta cargar datos desde el XML real
            service.cargar_xml('xml_data/planes.xml')
        except Exception as e:
            self.fail(f"El método cargar_xml lanzó una excepción: {e}")

if __name__ == '__main__':
    unittest.main()
