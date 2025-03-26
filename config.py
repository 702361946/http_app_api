#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)
import importlib.util
import os

from fastapi import FastAPI

from dependency import *

srln('config')

if True:
    main_value = json.load('config')
    if type(main_value).__name__ != 'dict':
        logging.error(f'get main_value error\n{main_value}')
        main_value = {
            'open_s_or_c': None,
            "server_add_mods": []
        }
        json.dump(main_value, 'config')


def server_add_app(app: FastAPI):
    # 定义mods目录路径
    mods_path = os.path.join(".", "mods")
    mods_path = os.path.join(mods_path, 'server')

    all_mods = []
    add_if = False

    if main_value["server_add_mods"] != {}:
        add_if = True

    # 遍历mods目录
    for filename in os.listdir(mods_path):
        if filename.endswith('.py'):
            # 获取模块名（去掉.py后缀）
            module_name = filename[:-3]

            if add_if:
                if module_name not in main_value["server_add_mods"]:
                    continue

            # 构建完整文件路径
            file_path = os.path.join(mods_path, filename)

            # 动态加载模块
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            all_mods.append(module)

        elif os.path.isdir(os.path.join(mods_path, filename)):
            init_path = os.path.join(mods_path, filename, '__init__.py')
            if os.path.exists(init_path):
                if add_if:
                    if filename not in main_value["server_add_mods"]:
                        continue
                # 如果是Python包，则动态加载
                try:
                    module = importlib.import_module(f'mods.server.{filename}')
                    all_mods.append(module)
                except ImportError as e:
                    logging.error(f"Failed to import package {filename}: {e}")

    for module in all_mods:
        # 如果模块中有add_app函数，则调用它
        if hasattr(module, 'add_app'):
            module.add_app(app)


mccae('config')
