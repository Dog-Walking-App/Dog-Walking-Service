from flask import Blueprint
from ...db.session import session
from .service.service import UsersService
from .controller.controller import UsersController
from ...http import Http, Request, Response

blueprint = Blueprint("users", __name__)

service = UsersService(session)
http = Http(Request(), Response())
controller = UsersController(http, service)


@blueprint.get("/")
def get_all():
    return controller.get_all()


@blueprint.get("/<user_id>")
def get_one(user_id):
    return controller.get_one(user_id)


@blueprint.post("/")
def create():
    return controller.create()
