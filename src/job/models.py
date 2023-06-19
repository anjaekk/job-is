from datetime import datetime
from dateutil.relativedelta import relativedelta

from sqlalchemy import DateTime, Column, String, Integer, Boolean, Text, JSON, Enum
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from src.database.config import Base
from .enums import JobCategoryEnum, JobPostingStatusEnum


class JobPosting(Base):
    __tablename__ = "job_postings"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    category = Column(Enum(JobCategoryEnum), nullable=False)
    
    location = relationship("Location", backref="job_postings")
    location_id = Column(Integer, ForeignKey("locations.id"), nullable=False)

    salary = Column(JSON, nullable=True)
    views = Column(Integer, nullable=False, default=0)
    status = Column(
        Enum(JobPostingStatusEnum), nullable=False, default=JobPostingStatusEnum.PUBLISHED
    )
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    renewaled_at = Column(DateTime, nullable=False, default=datetime.now)
    deadline = Column(
        DateTime(timezone=True), nullable=True, default=lambda: datetime.now() + relativedelta(months=3)
    )
    updated_at = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)



class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    name = Column(String(150))

    parent_id = Column(Integer, ForeignKey("locations.id"), nullable=True)
    parent = relationship("Location", remote_side=[id], backref="children")


class WorkingHours(Base):
    __tablename__ = "working_hours"

    id = Column(Integer, primary_key=True)
    day = Column(String(10), nullable=False)
    start_time = Column(String(10), nullable=False)
    end_time = Column(String(10), nullable=False)

    job_posting = relationship("JobPosting", backref="working_hours")
    job_posting_id = Column(Integer, ForeignKey("job_postings.id"), nullable=True)

    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=func.now())