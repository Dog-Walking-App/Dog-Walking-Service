from flask import request, jsonify
from marshmallow import Schema, ValidationError


def validate_json(schema: Schema):
    def decorator(function):
        def wrapper(*args, **kwargs):
            raw_data = request.get_json()

            try:
                schema.load(raw_data)
                return function(*args, **kwargs)
            except ValidationError as error:
                return jsonify(message="Invalid data", error=error.messages), 400
        return wrapper
    return decorator
