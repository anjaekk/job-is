

from sqlalchemy.orm import Session
from sqlalchemy import desc

from .models import ResumePosting
from .schemas import CreateResumePostingSchema

async def service_get_list_resume_posts(
    db: Session
):
    return db.query(ResumePosting).filter(
        ResumePosting.is_deleted == False
    ).order_by(desc(ResumePosting.created_at)).all()


async def service_create_resume_post(
    resume_post: CreateResumePostingSchema,
    db: Session
):
    new_resume_post = ResumePosting(**resume_post.dict())

    db.add(new_resume_post)
    db.commit()
    db.refresh(new_resume_post)
    return new_resume_post