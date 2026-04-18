# import_function.py

import os
import pandas as pd

def sheetnames_import(request):

    file_path = request.get("data", {}).get("file_path", "")

    sheet_file = pd.ExcelFile(file_path)
    sheetnames = sheet_file.sheet_names

    return ['sheetnames_import', sheetnames]

def columns_index(request):

    file_path = request.get("data", {}).get("file_path", "")
    sheet_name = request.get("data", {}).get("sheet_name", "")

    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.xlsx':
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
    elif file_extension == '.xls':
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine='xlrd')

    columns = df.columns.tolist()

    return ['columns_index', columns]

def unique_index(request):

    file_path = request.get("data", {}).get("file_path", "")
    sheet_name = request.get("data", {}).get("sheet_name", "")
    column_name = request.get("data", {}).get("column_name", "")

    unique_index_list_cleaned = []

    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.xlsx':
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')
    elif file_extension == '.xls':
        df = pd.read_excel(file_path, sheet_name=sheet_name, engine='xlrd')

    unique_index_np = df[column_name].unique()
    unique_index_list = unique_index_np.tolist()

    for item in unique_index_list:
        if not isinstance(item, (int, float)):                              # 检查item是否是int或float类型
            unique_index_list_cleaned.append(item.replace('\t', ''))        # 移除字符串中的所有制表符（\t）
        else:
            unique_index_list_cleaned.append(item)

    return ['unique_index', unique_index_list_cleaned]