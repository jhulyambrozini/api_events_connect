from src.model.repositories.interfaces.eventos_repository import EventosRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventsCreator:
    def __init__(self, events_repo: EventosRepositoryInterface):
        self.__events_repo = events_repo
    
    def create(self, http_request: HttpRequest) -> HttpResponse:
        events_info = http_request.body["data"]
        self.__check_events(events_info['name'])
        self.__insert_event(events_info['name'])
        return self.__format_response(events_info['name'])

    def __check_events(self, event_name: str) -> None:
        response = self.__events_repo.select_by_name(event_name)
        if response:
            raise Exception('Event already exists')
        
    def __insert_event(self, event_name: str) -> None:
        self.__events_repo.insert(event_name)

    def __format_response(self, event_name: str) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "Event",
                    "count": 1,
                    "attributes": {
                        "event_name": event_name
                    }
                }
            },
            status_code=201,
        )
