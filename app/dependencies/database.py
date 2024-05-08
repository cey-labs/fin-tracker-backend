from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Inherit this class to create database models
Base = declarative_base()


class Database:
    def __init__(self, db_url: str):
        self._SQLALCHEMY_DATABASE_URL = db_url
        self._engine = create_engine(self._SQLALCHEMY_DATABASE_URL, )
        # Each instance of SessionLocal is a database session
        self._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

    def get_session(self):
        return self._SessionLocal()

    def get_engine(self):
        return self._engine
