from src.model.entities.events import Eventos
from abc import ABC, abstractmethod

class EventosRepositoryInterface(ABC):
    @abstractmethod
    def insert(sel, event_name: str) -> None: pass

    @abstractmethod
    def select_by_name(self, event_name: str) -> Eventos: pass
