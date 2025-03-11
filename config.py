#  Copyright (c) 2025.
#  702361946@qq.com(https://github.com/702361946)

from dependency import *

srln('config')

if True:
    main_value = json.load('config')
    if type(main_value).__name__ != 'dict':
        logging.error(f'get main_value error\n{main_value}')
        main_value = {
            'open_s_or_r': None
        }
        json.dump(main_value, 'config')

mccae('config')
