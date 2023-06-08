from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .envs import config


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOW_ORIGINS,
    allow_credentials=config.ALLOW_CREDENTIALS,
    allow_methods=config.ALLOW_METHODS,
    allow_headers=config.ALLOW_HEADERS,
)


@app.get("/health")
async def health_check():
    return {"status": "ok"}