from fastapi import FastAPI

from app.handler.v1 import api_v1_router


app = FastAPI()
app.include_router(api_v1_router, prefix="/api/v1")

