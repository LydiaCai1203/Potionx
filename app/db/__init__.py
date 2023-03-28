import os
import time
import importlib

from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.model import Base
from app.db.postgresql import POSTGRESQL_URL
from app.db.mysql import MYSQL_URL
from config import config

url = {
    "postgresql": POSTGRESQL_URL,
    "mysql": MYSQL_URL
}.get(config.potionx_rel_db, "postgresql")

engine = create_engine(url, pool_size=100, max_overflow=100, pool_pre_ping=True, connect_args={'client_encoding': 'utf8'})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 每个请求都是一个新的会话，会话结束以后 session 关闭
# https://fastapi.tiangolo.com/tutorial/sql-databases/
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def import_table_model():
    """ 导入定义的数据表
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
    for mn in module_names:
        importlib.import_module(f"app.model.{mn}", package=None)


def init_db():
    db_module = importlib.import_module(f"app.db.{config.potionx_rel_db}", package=None) 
    
    while True:
        ping_flag = db_module.ping_db()
        if ping_flag: break
        logger.info(f"#### {config.potionx_rel_db} Not Ready，Reconnecting ... ####")
        time.sleep(1)
    logger.info(f"#### {config.potionx_rel_db} Already Ready，Connected! ####")
    
    import_table_model()
    Base.metadata.create_all(engine)
    
    init_msg = db_module.init_db(engine)
    logger.info(f"#### {config.potionx_rel_db} init {init_msg}... ####")
