#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)

from fastapi.responses import FileResponse

from .config import *


def main():
    s = HTTPMethod()
    app = s.server

    @app.get('/server/state')
    def start():
        return s.get_state()

    @app.get('/server/state_logging')
    def start_logging():
        return s.get_state_logging()

    @app.get('/server/routes')
    def start_routes():
        _t = []
        for _i in list(s.server.routes):
            _t.append(str(_i))
        return _t

    @app.get("/favicon.ico")
    def get_ico():
        return FileResponse('.\\favicon.ico')

    s.run()

