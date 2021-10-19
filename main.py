from potionx.lib.walk_module import walk_modules

from potionx.handler import app, api
from potionx.route import RESOURCES
from config import PORT


walk_modules()

if __name__ == "__main__":    
    for url, handler_cls in RESOURCES.items():
        print(url, handler_cls)
        api.add_resource(handler_cls, url)

    app.run(host="0.0.0.0", port=PORT)