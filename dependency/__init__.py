#  Copyright (c) 2024-2025.
#  702361946@qq.com(https://github.com/702361946)

import logging
from datetime import datetime

from ._json import Json
from ._path import log_path, root_logger, os_name, srln, mccae

# logging
if True:
    # 修改root logger的名称
    srln('__init__')

json = Json()

logging.info('__init__ ok and exit')
logging.info(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
