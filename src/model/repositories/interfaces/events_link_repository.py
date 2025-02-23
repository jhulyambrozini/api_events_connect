from abc import ABC, abstractmethod
from src.model.entities.events_link import EventsLink

class EventLinkRepositoryInterfaces(ABC):
    @abstractmethod
    def insert(sel, event_id: int, subscriber_id: int) -> str: pass
     
    @abstractmethod
    def select_events_link(self, event_id: int, subscriber_id: int) -> EventsLink: pass
        
