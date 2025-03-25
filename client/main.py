#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)

from .config import *


def main():
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
            print(t.http_method(mode, url))

if __name__ == '__main__':
    print(json.file_path)
