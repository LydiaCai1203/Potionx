import datetime
from enum import Enum
from typing import Any


def data_fmt_transfer(v: Any) -> Any:
    """ 常见数据格式的转换 """
    if isinstance(v, datetime.datetime):
        return v.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(v, Enum):
        return v.value
    else:
        return v
