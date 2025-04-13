from DB.conexion import Base
from sqlalchemy import Column, Integer, String

class Movie(Base):
    __tablename__ = 'tb_movies'
    id = Column(Integer, primary_key=True, autoincrement="auto")
    titulo = Column(String(200))
    genero = Column(String(50))
    anio = Column(Integer)
    clasificacion = Column(String(20))
    