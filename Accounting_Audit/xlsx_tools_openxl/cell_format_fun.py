# cell_format_fun.py

# 单元格格式

import openpyxl
from openpyxl.styles import Alignment

def cell_format(cell_fill, n):

    # 边框格式
    thin_border = openpyxl.styles.Border(left=openpyxl.styles.Side(style='thin'),
                                         right=openpyxl.styles.Side(style='thin'),
                                         top=openpyxl.styles.Side(style='thin'),
                                         bottom=openpyxl.styles.Side(style='thin'))

    if n == 1:
        cell_fill.border = thin_border
        cell_fill.alignment = Alignment(horizontal='center', vertical='center')

    elif n == 2:
        cell_fill.border = thin_border
        cell_fill.alignment = Alignment(vertical='center')

    elif n == 3:
        cell_fill.border = thin_border
        cell_fill.alignment = Alignment(horizontal='center', vertical='center')

    elif n == 4:
        cell_fill.border = thin_border
        cell_fill.alignment = Alignment(vertical='center')
        cell_fill.number_format = '#,##0.00'
    
    elif n == 5:
        cell_fill.border = thin_border
        cell_fill.alignment = Alignment(vertical='center')
        cell_fill.number_format = 'yyyy-mm-dd'

    return