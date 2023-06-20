import pytest
from flask import Flask
from . import controller


class MockUser:  # pylint: disable=too-few-public-methods
    def __init__(self, user_id, name, email):
        self.id = user_id  # pylint: disable=C0103
        self.name = name
        self.email = email

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }


users = [
    MockUser(1, "Alice", "alice@example.com"),
    MockUser(2, "Bob", "bob@example.com"),
    MockUser(3, "Charlie", "charlie@example.com")
]


# A test client for the controller
@pytest.fixture
def client():
    app = Flask(__name__)

    app.register_blueprint(controller.blueprint)

    return app.test_client()


# Test the get_all function
def test_get_all(client, mocker):  # pylint: disable=W0621
    mocker.patch(__name__ + ".controller.service.find_all", return_value=users)
    response = client.get("/")
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) == len(users)
    for index, item in enumerate(data):
        assert item == users[index].as_dict()


# Test the get_one function with valid id
def test_get_one_valid(client, mocker):  # pylint: disable=W0621
    mocker.patch(__name__ + ".controller.service.find_one",
                 side_effect=lambda id: users[int(id) - 1])
    response = client.get("/1")
    data = response.get_json()
    assert response.status_code == 200
    assert data == users[0].as_dict()


# Test the get_one function with invalid id
def test_get_one_invalid(client, mocker):  # pylint: disable=W0621
    mocker.patch(__name__ + ".controller.service.find_one", return_value=None)
    response = client.get("/4")
    data = response.get_json()
    assert response.status_code == 404
    assert data == {"message": "User not found"}


# Test the create function with valid data
def test_create_valid(client, mocker):  # pylint: disable=W0621
    mocker.patch(__name__ + ".controller.service.create",
                 side_effect=lambda name, email: MockUser(len(users) + 1, name, email))
    response = client.post(
        "/", json={"name": "David", "email": "david@example.com"})
    data = response.get_json()
    assert response.status_code == 201
    assert data["id"] == len(users) + 1
    assert data["name"] == "David"
    assert data["email"] == "david@example.com"


# Test the create function with invalid data
def test_create_invalid(client, mocker):  # pylint: disable=W0621
    mocker.patch(__name__ + ".controller.service.create",
                 side_effect=ValueError("Invalid data"))
    response = client.post("/", json={"name": "", "email": ""})
    data = response.get_json()
    assert response.status_code == 400
    assert data == {
        "message": "Invalid data",
        "error": {
            "email": ["Not a valid email address."],
            "name": ["Shorter than minimum length 1."]
        }
    }
