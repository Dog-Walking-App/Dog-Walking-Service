from marshmallow import Schema, ValidationError


def validate_json(schema: Schema):
    def decorator(function):
        def wrapper(self, *args, **kwargs):
            raw_data = self.request.get_json()

            try:
                schema.load(raw_data)
                return function(self, *args, **kwargs)
            except ValidationError as error:
                return self.response.send(
                    message="Invalid data",
                    error=error.messages,
                    status_code=400,
                )
        wrapper.__name__ = function.__name__
        return wrapper
    return decorator
