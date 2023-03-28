from sqlalchemy import Boolean, Column, Integer, String

from app.model import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, comment="自增ID")
    username = Column(String, unique=True, nullable=False, comment="用户名")
    password = Column(String, nullable=False, comment="密码")
