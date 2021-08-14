from typing import Any, Union

from sqlalchemy import create_engine
from sqlalchemy.engine.mock import MockConnection
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.future import Engine
from sqlalchemy.orm import sessionmaker

# CONNECTION STRING -- SQLLITE
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# CONNECTION STRING -- POSTGRES
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# CONNECTION STRING - MYSQL
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://stud:sai1ram2@192.168.68.115:33061/stud"

#ENGINE FOR SQLLITE
#engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

#ENGINE FOR OTHER DATABASEES
engine: Union[Union[MockConnection, Engine], Any] = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
