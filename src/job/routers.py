from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import desc
from fastapi_pagination import Page, paginate

from src.database.config import get_db
from .models import JobPosting
from .schemas import (
    JobPostingSchema, 
    CreateJobPostingSchema
)
from .enums import JobPostingStatusEnum


job_routers = APIRouter()


@job_routers.get("", response_model=Page[JobPostingSchema])
async def get_jobs(
    db: Session = Depends(get_db)
):
    """Get all job posts."""
    return paginate(
        db.query(JobPosting).filter(
            JobPosting.status == JobPostingStatusEnum.PUBLISHED
        ).order_by(desc(JobPosting.created_at)).all()
    )


@job_routers.post("", response_model=JobPostingSchema)
async def create_job(
    job_post: CreateJobPostingSchema,
    db: Session = Depends(get_db)
):
    """Create a job post."""
    new_job_post = JobPosting(**job_post.dict())

    db.add(new_job_post)
    db.commit()
    db.refresh(new_job_post)
    return new_job_post