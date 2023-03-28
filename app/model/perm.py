from sqlalchemy import Boolean, Column, Integer, String

from app.model import Base


class Perm(Base):
    __tablename__ = "perm"

    id = Column(Integer, primary_key=True, comment="自增ID")
    perm_name = Column(String, nullable=False, unique=True, comment="权限名称")
    perm_key = Column(String, nullable=False, comment="权限 key")
    perm_args = Column(String, nullable=True, comment="过滤参数")
