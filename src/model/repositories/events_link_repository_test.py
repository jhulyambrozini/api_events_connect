from .events_link_repository import EventLinkRepository
import pytest

@pytest.mark.skip('insert in db')
def test_create_event_link():
    event_id = 1
    subs_id = 4
    event_link_repository = EventLinkRepository()

    event_link_repository.insert(event_id, subs_id)