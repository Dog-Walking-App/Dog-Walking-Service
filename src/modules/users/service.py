from ...db.session import session
from .model import User


def find_all():
    users = session.query(User).all()
    return users


def find_one(user_id):
    user = session.query(User).get(user_id)
    return user


def create(name, email):
    user = User(name, email)
    session.add(user)
    session.commit()

    return user
