from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from .. import config

engine = create_engine(
    f"postgresql+psycopg2://{config.db_username}:{config.db_password}@{config.db_host}:{config.db_port}/{config.db_name}")  # pylint: disable=C0301

Base = declarative_base()
