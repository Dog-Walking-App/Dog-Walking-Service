from unittest.mock import MagicMock
from ..service.mock_service import UsersServiceMock
from .controller import UsersController
from ....http import HttpMock, RequestMock, ResponseMock

service_mock = UsersServiceMock()
request_mock = RequestMock()
response_mock = ResponseMock()
http_mock = HttpMock(request_mock, response_mock)
controller = UsersController(http_mock, service_mock)


# Test the get_all function
def test_get_all():
    response = controller.get_all()
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) == len(service_mock.users)
    for index, item in enumerate(data):
        assert item == service_mock.users[index].as_dict()


# Test the get_one function with valid id
def test_get_one_valid():
    response = controller.get_one("1")
    data = response.get_json()
    assert response.status_code == 200
    assert data == service_mock.users[0].as_dict()


# Test the get_one function with invalid id
def test_get_one_invalid():
    response = controller.get_one("4")
    data = response.get_json()
    assert response.status_code == 404
    assert data == {"message": "User not found"}


# Test the create function with valid data
def test_create_valid():
    request_mock.get_json = MagicMock(
        return_value={"name": "David", "email": "david@example.com"})
    response = controller.create()
    data = response.get_json()
    assert response.status_code == 201
    assert data["id"] == len(service_mock.users) + 1
    assert data["name"] == "David"
    assert data["email"] == "david@example.com"


# Test the create function with invalid data
def test_create_invalid():
    request_mock.get_json = MagicMock(
        return_value={"name": "", "email": ""})
    response = controller.create()
    data = response.get_json()
    assert response.status_code == 400
    assert data == {
        "message": "Invalid data",
        "error": {
            "email": ["Not a valid email address."],
            "name": ["Shorter than minimum length 1."]
        }
    }
