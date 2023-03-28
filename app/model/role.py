from sqlalchemy import Boolean, Column, Integer, String

from app.model import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True, comment="自增ID")
    name = Column(String, unique=True, nullable=False, comment="角色名")
