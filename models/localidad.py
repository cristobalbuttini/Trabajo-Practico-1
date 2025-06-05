from dataclasses import dataclass       #decorador
from db.session import Db               #importo la clase declarativa para usar sqlalchemy en la definicion de tablas
import sqlalchemy as sa                 #importa sqlalchemy con alias sa. No carga todas las funciones, solo las que voy a usar y voy declarando 


@dataclass(init=False, repr=True, eq=True)

class Localidad(Db):
    __tablename__= 'localidades'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=False)
    ciudad = sa.Column(sa.String(length=200), nullable=True) 
    provincia = sa.Column(sa.String(length=200), nullable=True)
    pais = sa.Column(sa.String(length=200), nullable=True)         