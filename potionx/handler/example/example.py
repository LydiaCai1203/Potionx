from flask import Flask, jsonify


from potionx.handler import BaseHandler
from potionx.route import route


@route("/asd")
class Example(BaseHandler):
    
    def get(self):
        a = self.write_json(msg="hello world")
        print(a)
        return a
    
