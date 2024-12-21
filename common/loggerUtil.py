import logging
import os
import time

from colorlog import ColoredFormatter

import config.conf

# 创建日志记录器
logger = logging.getLogger('my_logger')

# 检查是否已经添加过处理器，避免重复添加
if not logger.hasHandlers():
    logger.setLevel(logging.DEBUG)

    # 定义日志颜色格式
    log_colors = {
        'DEBUG': 'white',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red'
    }

    # 创建控制台处理器并设置级别
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 设置彩色格式化器，使用方括号分割信息
    color_formatter = ColoredFormatter(
        "[%(levelname)s] %(log_color)s[%(asctime)s]:[%(name)s] - %(filename)s:%(lineno)d - %(message)s",
        log_colors=log_colors
    )
    console_handler.setFormatter(color_formatter)

    # 确保日志目录存在
    path = os.path.join(config.conf.BASE_DIR, "log")
    if not os.path.exists(path):
        os.makedirs(path)

    # 创建文件处理器并设置级别
    daytime = time.strftime("%Y-%m-%d")
    filename = os.path.join(path, f'run_log_{daytime}.log')
    file_handler = logging.FileHandler(filename=filename, mode='a', encoding='utf8')
    file_handler.setLevel(logging.INFO)

    # 设置文件格式化器（不带颜色），使用方括号分割信息
    file_formatter = logging.Formatter(
        '[%(asctime)s] [%(name)s] [%(levelname)s] [%(filename)s:%(lineno)d] - %(message)s'
    )
    file_handler.setFormatter(file_formatter)

    # 将处理器添加到记录器
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
