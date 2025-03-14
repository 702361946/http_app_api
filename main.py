#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)

from config import *

srln('main')

while True:
    match main_value['open_s_or_r']:
        case 's':
            from server import main

            break
        case 'r':
            from client import main

            break
        case _:
            user_input = input("选择打开服务器或客户端(server\\s/client\\c)")
            logging.info(f"user input:{user_input}")
            if user_input == 's' or user_input == "server":
                main_value['open_s_or_r'] = 's'
                logging.info(f"user open server")
            elif user_input == 'c' or user_input == "client":
                main_value['open_s_or_r'] = 'c'
                logging.info(f"user open client")
            else:
                print('无此选项')

main()

logging.info('user exit')
