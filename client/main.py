#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)

from .config import *


async def main():
    t = HTTPMethod()
    while True:
        mode = input(f"输入请求方法\n输入exit退出\n{t.method}")
        if mode == "exit":
            break
        elif mode.upper() not in t.method:
            print("无此方法")
            continue

        while True:
            url = input("输入请求地址(如果输入../..则重新选择请求方法)")
            if url == '../..':
                break
            _t = await t.http_method(mode, url)
            try:
                print(f"ok:{_t.ok}")
                print(f"text:{_t.text}")
                print(f"json:{_t.json()}")
            except Exception as e:
                print(f"error:{e}")

if __name__ == '__main__':
    print(json.file_path)
