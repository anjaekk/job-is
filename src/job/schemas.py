import datetime
from typing import Any, ForwardRef, List, Optional, Dict

from pydantic import BaseModel, Field, validator

from .enums import JobCategoryEnum, JobPostingStatusEnum


class LocationSchema(BaseModel):
    id: int
    name: str
    parent_id: Optional[int] = None
    children: List[Any] = None

    class Config:
        orm_mode = True


class JobPostingSchema(BaseModel):
    title: str = Field(..., max_length=255)
    content: str = Field(...)
    category: JobCategoryEnum
    location: LocationSchema
    salary: Optional[dict]
    views: int = Field(..., ge=0)
    status: JobPostingStatusEnum
    created_at: datetime.datetime = Field(...)
    renewaled_at: datetime.datetime = Field(...)
    deadline: datetime.datetime = Field(...)
    updated_at: datetime.datetime = None
    deleted_at: Optional[datetime.datetime]

    @validator("category")
    def validate_category(cls, value):
        if value not in JobCategoryEnum:
            raise ValueError("Invalid category: Value is not in JobCategoryEnum")
        return value

    @validator("status")
    def validate_status(cls, value):
        if value not in JobPostingStatusEnum:
            raise ValueError("Invalid status: Value is not in JobPostingStatusEnum")
        return value
    
    class Config:
        orm_mode = True


class CreateJobPostingSchema(BaseModel):
    title: str = Field(..., max_length=255)
    content: str = Field(...)
    category: JobCategoryEnum = Field(...)
    location_id: int = Field(...)
    salary: Optional[Dict] = Field(...)
    working_hours: Optional[List[Dict[str, Dict[int, int]]]] = []

    @validator("category")
    def validate_category(cls, value):
        if value not in JobCategoryEnum:
            raise ValueError("Invalid category: Value is not in JobCategoryEnum")
        return value

    class Config:
        orm_mode = True


class UpdateJobPostingSchema(BaseModel):
    title: Optional[str] = Field(max_length=255)
    content: Optional[str]
    category: Optional[JobCategoryEnum]
    location_id: Optional[int]
    salary: Optional[Dict]
    working_hours: Optional[List[Dict[str, Dict[int, int]]]] =[]

    @validator("category")
    def validate_category(cls, value):
        if value and value not in JobCategoryEnum:
            raise ValueError("Invalid category: Value is not in JobCategoryEnum")
        return value

    class Config:
        orm_mode = True