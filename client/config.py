#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)

import os
import sys

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
            'server_ip': None,  # 服务器IP
            'server_port': None,  # 服务器端口
            'client_fixed_port': None,  # 客户端固定端口
            'automatic_logon': {  # 自动登录
                'open': False,
                'username': None,
                'password': None
            }
        }
