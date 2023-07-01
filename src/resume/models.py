from datetime import datetime

from sqlalchemy import DateTime, Column, String, Integer, Boolean, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.config import Base
from .enums import CountryEnum, JobTypeEnum


class ResumePosting(Base):
    __tablename__ = "resume_postings"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    job_type = Column(Enum(JobTypeEnum))
    nationality = Column(Enum(CountryEnum), default=CountryEnum.UNKNOWN)
    visa = Column(String(50), nullable=True)
    contact = Column(String(50), nullable=False)
    views = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    is_deleted = Column(Boolean, nullable=False, default=False)