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
        }
