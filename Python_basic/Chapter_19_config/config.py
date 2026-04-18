# config.py

import os
import json

# 獲取當前腳本所在的目錄
script_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_dir, 'config.json')

# 讀取JSON配置文件
with open(config_path, 'r') as f:
    config = json.load(f)

# 獲取設定值
host = config['database']['host']
print(f"Host: {host}")