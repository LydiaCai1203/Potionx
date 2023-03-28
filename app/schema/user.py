from pydantic import BaseModel


class UserSchema(BaseModel):
    username: str
    nickname: str
    phone: str
    email: str | None
    password: str
