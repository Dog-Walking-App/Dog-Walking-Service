from typing import List


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


class UsersServiceMock:
    def __init__(self):
        self.users = [
            MockUser(1, "Alice", "alice@example.com"),
            MockUser(2, "Bob", "bob@example.com"),
            MockUser(3, "Charlie", "charlie@example.com")
        ]

    def find_all(self) -> List[MockUser]:
        return self.users

    def find_one(self, user_id) -> MockUser:
        try:
            return self.users[int(user_id) - 1]
        except IndexError:
            return None

    def create(self, name, email) -> MockUser:
        return MockUser(len(self.users) + 1, name, email)
