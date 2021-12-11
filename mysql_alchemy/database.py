from typing import Any, Union

from sqlalchemy import create_engine
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import Engine
from sqlalchemy.orm import sessionmaker
from .config import settings

# CONNECTION STRING -- SQLITE
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# CONNECTION STRING -- POSTGRES
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# CONNECTION STRING - MYSQL

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print(SQLALCHEMY_DATABASE_URL)
# ENGINE FOR SQLITE
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# ENGINE FOR OTHER DATABASES
engine: Union[Union[MockConnection, Engine], Any] = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
