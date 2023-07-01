from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session

from src.database.config import get_db
from .schemas import ResumePostingSchema, CreateResumePostingSchema
from .services import service_get_list_resume_posts, service_create_resume_post


resume_routers = APIRouter()

@resume_routers.get("", response_model=Page[ResumePostingSchema])
async def get_resume_posts(
    db: Session = Depends(get_db)
):
    """Get resume posts."""
    resume_posts = await service_get_list_resume_posts(db)
    return paginate(resume_posts)


@resume_routers.post("", response_model=ResumePostingSchema)
async def create_resume_post(
    resume_post: CreateResumePostingSchema,
    db: Session = Depends(get_db)
):
    """Create a resume post."""
    return await service_create_resume_post(resume_post, db)