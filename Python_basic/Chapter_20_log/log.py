# log.py

import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,                                         # 设置日志级别为INFO
    format='%(asctime)s - %(levelname)s - %(message)s',         # 设置日志格式
    filename='export_log.log',                                  # 指定日志文件名
    filemode='a'                                                # 追加模式（'w' 为覆盖模式）
)

info = 'Hello, world!'

logging.info(f"Exporting file: {info}")

logging.info('Starting program')

logging.info('Trying to divide 1 by 0')

print(1 / 0)

logging.info('The division succeeded')

logging.info('Ending program')