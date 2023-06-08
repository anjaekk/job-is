from datetime import datetime

from sqlalchemy import DateTime, Column, String, Integer, Boolean, Text, Enum
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from ..database.config import Base
from post.enums import CountryEnum


class JobPosting(Base):
    __tablename__ = "job_postings"

    id = Column(Integer, primary_key=True)
    title = Column(String(256), nullable=False)
    content = Column(Text, nullable=False)
    
    location = relationship("Location", backref="job_postings")
    location_id = Column(Integer, ForeignKey("location.id"), nullable=False)
    
    salary_month = Column(Integer, nullable=True)
    salary_year = Column(Integer, nullable=True)
    views = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)
    deleted_at = Column(DateTime, nullable=True)
    is_deleted = Column(Boolean, nullable=False, default=False)


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    name = Column(String(150))

    parent = relationship("Location", remote_side=[id])
    parent_id = Column(Integer, ForeignKey("locations.id"), nullable=True)


class WorkingHours(Base):
    __tablename__ = "working_hours"

    id = Column(Integer, primary_key=True)
    day = Column(String(10), nullable=False)
    start_time = Column(String(10), nullable=False)
    end_time = Column(String(10), nullable=False)

    job_posting = relationship("JobPosting", backref="working_hours")
    job_posting_id = Column(Integer, ForeignKey("job_postings.id"), nullable=True)

    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)


class JobSeekerPostings(Base):
    __tablename__ = "job_seeker_postings"

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