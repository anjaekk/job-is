from fastapi import FastAPI
from fastapi_pagination import add_pagination
from starlette.middleware.cors import CORSMiddleware

from .envs import config
from .job.routers import job_routers
from .resume.routers import resume_routers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOW_ORIGINS,
    allow_credentials=config.ALLOW_CREDENTIALS,
    allow_methods=config.ALLOW_METHODS,
    allow_headers=config.ALLOW_HEADERS,
)

app.include_router(job_routers, prefix="/jobs")
app.include_router(resume_routers, prefix="/resumes")

add_pagination(app)

@app.get("/health")
async def health_check():
    return {"status": "ok"}