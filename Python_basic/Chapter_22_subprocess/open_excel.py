# open_excel.py

# 讓Python程序使用系統默認的電子表格軟件打開.xlsx文件，在macOS系統中，可以使用subprocess模組來調用open命令

import subprocess

file_path = '/Users/lei/Downloads/aaa.xlsx'

subprocess.run(['open', file_path])