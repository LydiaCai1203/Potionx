import os
import datetime

from redis import Redis
# from environs import Env

from config.base import MYSQL_CONF, REDIS_CONF, FLASK_MODE
from potionx.db.mysql import get_mysql_url
from config.base import *


class BaseConf:

    DB_LOCALHOST= get_mysql_url(MYSQL_CONF['localhost'])

    ENV = FLASK_MODE
    WTF_CSRF_ENABLED = True
    SQLALCHEMY_BINDS = {
        # 不同的数据库连接在此绑定
        'localhost': DB_LOCALHOST,
    }

    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    SCHEDULER_API_ENABLED = True
    PROPAGATE_EXCEPTIONS = True

    # SESSION CONFIG
    SECRET_KEY = os.urandom(64)
    SESSION_KEY_PREFIX = 'potionx.'
    SESSION_USE_SIGNER = False
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours=8)
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(**REDIS_CONF['localhost'])


class DevConf(BaseConf):
    DEBUG = True
    WTF_CSRF_ENABLED = False


class PrdConf(BaseConf):
    DEBUG = False