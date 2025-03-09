#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)

import os
import socket
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

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


def is_port_available(port, host='localhost'):
    """测试端口是否可用于部署本地服务
    :param port: 要测试的端口号
    :param host: 目标主机，默认为localhost
    :return: True表示端口可用，False表示端口已被占用
    """
    try:
        # 创建一个TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置超时时间为1秒
        sock.settimeout(1)
        # 尝试绑定端口
        sock.bind((host, port))
        sock.close()
        return True
    except socket.error as e:
        # 如果端口已被占用，会抛出socket.error异常
        print(f"端口 {port} 已被占用: {e}")
        return False


def get_open_port():
    """
    获取可用端口
    :return: 可用端口号，如果没有可用端口则返回False
    """
    start_port = 60000
    while_open = True
    while start_port != 60000 or while_open:
        if is_port_available(start_port):
            return start_port

        if start_port == 60000:
            while_open = False

        start_port += 1
        if start_port == 65535:
            start_port = 1

    return False


class HTTPMethod:
    def __init__(self):
        self.ip = server_config["server_fixed_ip"]
        self.port = server_config["server_fixed_port"]
        self.max_client = server_config["max_client"]
        self.get_client_message_time = server_config["get_client_message_time"]
        self.client_list = []
        self.version = server_config["version"]

        if server_config["server_fixed_ip"] is None:
            self.ip = get_local_ip()
        if server_config["server_fixed_port"] is None:
            self.port = get_open_port()

        # 定义请求处理类
        # class R(BaseHTTPRequestHandler):
        #     def do_GET(self):
        #         self.send_response(200)
        #         self.end_headers()
        #         self.wfile.write(b'Hello, World!')

        create_an_attempt = 0
        while create_an_attempt < 50:
            try:
                self.server = HTTPServer(
                    (self.ip, self.port),
                    BaseHTTPRequestHandler
                )
            except WindowsError:
                self.ip = input(f"此地址无效,请更换地址\n当前地址:{self.ip}")
                create_an_attempt += 1
            except OverflowError:
                print(f"端口已被占用或不可用\n尝试更换端口中\n当前端口:{self.port}")
                if self.port >= 65535:
                    self.port = 1025
                else:
                    self.port += 1
                create_an_attempt += 1
            except Exception as e:
                print(f"{e}")

    def run(self) -> bool:
        """
        运行此已定义的服务
        :return: T/F
        """
        try:
            print("启动中(启动成功后无提示)")
            self.server.serve_forever()
            return True
        except Exception as e:
            print(f"{e}")
            return False

    def stop(self) -> bool:
        """
        停止此服务
        :return: T/F
        """
        try:
            self.server.shutdown()
            return True
        except Exception as e:
            print(f"{e}")
            return False

    def http_get(self):
        pass

    def http_post(self):
        pass

    def http_put(self):
        pass

    def http_delete(self):
        pass

    def http_head(self):
        pass

    def http_options(self):
        pass

    def http_patch(self):
        pass

    def http_trace(self):
        pass

    def http_connect(self):
        pass

    def http_other(self):
        pass

    def http_method_get(self, method):
        """
        根据请求的方法获取对应的函数(请自行调用)
        :param method: 方法名
        :return: T/F
        """
        method = method.upper()
        match method:
            case "GET":
                return self.http_get
            case "POST":
                return self.http_post
            case "PUT":
                return self.http_put
            case "DELETE":
                return self.http_delete
            case "HEAD":
                return self.http_head
            case "OPTIONS":
                return self.http_options
            case "PATCH":
                return self.http_patch
            case "TRACE":
                return self.http_trace
            case "CONNECT":
                return self.http_connect
            case _:
                return self.http_other

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
