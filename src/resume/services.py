
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import desc

from .models import ResumePosting
from .schemas import CreateResumePostingSchema
from ..core.posts import add_posting_views


async def service_get_list_resumes(
    db: Session
):
    return db.query(ResumePosting).filter(
        ResumePosting.is_deleted == False
    ).order_by(desc(ResumePosting.created_at)).all()


async def add_resume_posting_views(db, resume_post):
    resume_post.views += 1
    db.commit()
    db.refresh(resume_post)

async def service_get_resume_by_id(
    resume_id: int,
    db: Session
):
    if resume_post := db.get(ResumePosting, resume_id):
        await add_posting_views(db, resume_post)
        return resume_post
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Resume post not found."
        )


async def service_create_resume(
    resume_post: CreateResumePostingSchema,
    db: Session
):
    new_resume_post = ResumePosting(**resume_post.dict())

    db.add(new_resume_post)
    db.commit()
    db.refresh(new_resume_post)
    return new_resume_post