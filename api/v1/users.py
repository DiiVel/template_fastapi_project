from fastapi import APIRouter, Depends

from schemas.users import UserSchemaAdd
from services.users import UsersService
from core.dependencies import users_service

router = APIRouter(
    prefix="/users",
)


@router.get("/ping")
async def ping():
    return {"message": "pong"}


@router.post("/")
async def create_user(
        user: UserSchemaAdd,
        users_service: UsersService = Depends(users_service),
):
    user_id = await users_service.add_post(user)
    return {"post_id": user_id}


@router.get("/")
async def get_posts(
        users_service: UsersService = Depends(users_service),
):
    users = await users_service.get_posts()
    return users


@router.get("/{user_id:int}")
async def get_post(
        user_id: int,
        users_service: UsersService = Depends(users_service),
):
    user = await users_service.get_post(user_id)
    return user


@router.patch("/release_lock")
async def release_lock():
    return {"message": "release lock"}


@router.post("/acquire_lock")
async def acquire_lock():
    return {"message": "acquire_lock"}
