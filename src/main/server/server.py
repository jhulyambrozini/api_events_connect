from flask import Flask
from src.main.routes.events import event_route_bp
from src.main.routes.subscribers import subscriber_route_bp
from src.main.routes.events_link import event_link_route_bp

app = Flask(__name__)
app.register_blueprint(event_route_bp)
app.register_blueprint(subscriber_route_bp)
app.register_blueprint(event_link_route_bp)

