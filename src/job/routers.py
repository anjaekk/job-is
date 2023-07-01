from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session
from sqlalchemy import desc

from src.database.config import get_db
from .schemas import (
    JobPostingSchema, 
    CreateJobPostingSchema,
    UpdateJobPostingSchema, 
)
from .services import (
    service_get_list_jobs,
    service_get_job_by_id,
    service_create_job,
    service_update_job_by_id,
    service_delete_job_by_id
)


job_routers = APIRouter()


@job_routers.get("", response_model=Page[JobPostingSchema])
async def get_jobs(
    db: Session = Depends(get_db)
):
    """Get job posts."""
    jobs = await service_get_list_jobs(db)
    return paginate(jobs)


@job_routers.get("/{job_id}", response_model=JobPostingSchema)
async def get_job(
    job_id: int,
    db: Session = Depends(get_db)
):
    """Get a job post."""
    return await service_get_job_by_id(job_id, db)


@job_routers.post("", response_model=JobPostingSchema)
async def create_job(
    job_post: CreateJobPostingSchema,
    db: Session = Depends(get_db)
):
    """Create a job post."""
    return await service_create_job(job_post, db)


@job_routers.put("/{job_id}", response_model=JobPostingSchema)
async def update_job(
    job_id: int,
    job_post: UpdateJobPostingSchema,
    db: Session = Depends(get_db)
):
    """Update a job post."""
    return await service_update_job_by_id(job_id, job_post, db)


@job_routers.delete("/{job_id}")
async def delete_job(
    job_id: int,
    db: Session = Depends(get_db)
):
    """Delete a job post."""
    return await service_delete_job_by_id(job_id, db)