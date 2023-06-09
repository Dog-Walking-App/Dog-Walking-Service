from sqlalchemy import Column, Integer, String
from ...db.engine import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
