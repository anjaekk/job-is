import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional

from .enums import JobTypeEnum, CountryEnum


class ResumePostingSchema(BaseModel):
    title: str = Field(..., max_length=255)
    content: str = Field(...)
    job_type: JobTypeEnum = Field(...)
    nationality: CountryEnum = CountryEnum.UNKNOWN
    visa: Optional[str]
    contact: str = Field(...)
    views: int = Field(..., ge=0)
    created_at: datetime.datetime = Field(...)
    updated_at: datetime.datetime = Field(...)
    deleted_at: Optional[datetime.datetime] = Field(...)
    is_deleted: bool = Field(...)
    
    @validator("job_type")
    def validate_job_type(cls, value):
        if value not in JobTypeEnum:
            raise ValueError("Invalid job_type: Value is not in JobTypeEnum.")
        return value
    
    @validator("nationality")
    def validate_nationality(cls, value):
        if value not in CountryEnum:
            raise ValueError("Invalid nationaity: Value is not in CountryEnum.")

    class Config:
        orm_mode = True


class CreateResumePostingSchema(BaseModel):
    title: str = Field(..., max_length=255)
    content: str = Field(...)
    job_type: JobTypeEnum = Field(...)
    nationality: Optional[CountryEnum] = CountryEnum.UNKNOWN
    visa: Optional[str]  = None
    contact: str = Field(...)

    class Config:
        orm_mode = True
