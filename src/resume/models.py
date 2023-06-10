from datetime import datetime

from sqlalchemy import DateTime, Column, String, Integer, Boolean, Text, Enum
from sqlalchemy.orm import relationship

from ..database.config import Base
from resume.enums import CountryEnum


class ResumePostings(Base):
    __tablename__ = "resume_postings"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    content = Column(Text, nullable=False)
    job_type = Column(String(10), nullable=False)
    nationality =Column(Enum(CountryEnum), nullable=True)
    visa = Column(String(50), nullable=True)
    contract = Column(String(50), nullable=False)
    views = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)
    deleted_at = Column(DateTime, nullable=True)
    is_deleted = Column(Boolean, nullable=False, default=False)