from pydantic import BaseModel, Field


class User(BaseModel):
    email: str = Field(default='admin')
    password: str = Field(default='admin')
