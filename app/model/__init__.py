import re
import json
from typing import Any

import sqlalchemy
from sqlalchemy.sql import expression
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import DateTime, Boolean, Column, text
from sqlalchemy.ext.declarative import as_declarative, declared_attr

from app.util import data_fmt_transfer


def row_asdict(row_obj: sqlalchemy.engine.Row) -> dict:
    """ row 序列化 """
    data = {}
    for key, value in row_obj._mapping.items():
        (
            data.update(value._asdict())
            if isinstance(value, Base) else
            data.update({key: data_fmt_transfer(value)})
        )
    return data

# monkey patch
sqlalchemy.engine.Row._asdict = row_asdict


@as_declarative()
class Base:
    id: Any
    __name__: str

    @declared_attr
    def extra(cls):
        return Column(
            JSONB,
            nullable=False,
            server_default="{}",
            comment="预留扩充字段"
        )

    @declared_attr
    def is_delete(cls):
        return Column(
            Boolean,
            nullable=False,
            server_default=expression.false(),
            default=False,
            comment="是否删除"
        )

    @declared_attr
    def created_at(cls):
        return Column(
            DateTime(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
            comment="创建时间"
        )

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
            comment="更新时间"
        )

    @declared_attr
    def __tablename__(cls) -> str:
        return re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

    def _asdict(self) -> dict:
        """ 一些特殊字段类型的转换
        """
        r = {}
        for k in filter(
            lambda x: not x.startswith("_")
                and not callable(getattr(self, x))
                and x not in ["is_delete", "registry", "metadata"],
            dir(self)
        ):
            v = getattr(self, k)
            try:
                r[k] = json.loads(v)
            except Exception:
                r[k] = data_fmt_transfer(v)
        return r
