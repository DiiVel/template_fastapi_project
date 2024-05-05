import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, TIMESTAMP
from schemas.users import UserSchema
from core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_ad = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    env = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    locktime = Column(TIMESTAMP, default=None)

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            created_ad=self.created_ad,
            login=self.login,
            password=self.password,
            project_id=self.project_id,
            env=self.env,
            domain=self.domain,
            locktime=self.locktime,
        )

    @staticmethod
    def validate_env(env_value: str):
        valid_values = ["prod", "preprod", "stage"]
        if env_value not in valid_values:
            raise ValueError(f"Invalid value for 'env'. Valid values are: {', '.join(valid_values)}")
        return env_value

    @staticmethod
    def validate_domain(domain_value: str):
        valid_values = ["canary", "regular"]
        if domain_value not in valid_values:
            raise ValueError(f"Invalid value for 'domain'. Valid values are: {', '.join(valid_values)}")
        return domain_value

    def __setattr__(self, key, value):
        if key == "env":
            value = self.validate_env(value)
        elif key == "domain":
            value = self.validate_domain(value)
        super().__setattr__(key, value)
