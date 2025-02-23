from src.model.configs.connection import DBConnectionHandler
from src.model.entities.events_link import EventsLink
from src.model.repositories.interfaces.events_link_repository import EventLinkRepositoryInterfaces
import random

class EventLinkRepository(EventLinkRepositoryInterfaces):
    def insert(sel, event_id: int, subscriber_id: int) -> str:
        with DBConnectionHandler() as db:
            try:
                link_final = ''.join(random.choices('0123456789', k=7))
                formated_link = f'evento-{event_id}-{subscriber_id}-{link_final}'
                new_event_link = EventsLink(
                    evento_id=event_id,
                    inscrito_id=subscriber_id,
                    link=formated_link
                )
                db.session.add(new_event_link)
                db.session.commit()
                return formated_link
            except Exception as exception:
                db.session.rollback()
                raise exception
    
    def select_events_link(self, event_id: int, subscriber_id: int) -> EventsLink:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(EventsLink)
                .filter(
                    EventsLink.evento_id == event_id,
                    EventsLink.inscrito_id == subscriber_id
                )
                .one_or_none()
            )
            return data
