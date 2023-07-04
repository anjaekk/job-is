import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import desc

from src.database.config import get_db
from .models import JobPosting, Location
from .schemas import (
    CreateJobPostingSchema,
    UpdateJobPostingSchema
)
from .enums import JobPostingStatusEnum


async def service_get_list_jobs(
    db: Session
):
    return db.query(JobPosting).filter(
        JobPosting.status == JobPostingStatusEnum.PUBLISHED
    ).order_by(desc(JobPosting.created_at)).all()


async def add_job_posting_views(db, job_post):
    job_post.views += 1
    db.commit()
    db.refresh(job_post)


async def service_get_job_by_id(
    job_id: int,
    db: Session
):
    if job_post := db.get(JobPosting, job_id):
        await add_job_posting_views(db, job_post)
        return job_post
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job post not found."
        )


async def generage_location(db: Session, location_id: int):
    if location := db.get(Location, location_id):
        return location
    else:
        raise HTTPException(status_code=404, detail="Location not found")


async def service_create_job(
    job_post: CreateJobPostingSchema,
    db: Session,
):  
    await generage_location(db, job_post.location_id)
    new_job_post = JobPosting(**job_post.dict())

    db.add(new_job_post)
    db.commit()
    db.refresh(new_job_post)
    return new_job_post


async def service_update_job_by_id(
    job_id: int,
    job_post: UpdateJobPostingSchema,
    db: Session
):
    if job := db.get(JobPosting, job_id):
        updated_fields = job_post.dict(exclude_unset=True)
        for field, value in updated_fields.items():
            setattr(job, field, value)
        db.commit()
        db.refresh(job)
        return job
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job post not found."
        )


async def service_delete_job_by_id(
    job_id: int,
    db: Session
):
    if job := db.get(JobPosting, job_id):
        job.status = JobPostingStatusEnum.DELETED
        job.deleted_at = datetime.datetime.now()
        db.commit()
        db.refresh(job)
        return job
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job post not found."
)