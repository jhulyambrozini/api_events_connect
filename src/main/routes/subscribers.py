from flask import Blueprint, jsonify, request
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest
from src.validators.subscribers_creator_validator import subscribers_creator_validator 
from src.controllers.subscribers.subscribers_creator import SubscribersCreator
from src.model.repositories.inscritos_repository import InscritosRepository

subscriber_route_bp = Blueprint("subs_route", __name__)

@subscriber_route_bp.route("/subscriber", methods=["POST"])
def create_subscriber():
    subscribers_creator_validator(request)
    http_request = HttpRequest(body=request.json)
    subs_repo = InscritosRepository()
    subscriber_creator = SubscribersCreator(subs_repo)

    response = subscriber_creator.create(http_request)

    return jsonify(response.body), response.status_code