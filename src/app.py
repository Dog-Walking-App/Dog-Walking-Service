from flask import Flask
from .modules.routes import register_routes

app = Flask(__name__)

register_routes(app)
