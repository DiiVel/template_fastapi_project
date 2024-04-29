from repository.users import UserRepository
from services.users import UsersService


def users_service() -> UsersService:
    return UsersService(UsersService)