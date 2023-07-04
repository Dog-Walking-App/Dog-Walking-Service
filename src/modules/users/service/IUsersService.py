from typing import List  # pylint: disable=invalid-name
from abc import ABC, abstractmethod
from ..model import User


class IUsersService(ABC):
    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def find_one(self, user_id: str) -> User | None:
        pass

    @abstractmethod
    def create(self, name: str, email: str) -> User:
        pass
