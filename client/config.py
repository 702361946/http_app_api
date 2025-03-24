#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)

import os
import sys

import requests

# 寻找包
if True:
    # os.path.abspath(__file__) -> .\server\config.py
    # os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ->.\
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from dependency import *

# 文件保存区调整
json.file_path = os.path.join('json', 'client')

# 加载配置
if True:
    client_config = json.load("config")
    if type(client_config).__name__ != 'dict':
        client_config = {
            'server_url': None,  # 服务器地址
            'client_fixed_port': None,  # 客户端固定端口
            'automatic_logon': {  # 自动登录
                'open': False,
                'username': None,
                'password': None
            }
        }


class HTTPMethod:
    def __init__(self):
        self.method: set[str] = {
            "GET",
            "POST",
            "DELETE",
            "PUT",
            "PATCH",
            "HEAD",
            "OPTIONS"
        }
        self.http = requests

        if type(client_config["server_url"]).__name__ != "str":
            self.server_url = input("请输入服务器地址")
        else:
            self.server_url = client_config["server_url"]

        if self.server_url[-1] == '/':
            self.server_url = self.server_url[:-1]

        if type(client_config["client_fixed_port"]).__name__ != "int":
            self.client_fixed_port = None
        else:
            self.client_fixed_port = client_config["client_fixed_port"]

        # 自动登录部分
        if True:
            pass

    async def get(self, path: str = ""):
        """
        发送get请求
        :param path: 请求路径
        :return: 返回请求结果
        """
        return self.http.get(f"{self.server_url}/{path}")

    async def post(self, path: str = ""):
        """
        发送post请求
        :param path:
        :return:
        """
        return self.http.post(f"{self.server_url}/{path}")

    async def delete(self, path: str = ""):
        """
        发送delete请求
        :param path:
        :return:
        """
        return self.http.delete(f"{self.server_url}/{path}")

    async def put(self, path: str = ""):
        """
        发送put请求
        :param path:
        :return:
        """
        return self.http.put(f"{self.server_url}/{path}")

    async def patch(self, path: str = ""):
        """
        发送patch请求
        :param path:
        :return:
        """
        return self.http.patch(f"{self.server_url}/{path}")

    async def head(self, path: str = ""):
        """
        发送head请求
        :param path:
        :return:
        """
        return self.http.head(f"{self.server_url}/{path}")

    async def options(self, path: str = ""):
        """
        发送options请求
        :param path:
        :return:
        """
        return self.http.options(f"{self.server_url}/{path}")

    async def http_method(self, method: str, path: str = ""):
        """
        对方法进行判断并发送请求
        :param method: 方法
        :param path:
        :return:
        """
        match method:
            case 'GET':
                method = self.get
            case 'POST':
                method = self.post
            case 'DELETE':
                method = self.delete
            case 'PUT':
                method = self.put
            case 'PATCH':
                method = self.patch
            case 'HEAD':
                method = self.head
            case 'OPTIONS':
                method = self.options
            case _:
                return False

        return await method(path)

    @staticmethod
    async def return_json(message: requests.Request = None):
        """
        用于对消息进行json化并返回
        :param message:
        :return: F/json
        """
        try:
            if message is not None:
                return message.json()

        except Exception as e:
            print(e)
            logging.error(f"json化失败\n{e}")
            return False
