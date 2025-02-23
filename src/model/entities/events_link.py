from src.model.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class EventsLink(Base):
    __tablename__ = "eventos_link"

    id = Column(Integer, primary_key=True, autoincrement=True)
    evento_id = Column(Integer, ForeignKey('eventos.id'))
    inscrito_id = Column(Integer, ForeignKey('inscritos.id'))
    link = Column(String, nullable=False)
