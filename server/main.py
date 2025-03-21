#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)

from fastapi.responses import FileResponse

from .config import *


def main(add_app=None):
    """

    :param add_app: 可以通过传入一个已定义的函数来添加路由,要求能默认接受一个FastAPI对象
    :return: 无返回,直接启动
    """
    s = HTTPMethod()
    app = s.server

    @app.get('/server/state')
    async def start():
        return await s.get_state()

    @app.get('/server/state_logging')
    async def start_logging():
        return await s.get_state_logging()

    @app.get('/server/routes')
    async def start_routes():
        _t = []
        for _i in list(await s.server.routes):
            _t.append(str(_i))
        return _t

    @app.get("/favicon.ico")
    async def get_ico():
        return FileResponse('.\\favicon.ico')

    if add_app is not None:
        add_app(app)

    s.run()

