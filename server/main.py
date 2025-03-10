#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)

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

    s.run()


if __name__ == '__main__':
    print(json.file_path)
