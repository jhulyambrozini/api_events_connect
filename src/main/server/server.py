from flask import Flask
from src.main.routes.events import event_route_bp

app = Flask(__name__)
app.register_blueprint(event_route_bp)