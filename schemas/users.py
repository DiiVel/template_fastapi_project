import datetime
from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    created_ad: datetime
    login: str
    password: str
    project_id: int
    env: str
    domain: str
    locktime: datetime


class UserSchemaAdd(BaseModel):
    login: str
    password: str
    project_id: int
    env: str
    domain: str
    locktime: datetime
