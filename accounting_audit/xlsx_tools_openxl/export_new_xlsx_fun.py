# export_new_xlsx_fun.py

# 导出新 xlsx 文件

from tkinter import filedialog
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows

def export_new_xlsx(df):

    # 实例化工作簿
    wb = openpyxl.Workbook()

    # 获取第一张工作表并赋予它一个名称
    ws = wb.active

    # 将DataFrame的数据添加到Excel工作表
    for r in dataframe_to_rows(df, index=False, header=True):
        ws.append(r)

    # 调整列宽
    for column_cells in ws.columns:
        length = max(len(str(cell.value))+8 for cell in column_cells)
        ws.column_dimensions[column_cells[0].column_letter].width = length
    
    # 保存工作簿会在磁盘上创建文件
    file_path = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel Files', '*.xlsx')])
    wb.save(file_path)

    info = f'The xlsx output file path: {file_path}\nThe xlsx output file was exported successfully!\n'

    return [True, info, file_path]