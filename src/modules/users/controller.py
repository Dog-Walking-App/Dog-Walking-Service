from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, validate
from ...utils.validate_json import validate_json
from . import service

blueprint = Blueprint("users", __name__)


@blueprint.route("/")
def get_all():
    users = service.find_all()

    users_dict = [user.as_dict() for user in users]
    return jsonify(users_dict)


@blueprint.route("/<user_id>")
def get_one(user_id):
    user = service.find_one(user_id)
    if user is None:
        return jsonify(message="User not found"), 404

    user_dict = user.as_dict()
    return jsonify(user_dict)


class UserSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)


@blueprint.route("/", methods=["POST"])
@validate_json(UserSchema())
def create():
    data = request.get_json()
    user = service.create(data["name"], data["email"])

    user_dict = user.as_dict()
    return jsonify(user_dict), 201
