from models import User
from core.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User
