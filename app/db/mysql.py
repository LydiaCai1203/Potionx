from config import config


MYSQL_URL = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset={charset}".format(
    username=config.mysql.username,
    password=config.mysql.password,
    host=config.mysql.host,
    port=config.mysql.port,
    db=config.mysql.database,
    charset=config.mysql.charset
)


def ping_db() -> bool:
    return False


def init_db(engine) -> str:
    return "Success"
