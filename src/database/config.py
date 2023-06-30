from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from ..envs import config


Base = declarative_base()

engine = create_engine(config.DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()