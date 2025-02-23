from flask import Blueprint, jsonify, request
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest
from src.validators.events_creator_validator import events_creator_validator 
from src.controllers.events.events_creator import EventsCreator
from src.model.repositories.eventos_repository import EventosRepository

event_route_bp = Blueprint("event_route", __name__)

@event_route_bp.route("/events", methods=["POST"])
def create_event():
    events_creator_validator(request)
    http_request = HttpRequest(body=request.json)
    eventos_repo = EventosRepository()
    events_creator = EventsCreator(eventos_repo)

    response = events_creator.create(http_request)

    return jsonify(response.body), response.status_code