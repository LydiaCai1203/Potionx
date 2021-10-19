from functools import wraps
from urllib.parse import urljoin

from flask_restful import Resource


RESOURCES = dict()

def route(url: str):

    url_prefix = "/api/v1"
    url = f"{url_prefix}{url}"

    def decorator(handler_cls: Resource):
        RESOURCES.update({url: handler_cls})

        @wraps(handler_cls)
        def inner():
            return handler_cls    
        return inner
    return decorator
