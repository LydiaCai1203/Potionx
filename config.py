import os
import sys

from loguru import logger
from dynaconf import Dynaconf


global_config = Dynaconf(
    load_dotenv=True,
    envvar_prefix=False,
    settings_files=['config/settings.json', 'config/.secrets.json'],
)
config = (
    global_config.production
    if global_config.potionx_env == "production" else
    global_config.development
)


# log-config
class PLog:
    """ 自定义的日志配置
    """
    
    log_format = (
        "<level>{level: <8}</level> "
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> - "
        "<blue>{process}</blue> "
        "<cyan>{module}</cyan>.<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
        "<level>{message}</level>"
    )
    def __init__(self):
        logger.remove()
        self._log_path = "logs"
        os.makedirs(self._log_path, exist_ok=True)
        self._init_stdout_log()
        self._init_debug_log()
        self._init_info_log()
        self._init_error_log()

    def _init_info_log(self):
        logger.add(
            os.path.join(self._log_path, "info.log.{time:YYYY-MM-DD}"),
            format=self.log_format,
            level="INFO",
            rotation="00:00",
            retention="3 days",
            backtrace=True,
            diagnose=True,
        )
    
    def _init_error_log(self):
        logger.add(
            os.path.join(self._log_path, "error.log.{time:YYYY-MM-DD}"),
            format=self.log_format,
            level="ERROR",
            rotation="00:00",
            retention="3 days",
            backtrace=True,
            diagnose=True,
        )

    def _init_debug_log(self):
        logger.add(
            os.path.join(self._log_path, "debug.log.{time:YYYY-MM-DD}"),
            format=self.log_format,
            level="DEBUG",
            rotation="00:00",
            retention="1 days",
            backtrace=True,
            diagnose=True,
        )
    
    def _init_stdout_log(self):
        logger.add(
            sys.stdout,
            format=self.log_format,
            level="INFO",
            colorize=True,
        )



print(
    """
                                        \ | | / 
                                    |    Ø___oo 
                    / \     / \    /   (__ „ „ „ „] 
                    / ^ \  /  ^ \ /     _) 
                    ) V V  V /      __) 
                    )           /   /   ___) 
        / \        V¯V¯V|   |      )__) 
        <   >             / ( „ „ )     ) ___) 
        |  |             (         |    \_ ___)\_ 
        |   \______(         /        )____)_)_ 
        \____________(______;_;_)_;_;_)Æ¨              -byacaicai
    """
)
