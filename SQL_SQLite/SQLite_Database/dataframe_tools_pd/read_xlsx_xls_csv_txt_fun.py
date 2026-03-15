# read_xlsx_xls_csv_txt_fun.py

# 读取数据文件

import os
import pandas as pd

def read_xlsx_xls_csv_txt(file_path = None,
                          sheet_name = 0,                     # 默认读取第一个工作表 (索引0)
                          skiprows = None,                    # 默认不跳过任何行
                          usecols = None,                     # 默认读取所有列
                          nrows = None,                       # 默认读取所有行
                          index_col = None,                   # 默认无索引列（生成RangeIndex）
                          header = 0,                         # 默认第0行（第一行）作为列名，设为 None 时无列名
                          names = None,                       # 默认使用Excel中的列名（由header决定）。提供列表将覆盖现有列名，通常与 header=None 配合使用
                          na_values = None,                   # 默认无额外空值标识。提供字符串、列表或字典（按列指定），将指定值识别为NaN
                          keep_default_na = True,             # 默认启用pandas内置空值识别（如"", "#N/A", "NULL"等）。设为False则仅识别na_values指定的空值
                          dtype = None,                       # 默认自动推断列数据类型。字典格式：{列名: 数据类型}，强制指定列的数据类型
                          converters = None,                  # 默认无列转换函数。字典格式：{列索引/列名: 函数}，在读取时对指定列应用函数
                          sep=',',                            # csv参数，默认逗号
                          encoding='utf-8',                   # csv参数，默认utf-8
                          engine_csv='c'                      # csv参数，默认c
                        ):

    skiprows        = None if skiprows == 'None'        or skiprows == None         else int(skiprows)
    usecols         = None if usecols == 'None'         or usecols == None          else usecols
    nrows           = None if nrows == 'None'           or nrows == None            else nrows
    index_col       = None if index_col == 'None'       or index_col == None        else index_col 
    header          = 0    if header == '0'             or header == 0              else int(header)
    names           = None if names == 'None'           or names == None            else names
    na_values       = None if na_values == 'None'       or na_values == None        else na_values
    keep_default_na = True if keep_default_na == 'True' or keep_default_na == True  else False
    dtype           = None if dtype == 'None'           or dtype == None            else dtype
    converters      = None if converters == 'None'      or converters == None       else converters

    try:
        file_extension = os.path.splitext(file_path)[1].lower()

        if file_extension in ['.xlsx', '.xls']:
            if file_extension == '.xlsx':
                engine = 'openpyxl'
            elif file_extension == '.xls':
                engine = 'xlrd'
            df = pd.read_excel(file_path,
                               sheet_name = sheet_name,             # 默认读取第一个工作表 (索引0)
                               skiprows = skiprows,                 # 默认不跳过任何行
                               usecols = usecols,                   # 默认读取所有列
                               nrows = nrows,                       # 默认读取所有行
                               index_col = index_col,               # 默认无索引列（生成RangeIndex）
                               header = header,                     # 默认第0行（第一行）作为列名，设为 None 时无列名
                               names = names,                       # 默认使用Excel中的列名（由header决定）。提供列表将覆盖现有列名，通常与 header=None 配合使用
                               na_values = na_values,               # 默认无额外空值标识。提供字符串、列表或字典（按列指定），将指定值识别为NaN
                               keep_default_na = keep_default_na,   # 默认启用pandas内置空值识别（如"", "#N/A", "NULL"等）。设为False则仅识别na_values指定的空值
                               dtype = dtype,                       # 默认自动推断列数据类型。字典格式：{列名: 数据类型}，强制指定列的数据类型
                               converters = converters,             # 默认无列转换函数。字典格式：{列索引/列名: 函数}，在读取时对指定列应用函数
                               engine = engine)

        elif file_extension in ['.csv', '.txt']:
            if file_extension == '.csv':
                engine = engine_csv
            elif file_extension == '.txt':
                engine = 'python'
            df = pd.read_csv(file_path,
                             sep = sep,                          # 默认逗号
                             encoding = encoding,                # 默认utf-8
                             skiprows = skiprows,                # 默认不跳过任何行
                             usecols = usecols,                  # 默认读取所有列
                             nrows = nrows,                      # 默认读取所有行
                             index_col = index_col,              # 默认无索引列（生成RangeIndex）
                             header = header,                    # 默认第0行（第一行）作为列名，设为 None 时无列名
                             names = names,                      # 默认使用Excel中的列名（由header决定）。提供列表将覆盖现有列名，通常与 header=None 配合使用
                             na_values = na_values,              # 默认无额外空值标识。提供字符串、列表或字典（按列指定），将指定值识别为NaN
                             keep_default_na = keep_default_na,  # 默认启用pandas内置空值识别（如"", "#N/A", "NULL"等）。设为False则仅识别na_values指定的空值
                             dtype = dtype,                      # 默认自动推断列数据类型。字典格式：{列名: 数据类型}，强制指定列的数据类型
                             converters = converters,            # 默认无列转换函数。字典格式：{列索引/列名: 函数}，在读取时对指定列应用函数
                             engine = engine)

        else:
            info = 'Data file format is not supported.\nPlease try importing again.\n'
            df = pd.DataFrame()
            return [False, info, df]

    except Exception as e:
        info = f'Data file reading failed.\nPlease try importing again.\n{e}\n'
        df = pd.DataFrame()
        return [False, info, df]

    info = 'Data file read successfully!\n'
    return [True, info, df]