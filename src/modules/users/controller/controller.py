from marshmallow import Schema, fields, validate
from ....utils.validate_json import validate_json
from ..service.service import IUsersService
from ....http import Http, Controller


class UserSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)


class UsersController(Controller):
    def __init__(
        self,
        http: Http,
        service: IUsersService,
    ):
        super().__init__(http)
        self.service = service

    def get_all(self):
        users = self.service.find_all()

        users_dict = [user.as_dict() for user in users]
        return self.response.send(users_dict)

    def get_one(self, user_id):
        user = self.service.find_one(user_id)
        if user is None:
            return self.response.send(message="User not found", status_code=404)

        user_dict = user.as_dict()
        return self.response.send(user_dict)

    @validate_json(UserSchema())
    def create(self):
        data = self.request.get_json()
        user = self.service.create(data["name"], data["email"])

        user_dict = user.as_dict()
        return self.response.send(user_dict, status_code=201)
