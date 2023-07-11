from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import Session

from src.database.config import get_db
from .schemas import ResumePostingSchema, CreateResumePostingSchema
from .services import (
    service_get_list_resumes, 
    service_create_resume, 
    service_get_resume_by_id,
)


resume_routers = APIRouter()

@resume_routers.get("", response_model=Page[ResumePostingSchema])
async def get_resume_posts(
    db: Session = Depends(get_db)
):
    """Get resume posts."""
    resume_posts = await service_get_list_resumes(db)
    return paginate(resume_posts)


@resume_routers.get("/{resume_id}", response_model=ResumePostingSchema)
async def get_resume(
    resume_id: int,
    db: Session = Depends(get_db)
):
    """Get a resume post."""
    return await service_get_resume_by_id(resume_id, db
)


@resume_routers.post("", response_model=ResumePostingSchema)
async def create_resume_post(
    resume_post: CreateResumePostingSchema,
    db: Session = Depends(get_db)
):
    """Create a resume post."""
    return await service_create_resume(resume_post, db)


