from flask import send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from src.app import app


@app.route("/api/spec")
def get_spec():
    return send_from_directory(app.root_path, "documentation/swagger.yaml")


SWAGGER_URL = "/api/docs"
API_URL = "/api/spec"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
)

app.register_blueprint(swaggerui_blueprint)
