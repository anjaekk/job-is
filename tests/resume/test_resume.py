import pytest
from sqlalchemy.orm import Session

from src.resume.models import ResumePosting
from src.resume.schemas import CreateResumePostingSchema, ResumePostingSchema


@pytest.mark.asyncio
async def test_get_list_resume_posts(session: Session, resume_posting: ResumePosting):
    from src.resume.services import service_get_list_resume_posts as get_list_resume_posts

    case = await get_list_resume_posts(db=session)
    assert case
    assert len(case) == len(resume_posting)


@pytest.mark.asyncio
async def test_create_resume_post(session: Session):
    from src.resume.services import service_create_resume_post as create_resume_post

    resume_post = CreateResumePostingSchema(
        title="제목",
        content="내용",
        job_type="fulltime",
        contact="01012345678",
    )
    case = await create_resume_post(resume_post=resume_post, db=session)
    assert case
    assert case.title == resume_post.title