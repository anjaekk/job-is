from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.config import get_db
from .models import JobPosting
from .schemas import JobPostingSchema
from .enums import JobPostingStatusEnum


job_routers = APIRouter()


@job_routers.get("", response_model=list[JobPostingSchema])
async def get_jobs(
    db: Session = Depends(get_db)
):
    """Get all job posts."""
    return db.query(JobPosting).filter(
        JobPosting.status == JobPostingStatusEnum.PUBLISHED
    ).all()