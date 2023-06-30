import pytest
import asyncio
from sqlalchemy.orm import Session
from src.job.models import  JobPosting, Location
from src.job.schemas import CreateJobPostingSchema


@pytest.mark.asyncio
async def test_get_list_jobs(session: Session, job_posting: JobPosting):
    from src.job.services import service_get_list_jobs as get_list_jobs
    
    case = await get_list_jobs(db=session)
    assert len(case) == len(job_posting)


@pytest.mark.asyncio
async def test_create_job(session: Session, location: Location):
    from src.job.services import service_create_job as create_job

    job_post = CreateJobPostingSchema(
        title="제목",
        content="내용",
        category="food_service",
        location_id=location.id,
        salary={"시급": "1000000"}
    )
    response = await create_job(db=session, job_post=job_post)
    assert response
    assert response.title == job_post.title
