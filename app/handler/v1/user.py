from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from app.db import get_db
from app.schema import GerneralResponse
from app.schema.user import UserSchema

router = APIRouter()


@router.post("/register")
async def regist_user(item: UserSchema, db: Session = Depends(get_db)):
    """ 用户注册
    """
    response = GerneralResponse()
    db.query()