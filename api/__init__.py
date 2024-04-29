from fastapi import FastAPI
from .v1.api import router

app = FastAPI(
    title="Prodigy blog API v1",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.include_router(router)