from .eventos_repository import EventosRepository
import pytest

@pytest.mark.skip('insert in db')
def test_insert_events():
    event_name = 'testanto 2'
    event_repository = EventosRepository()

    event_repository.insert(event_name)

def test_select_by_name():
    event_name = 'testanto'
    event_repository = EventosRepository()
    event = event_repository.select_by_name(event_name)
    print(event)
    print(event.nome)
