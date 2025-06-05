from dataclasses import dataclass       #decorador
from db.session import Db               #importo la clase declarativa para usar sqlalchemy en la definicion de tablas
import sqlalchemy as sa                 #importa sqlalchemy con alias sa. No carga todas las funciones, solo las que voy a usar y voy declarando 


@dataclass(init=False, repr=True, eq=True)

class Especialidad(Db):
    __tablename__= 'especialidades'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=False)
    nombre = sa.Column(sa.String(length=100), nullable=True)          