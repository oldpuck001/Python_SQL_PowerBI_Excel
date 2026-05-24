# create_new_xlsx_fun.py

import openpyxl

# 新建工作簿

def create_new_xlsx(file_path, sheet_name_list):
    
    # 实例化工作簿
    wb = openpyxl.Workbook()

    # 获取第一张工作表并赋予它一个名称
    ws_1 = wb.active
    ws_1.title = sheet_name_list[0]

    # 获取第二张工作表并赋予它一个名称
    for t in sheet_name_list[1:]:
        wb.create_sheet(title=t)

    # 保存工作簿会在磁盘上创建文件
    wb.save(file_path)

    return f'The xlsx output file path: {file_path}\nThe xlsx output file was created successfully!\n'