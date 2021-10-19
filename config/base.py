""" 基础配置
"""
from environs import Env


env = Env()
env.read_env()
FLASK_MODE = env.str("FLASK_MODE", "dev")
PORT = env.int("PORT", 8002)

MYSQL_CONF = {
    "localhost": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "123",
        "port": 3306,
        "name": "db1",
    }
}

REDIS_CONF = {
    "localhost": {
        "host": "127.0.0.1",
        "port": 6379,
        "password": "",
        "ssl": True,
        "socket_connect_timeout": 5,
    }
}
