import os
import inspect
import importlib
import traceback

from loguru import logger
from sqlalchemy import text

from app.model import Base
from config import config


POSTGRESQL_URL = "postgresql://{username}:{password}@{host}:{port}/{db}".format(
    username=config.postgresql.username,
    password=config.postgresql.password,
    host=config.postgresql.host,
    port=config.postgresql.port,
    db=config.postgresql.database 
)


def ping_db() -> bool:
    text = os.popen(
        "pg_isready "
        f"--dbname={config.postgresql.database} "
        f"--host={config.postgresql.host} "
        f"--port={config.postgresql.port} "
        f"--username={config.postgresql.username} "
    )
    return True if "accept" in text.read() else False


def get_updated_trigger_sql(table_name: str) -> tuple:
    """ 创建更新时间的触发器 """
    create_func_sql = """
        CREATE OR REPLACE FUNCTION update_modified_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = now();
            RETURN NEW;
        END;
        $$ language 'plpgsql';
    """
    create_trigger_sql = """
        CREATE TRIGGER update_{table_name}_update_at 
        BEFORE UPDATE ON {table_name} 
        FOR EACH ROW EXECUTE PROCEDURE  update_modified_column();
    """
    return create_func_sql, create_trigger_sql.format(table_name=table_name)


def get_model_class() -> list:
    """ 获取所有数据库的表名
    """
    app_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(app_path, "model")
    module_names = map(
        lambda x: x.rstrip(".py"),
        filter(
            lambda x: x.endswith(".py") and x != "__init__.py",
            os.listdir(model_path)
        )
    )
    module_class = [
        inspect.getmembers(
            importlib.import_module(f"app.model.{mn}", package=None), 
            inspect.isclass
        )
        for mn in module_names
    ]
    tables = [
        c[1].__tablename__
        for mc in module_class
        for c in mc
        if issubclass(c[1], Base) and c[0] != "Base"
    ]
    return tables


def init_db(engine) -> str:
    tables = get_model_class()
    for table in tables:
        with engine.connect() as conn:
            trans = conn.begin()
            try:
                fsql, tsql = get_updated_trigger_sql(table)
                conn.execute(text(fsql))
                conn.execute(text(tsql))
                trans.commit()
            except Exception:
                trans.rollback()
                msg = traceback.format_exc()
                if "already" not in msg:
                    return msg
            finally:
                trans.close()
    return "Success"
