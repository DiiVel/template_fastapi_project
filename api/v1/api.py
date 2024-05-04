from fastapi import FastAPI
from .users import router as users_router

router = FastAPI()

router.include_router(users_router)
