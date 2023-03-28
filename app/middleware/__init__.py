from typing import Callable
from loguru import logger

from fastapi import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app import app
from app.schema import GerneralResponse, ReqException, ReqStatus


# 全局错误捕获器
@app.middleware("http")
async def errors_handling(request: Request, call_next: Callable):
    try:
        response = await call_next(request)
    except ReqException as exc:
        msg = "-".join(map(lambda x: str(x), exc.args[1:]))
        response = JSONResponse(
            status_code=ReqStatus.SUCCESS,
            content=jsonable_encoder(
                GerneralResponse(
                    code=exc,
                    message=msg,
                    data=None,
                )
            ),
        )
    except Exception as exc:
        msg = __import__("traceback").format_exc()
        logger.error(msg)
        msg = "-".join(map(lambda x: str(x), exc.args))
        response = JSONResponse(
            status_code=ReqStatus.SUCCESS,
            content=jsonable_encoder(
                GerneralResponse(
                    code=ReqStatus.FAILED,
                    message=msg or "服务器错误，请联系管理员",
                    data=None,
                )
            ),
        )
    return response
