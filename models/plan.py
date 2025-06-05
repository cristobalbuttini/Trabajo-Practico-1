from dataclasses import dataclass       #decorador
from db.session import Db               #importo la clase declarativa para usar sqlalchemy en la definicion de tablas
import sqlalchemy as sa                 #importa sqlalchemy con alias sa. No carga todas las funciones, solo las que voy a usar y voy declarando 


@dataclass(init=False, repr=True, eq=True)

class Plan(Db):
    __tablename__= 'planes'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)  # El ID es autoincremntal (me parece que queda mas claro que usar los valores del xml que no estan en orden)
    
    especialidad = sa.Column(sa.Integer, nullable=True)
    plan = sa.Column(sa.Integer, nullable=True)
    nombre = sa.Column(sa.String(length=200), nullable=True)
      