from fastapi import APIRouter

from app.handler.v1 import user, role, perm


api_v1_router = APIRouter()
api_v1_router.include_router(user.router, prefix="/user")
api_v1_router.include_router(role.router, prefix="/role")
api_v1_router.include_router(perm.router, prefix="/perm")
