from flask import Blueprint
from ...db.session import session
from .service.service import UsersService
from .controller.controller import UsersController, http_service
from ...http import Http, Request, Response


service = UsersService(session)
http = Http(Request(), Response())
controller = UsersController(http, service)

blueprint = Blueprint("users", __name__)
http_service.build(blueprint, controller)
