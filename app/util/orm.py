from typing import Any

from sqlalchemy.sql import asc, desc
from sqlalchemy.orm import Session, Query
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.dialects import postgresql

from app.model import Base


class BaseRepo:
    
    @staticmethod
    def compile_query(query: Query) -> str:
        compiler = query.compile if not hasattr(query, 'statement') else query.statement.compile
        return compiler(dialect=postgresql.dialect())

    @staticmethod
    def upsert(session: Session, table: Base, row: dict[str, Any], constraint: list[str]) -> int:
        """ 存在即更新，否则则插入，返回行主键(id)

        Args:
            session (Session): next(get_db())
            table (Base): app.model.Model 里的表对象
            row (dict[str, Any]): 待插入数据字典
            constraint (list[str]): 表字段名称列表，当该列表内字段的数据在表中存在，则执行更新操作，否则执行插入操作

        Returns:
            int: 行主键
        """
        insert_stmt = insert(table.__table__).values(**row)
        on_conflict_stmt = insert_stmt.on_conflict_do_update(
            index_elements=constraint,
            set_=row
        )
        obj = session.execute(on_conflict_stmt.returning(table.id))
        return obj.fetchone()[0]
    
    @staticmethod
    def sql_order(expr: Query, is_desc: str, order_fields: str) -> Query:
        """ 获取排序 query expr
        Args:
            expr: Query - 查询语句
            is_desc: str - 排序类型，0-升序 1-降序, 英文逗号分隔
            order_fields: str - 排序字段，英文逗号分隔
        """
        return expr.order_by(
            *[
                (desc if int(is_desc) else asc)(order_field)
                for order_field, is_desc in zip(order_fields.split(","), is_desc.split(","))
            ]
        )

    @staticmethod
    def sql_pagination(expr: Query, page_size: int, page_no: int) -> Query:
        """ 获取分页条件
        Args:
            expr: Query - 查询语句
            page_size: int - 页大小
            page_no: int - 页码
        """
        return (
            expr.offset((page_no - 1) * page_size)
            .limit(page_size)
        )
