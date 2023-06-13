import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from ..src.database.config import Base, get_db
from ..src.main import app


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
Session = scoped_session(sessionmaker())


@pytest.fixture(scope="session")
def db():
    engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function", autouse=True)
def session(db):
    db = Session()
    yield db
    db.rollback()


@pytest.fixture(scope="function")
def client(session):
    yield TestClient(app)