from typing import List
from abc import ABC, abstractmethod


class IUser(ABC):
    id: int
    name: str
    email: str

    @abstractmethod
    def __init__(self, name: str, email: str) -> None:
        pass

    @abstractmethod
    def as_dict(self):
        pass


class IUsersService(ABC):
    @abstractmethod
    def find_all(self) -> List[IUser]:
        pass

    @abstractmethod
    def find_one(self, user_id: str) -> IUser | None:
        pass

    @abstractmethod
    def create(self, name: str, email: str) -> IUser:
        pass
