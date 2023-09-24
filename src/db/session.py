from sqlalchemy.orm import sessionmaker
from . import engine

from ..modules.users.model import User  # pylint: disable=W0611

engine.Base.metadata.create_all(engine.engine)

Session = sessionmaker(bind=engine.engine)
session = Session()
