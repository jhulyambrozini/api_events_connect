from src.model.repositories.interfaces.inscritos_repository import InscritosRepositoryInterface
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscribersCreator:
    def __init__(self, subs_repo: InscritosRepositoryInterface):
        self.__subs_repo = subs_repo
    
    def create(self, http_request: HttpRequest) -> HttpResponse:
        subs_info = http_request.body["data"]
        subs_email = subs_info["email"]
        subs_evento_id = subs_info["evento_id"]

        self.__check_subscriber(subs_email, subs_evento_id)
        self.__insert_sub(subs_info)
        return self.__format_response(subs_info)

    def __check_subscriber(self, email: str, evento_id: int) -> None:
        response = self.__subs_repo.select_subscriber(email, evento_id)
        if response:
            raise Exception('Inscrição já realizada com email '+email)

    def __insert_sub(self, subscriber_infos: dict) -> None:
        self.__subs_repo.insert(subscriber_infos)

    def __format_response(self, subscriber_infos: dict) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "Subscriber",
                    "count": 1,
                    "attributes": subscriber_infos
                }
            },
            status_code=201,
       )
        