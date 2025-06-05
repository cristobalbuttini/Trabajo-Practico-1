from models import Orientacion
from db.session import SessionLocal  # Sesión configurada con SQLAlchemy


class OrientacionRepository:
    def __init__(self):
        # Crea una nueva sesión de base de datos para cada instancia del repositorio
        self.session = SessionLocal()

    def persistir(self, orientacion: Orientacion):
        try:
            self.session.add(orientacion)        # Agrega la entidad a la sesión
            self.session.commit()                 # Realiza commit en la base de datos
        except Exception as e:
            self.session.rollback()               # Revierte en caso de error
            raise e
        finally:
            self.session.close()                  # Cierra la sesión al finalizar
