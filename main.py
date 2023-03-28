import uvicorn

from app.db import init_db
from config import PLog, config

PLog()


if __name__ == '__main__':
    from loguru import logger

    init_msg = init_db()
    logger.info(f"#### Init DB {init_msg} ####")

    uvicorn.run(
        app="app:app",
        host=config.host,
        port=config.port,
        workers=config.workers,
        reload=config.reload
    )
