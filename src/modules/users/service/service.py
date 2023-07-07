from typing import List
from sqlalchemy.orm import Session
from ..model import User
from .IUsersService import IUsersService


class UsersService(IUsersService):
    def __init__(self, session: Session):
        self.session = session

    def find_all(self) -> List[User]:
        users = self.session.query(User).all()
        return users

    def find_one(self, user_id) -> User:
        user = self.session.query(User).get(user_id)
        return user

    def create(self, name, email) -> User:
        user = User(name, email)
        self.session.add(user)
        self.session.commit()

        return user
