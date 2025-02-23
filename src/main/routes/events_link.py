from flask import Blueprint, jsonify, request
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

from src.controllers.events_link.events_link_creator import EventsLinkCreator
from src.model.repositories.events_link_repository import EventLinkRepository

event_link_route_bp = Blueprint("event_link_route", __name__)

@event_link_route_bp.route("/events_links", methods=["POST"])
def create_new_link():
    http_request = HttpRequest(body=request.json)
    events_link_repo = EventLinkRepository()
    events_link_creator = EventsLinkCreator(events_link_repo)

    response = events_link_creator.create(http_request)

    return jsonify(response.body), response.status_code