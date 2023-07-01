import pytest
import asyncio
from sqlalchemy.orm import Session

from src.job.models import  JobPosting, Location
from src.job.schemas import CreateJobPostingSchema, UpdateJobPostingSchema


@pytest.mark.asyncio
async def test_get_list_jobs(session: Session, job_posting: JobPosting):
    from src.job.services import service_get_list_jobs as get_list_jobs
    
    case = await get_list_jobs(db=session)
    assert len(case) == len(job_posting)


@pytest.mark.asyncio
async def test_get_job_by_id(session: Session, job_posting: JobPosting):
    from src.job.services import service_get_job_by_id as get_job_by_id

    case = await get_job_by_id(job_id=job_posting[0].id, db=session)
    assert case
    assert case.id == job_posting[0].id
    assert case.title == job_posting[0].title


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
    case = await create_job(job_post=job_post, db=session)
    assert case
    assert case.title == job_post.title


@pytest.mark.asyncio
async def test_update_job_by_id(session: Session, job_posting: JobPosting):
    from src.job.services import service_update_job_by_id as update_job_by_id

    job_post = UpdateJobPostingSchema(title="변경된 제목")
    case = await update_job_by_id(job_id=job_posting[0].id, job_post=job_post, db=session)
    assert case
    assert case.title == job_post.title


@pytest.mark.asyncio
async def test_delete_job_by_id(session: Session, job_posting: JobPosting):
    from src.job.services import service_delete_job_by_id as delete_job_by_id

    case = await delete_job_by_id(job_id=job_posting[0].id, db=session)
    assert case