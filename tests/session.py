from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
Session = scoped_session(sessionmaker(bind=engine))