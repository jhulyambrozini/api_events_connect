from sqlalchemy import Column, Integer, String
from src.model.configs.base import Base

class Eventos(Base):
    __tablename__ =  'eventos'

    id = Column(Integer, prymary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)