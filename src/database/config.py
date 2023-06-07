from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from envs import config


DB_URL = f"mysql+pymysql://{config.DATABASE_URL}"

Base = declarative_base()

engine = create_async_engine(DB_URL, echo=True)

SessionLocal = sessionmaker(class_=AsyncSession, expire_on_commit=False, bind=engine)