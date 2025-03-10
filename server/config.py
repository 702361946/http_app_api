#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)
import os
import socket
import sys

import uvicorn
from fastapi import FastAPI

# 寻找包
if True:
    # os.path.abspath(__file__) -> .\server\config.py
    # os.path.dirname(os.path.dirname(os.path.abspath(__file__))) ->.\
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from dependency import *

# 文件保存区调整
json.file_path = os.path.join('json', 'server')

# 加载配置
if True:
    server_config = json.load("config")
    if type(server_config).__name__ != 'dict':
        server_config = {
            'server_fixed_ip': None,  # 服务器固定IP(若为空,则自动获取一个本地可用ip)
            'server_fixed_port': None,  # 服务器固定端口(若为空,则从60000开始不断+1,请配置好范围转发)
            'max_client': None,  # 最大客户端数量
            'get_client_message_time': 10,  # 获取客户端消息间隔(ms)
            'version': '0.1'
        }


def get_local_ip():
    """获取本机网卡IP地址"""
    try:
        # 创建一个UDP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 连接到一个外部地址
        s.connect(("8.8.8.8", 80))
        # 获取本地IP地址
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception as e:
        print(f"获取IP地址失败: {e}")
        return "127.0.0.1"  # 如果失败返回本地回环地址


class HTTPMethod:
    def __init__(self):
        self.ip = server_config["server_fixed_ip"]
        self.port = server_config["server_fixed_port"]
        self.max_client = server_config["max_client"]
        self.get_client_message_time = server_config["get_client_message_time"]
        self.client_list = []
        self.version = server_config["version"]

        while True:
            try:
                if self.ip is None:
                    self.ip = get_local_ip()

                elif type(self.ip).__name__ != 'str':
                    logging.error(f"配置ip无效:{self.ip}")
                    print(f"配置ip无效:{self.ip}")
                    self.ip = get_local_ip()

                # 空ip会绑定到0.0.0.0上,这是不希望的
                elif self.ip == '' or self.ip == '0.0.0.0':
                    self.ip = input('ip不可绑定至0.0.0.0,请手动输入')

                elif self.ip.split('.') != 4:
                    logging.error(f"配置ip长度不足:{self.ip}")
                    print(f"配置ip长度不足:{self.ip}")
                    self.ip = get_local_ip()

                for _ip in self.ip.split('.'):
                    try:
                        if int(_ip) < 0 or int(_ip) > 255:
                            logging.error(f"ip段超出范围:{self.ip}")
                            print(f"ip段超出范围:{self.ip}")
                            self.ip = get_local_ip()
                    except ValueError:
                        logging.error(f"ip段包含其他字符:{self.ip}")
                        print(f"ip段包含其他字符:{self.ip}")
                        self.ip = get_local_ip()

                if self.port is None:
                    self.port = 60000
                elif type(self.port).__name__ != 'int':
                    try:
                        self.port = int(self.port)
                    except ValueError:
                        logging.error(f"配置端口无效:{self.port}")
                        print(f"配置端口无效:{self.port}")
                        self.port = 60000
                if self.port < 1025 or self.port > 65535:
                    logging.error(f"配置端口超出范围:{self.port}")
                    print(f"配置端口超出范围:{self.port}")
                    self.port = 60000

                logging.info(f"ip:{self.ip}")
                logging.info(f"port:{self.port}")

                self.server = FastAPI()
                break
            except Exception as e:
                logging.error(e)
                print(e)


    def run(self) -> bool:
        """
        运行此已定义的服务
        :return: T/F
        """
        try:
            print("启动中")
            uvicorn.run(self.server, host=self.ip, port=self.port)
            return True
        except Exception as e:
            print(f"{e}")
            return False

    def get_state(self):
        """获取当前的状态"""
        _state = {
            'ip': self.ip,
            'port': self.port,
            'max_client': self.max_client,
            'get_client_message_time': self.get_client_message_time,
            'client_list': self.client_list,
            'version': self.version
        }
        print(f"server_state\n{_state}")
        return _state

    def get_state_logging(self):
        """获取当前的状态并记录日志"""
        _state = self.get_state()
        logging.info("server_state")
        logging.info(_state)
        logging.info("END")
