import datetime
from http import HTTPStatus
from http.client import HTTPException

from fastapi import APIRouter, Depends
from fastapi.responses import Response

from schemas.users import UserSchemaAdd, UserSchema
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
    return {"user_id": user_id}


@router.get("/")
async def get_users(
    users_service: UsersService = Depends(users_service),
):
    users = await users_service.get_posts()
    return users


@router.patch("/release_lock/{user_id:int}")
async def release_lock(
    user_id: int,
    users_service: UsersService = Depends(users_service),
):
    """
    Release lock for user
    :param user_id: need to be sent in order to acquire lock.
    :param users_service: object that holds the users service and helps to use db
    :return: 200 OK if successful
    """
    user = await users_service.get_user(user_id)

    if user is None:
        raise HTTPException(status_code=400, detail="There is no such user.")
    if user.locktime is None:
        raise HTTPException(status_code=400, detail="User is already unlocked.")

    user.locktime = None

    await users_service.update_user(user)

    return {"message": "acquire_lock"}


@router.post("/acquire_lock/{user_id:int}")
async def acquire_lock(
    user_id: int,
    users_service: UsersService = Depends(users_service),
):
    """
    Acquire the locktime of a user.
    :param user_id: need to be sent in order to acquire lock.
    :param users_service: object that holds the users service and helps to use db
    :return:
    """
    user = await users_service.get_user(user_id)

    if user is None:
        raise HTTPException(status_code=400, detail="There is no such user.")
    if user.locktime is not None:
        raise HTTPException(status_code=400, detail="User is already locked.")

    user.locktime = datetime.datetime.utcnow()

    await users_service.update_user(user)

    return Response(status_code=HTTPStatus.OK, content={"message": "Lock has been acquired successfully."})
