from sqlalchemy import Column, Integer, String, UniqueConstraint

from app.model import Base


class UserToPerm(Base):
    __tablename__ = "user_to_role"
    __table_args__ = (
        UniqueConstraint(
            "user_pk", 
            "role_pk", 
            name='unique_user_role_idx'
        ),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_pk = Column(String, nullable=False)
    role_pk = Column(String, nullable=False)
