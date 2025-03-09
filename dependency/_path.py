#  Copyright (c) 2024-2025.
#  702361946@qq.com(https://github.com/702361946)

import logging
import os
from datetime import datetime

# 检查操作系统,以及处理路径
match os.name:
    case 'nt':
        os_name = 'Windows'
        log_path = os.path.expanduser('~\\AppData')
        log_path = os.path.join(log_path, 'LocalLow\\702361946\\Chemical Equation Game\\game.log')
    case 'posix':
        os_name = 'MacOS'
        log_path = os.path.expanduser('~/Library')
        log_path = os.path.join(log_path, 'Logs/702361946/Chemical Equation Game/game.log')
    case _:
        print(f"os.name:{os.name}")
        input('不支持的操作系统\n请发邮件至702361946@qq.com\n并附上python os.name输出内容')
        exit()

# 目录补全
os.makedirs(os.path.dirname(log_path), exist_ok=True)

if True:
    logging.basicConfig(filename=log_path, filemode='w', level=logging.DEBUG, encoding='UTF-8')
    # 获取root logger
    root_logger = logging.getLogger()
    # 修改root logger的名称
    root_logger.name = 'path'
    logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    logging.info(f"{os_name}:{log_path}")


    def setting_root_logger_name(root_logger_name: str) -> bool:
        """
        修改root logger的名称

        :param root_logger_name: 新root_logger名
        :return: 永远返回True,除非Error
        """
        logging.info("setting root_logger.name")
        logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        root_logger.name = root_logger_name
        logging.info(f"root_logger.name:{root_logger_name}")
        return True


    srln = setting_root_logger_name


    def module_configuration_completed_and_exit(module_name: str, message: str = None) -> bool:
        """
        报告模块配置完成并退出
        :param module_name: 模块名
        :param message: 自定义消息
        :return: 永远返回True,除非Error
        """
        if message:
            logging.info(message)
        else:
            logging.info(f"{module_name} ok and exit")
        logging.info(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        return True


    mccae = module_configuration_completed_and_exit

mccae('path')
