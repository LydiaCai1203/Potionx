from typing import Generic, TypeVar, Any

from pydantic import BaseModel
from pydantic.generics import GenericModel

T = TypeVar("T")


class ReqException(Exception):
    def __init__(self, value: int, msg: str, msg_cn: str):
        self.value = value
        self.msg = msg
        self.msg_cn = msg_cn
    
    def __int__(self):
        return self.value
    
    def __str__(self):
        return self.msg


class ReqStatus:
    BASE = 100000
    
    SUCCESS = ReqException(BASE + 1, "Success", "成功")
    FAILED = ReqException(BASE + 2, "Faild", "失败")
    
    EXISTS = ReqException(BASE + 3, "Exists", "已存在")
    NOT_FOUND = ReqException(BASE + 4, "Not found", "未找到")
    NOT_EXISTS = ReqException(BASE + 5, "Not exists", "不存在")
    UNKNOWN = ReqException(BASE + 6, "Unknown error", "未知错误")
    PARAM_ERROR = ReqException(BASE + 7, "Params error", "参数错误")
    METHOD_NOT_ALLOWED = ReqException(BASE + 8, "Method not allowed", "请求方法不被允许")

    NOT_LOGIN = ReqException(BASE + 9, "Not login", "未登录")
    USER_BANNED = ReqException(BASE + 10, "User is banned", "用户被禁用")
    PERMISSION_DENIED = ReqException(BASE + 11, "Permission denied", "权限不足")
    DATA_PERMISSION_DENIED = ReqException(BASE + 12, "Data permission denied", "数据权限不足")


class GerneralResponse(GenericModel, Generic[T]):

    def __init__(
        self,
        code: int=int(ReqStatus.SUCCESS), 
        message: str=str(ReqStatus.SUCCESS), 
        data: T=None
    ):
        self.code = code
        self.message = message
        self.data = data


class BaseSchema(BaseModel):
    extra: Any | None
    is_delete: bool | None
    created_at: str | None
    updated_at: str | None
