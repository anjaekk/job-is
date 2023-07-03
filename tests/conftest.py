import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as AlembicConfig

from src.database.config import Base, get_db
from src.main import app
from .session import Session, engine
from .factories import (
    LocationFactory, 
    JobPostingFactory,
    ResumePostingFactory,
)


@pytest.fixture(scope="session")
def db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function", autouse=True)
def session(db):
    session = Session()
    yield session
    session.rollback()
    session.close()


@pytest.fixture
def location(session: Session):
    LocationFactory(name="강남구", parent_id=1)
    return LocationFactory()


@pytest.fixture
def job_posting(session: Session):
    return JobPostingFactory.create_batch(10)


@pytest.fixture
def resume_posting(session: Session):
    return ResumePostingFactory.create_batch(10)