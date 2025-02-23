from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interfaces.inscritos_repository import InscritosRepositoryInterface

class SubscriberManager:
    def __init__(self, subscribers_repo: InscritosRepositoryInterface):
        self.__subs_repo = subscribers_repo
    
    def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpResponse:
        link = http_request.params["link"]
        event_id = http_request.params["event_id"]
        response = self.__subs_repo.select_subscribers_by_link(link, event_id)
        print(response)
        return self.__format_response(response)

    def get_event_ranking(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.params["event_id"]
        response = self.__subs_repo.get_ranking(event_id)
        return self.__format_event_ranking(response)

    def __format_response(self, response: list) -> HttpResponse:
        formattted_subscriber = []
        for sub in response:
            formattted_subscriber.append({
                "email": sub.email,
                "nome": sub.nome,
            })
        return HttpResponse(
            body={
                "data": {
                    "type": "Subscribers",
                    "count": len(response),
                    "attributes": formattted_subscriber
                }
            },
            status_code=200,
        )

    def __format_event_ranking(self, event_raking: list) -> HttpResponse:
        formattted_event_ranking = []
        for position in event_raking:
            formattted_event_ranking.append({
                "link": position.link,
                "total_subscribers": position.total,
            })
        return HttpResponse(
            body={
                "data": {
                    "type": "Ranking",
                    "count": len(event_raking),
                    "attributes": formattted_event_ranking
                }
            },
            status_code=200,
        )