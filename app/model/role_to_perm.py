from sqlalchemy import Column, Integer, String, UniqueConstraint

from app.model import Base


class RoleToPerm(Base):
    __tablename__ = "role_to_perm"
    __table_args__ = (
        UniqueConstraint(
            "role_pk", 
            "perm_pk", 
            name='unique_role_perm_idx'
        ),
    )

    id = Column(Integer, primary_key=True, index=True)
    role_pk = Column(String, nullable=False)
    perm_pk = Column(String, nullable=False)
