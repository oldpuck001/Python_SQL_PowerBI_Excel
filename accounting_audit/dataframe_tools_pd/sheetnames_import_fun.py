# sheetnames_import_fun.py

# 获取工作表名称列表

import pandas as pd

def sheetnames_import(file_path=None):

    try:
        sheet_file = pd.ExcelFile(file_path)
        sheetnames = sheet_file.sheet_names
        info = 'Worksheet list successfully read!\n'
        return [True, info, sheetnames]
    
    except:
        sheetnames = []
        info = 'Failed to read worksheet list!\nThis feature is only supported for xlsx and xls format files.\n'
        return [False, info, sheetnames]