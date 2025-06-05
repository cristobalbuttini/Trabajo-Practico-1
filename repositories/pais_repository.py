from models import Pais
from db.session import SessionLocal  # Sesión configurada con SQLAlchemy


class PaisRepository:
    def __init__(self):
        # Crea una nueva sesión de base de datos para cada instancia del repositorio
        self.session = SessionLocal()

    def persistir(self, pais: Pais):
        try:
            self.session.add(pais)        # Agrega la entidad a la sesión
            self.session.commit()                 # Realiza commit en la base de datos
        except Exception as e:
            self.session.rollback()               # Revierte en caso de error
            raise e
        finally:
            self.session.close()                  # Cierra la sesión al finalizar
