import datetime
from typing import Any, ForwardRef, List, Optional

from pydantic import BaseModel, Field, validator

from .enums import JobCategoryEnum, JobPostingStatusEnum


class LocationSchema(BaseModel):
    id: int
    name: str
    parent_id: Optional[int] = None
    children: List[Any] = []

    class Config:
        orm_mode = True


class JobPostingSchema(BaseModel):
    title: str
    content: str
    catetory: JobCategoryEnum
    location: LocationSchema
    salary: Optional[dict]
    views: int
    status: JobPostingStatusEnum
    created_at: datetime.datetime
    renewaled_at: datetime.datetime
    deadline: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: Optional[datetime.datetime]

    @validator("status")
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