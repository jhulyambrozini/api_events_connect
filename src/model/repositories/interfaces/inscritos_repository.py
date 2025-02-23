from abc import ABC, abstractmethod
from src.model.entities.inscritos import Inscritos

class InscritosRepositoryInterface(ABC):
    @abstractmethod
    def insert(sel, subscriber_infos: dict) -> None: pass

    @abstractmethod
    def select_subscriber(self, email: str, evento_id: int) -> Inscritos: pass