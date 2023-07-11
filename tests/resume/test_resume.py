import pytest
from sqlalchemy.orm import Session

from src.resume.models import ResumePosting
from src.resume.schemas import CreateResumePostingSchema, ResumePostingSchema


@pytest.mark.asyncio
async def test_get_list_resume_posts(session: Session, resume_posting: ResumePosting):
    from src.resume.services import service_get_list_resumes as get_list_resumes

    case = await get_list_resumes(db=session)
    assert case
    assert len(case) == len(resume_posting)


@pytest.mark.asyncio
async def test_get_resume_by_id(session: Session, resume_posting: ResumePosting):
    from src.resume.services import service_get_resume_by_id as get_resume_by_id

    case = await get_resume_by_id(resume_id=1, db=session)
    assert case
    assert case.title == resume_posting[0].title


@pytest.mark.asyncio
async def test_create_resume_post(session: Session):
    from src.resume.services import service_create_resume as create_resume

    resume_post = CreateResumePostingSchema(
        title="제목",
        content="내용",
        job_type="fulltime",
        contact="01012345678",
    )
    case = await create_resume(resume_post=resume_post, db=session)
    assert case
    assert case.title == resume_post.title