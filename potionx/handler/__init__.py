import os
import json

from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api
from werkzeug.exceptions import HTTPException
from werkzeug.exceptions import NotFound

from config import FLASK_MODE, DevConf, PrdConf


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(PrdConf if FLASK_MODE == "prd" else DevConf)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


app = create_app()
api = Api(app)


class BaseHandler(Resource):

    def write_json(code=200, msg="", data=None):
        """ 序列化返回
        """
        return {
            "code": code,
            "msg": msg,
            "data": data,
        }

    # @staticmethod
    # @app.errorhandler(Exception)
    # def write_error(e: Exception):
    #     """ 全局异常捕捉
    #     """
    #     code = 500
    #     if isinstance(e, HTTPException):
    #         code = e.code
        
    #     BaseHandler.write_json(code=code, msg=str(e))


    # @app.before_request
    # def before_request():
    #     pass
    
    # @app.after_request
    # def after_request(resp):
    #     pass