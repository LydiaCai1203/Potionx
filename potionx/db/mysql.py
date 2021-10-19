from copy import deepcopy
from six.moves.urllib.parse import quote


def get_mysql_url(conf: dict) -> str:
    db_conf = deepcopy(conf)
    db_conf["user"] = quote(conf.get("user", ""))
    db_conf["password"] = quote(conf.get("password", ""))

    url = "mysql+pymysql://{user}:{password}@{host}:{port}/{name}?charset=utf8mb4".format(
        **db_conf
    )
    return url
