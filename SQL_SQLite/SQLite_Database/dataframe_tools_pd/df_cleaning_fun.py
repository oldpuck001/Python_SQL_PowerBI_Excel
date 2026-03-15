# df_cleaning_fun.py

# 数据清洗

import pandas as pd

def df_cleaning(df, clean_col, clean_option):

    info = f'DataFrame column: {clean_col}\n数据清洗选项：{clean_option}\n'

    try:
        if clean_option == 'drop_duplicates':
            df = df.drop_duplicates(subset=[clean_col])                                         # 删除指定列的重复行

        elif clean_option == 'fillna_0':
            df[clean_col] = df[clean_col].fillna(0)                                             # 填充缺失值为 0

        elif clean_option == 'fillna_<blank>':
            df[clean_col] = df[clean_col].fillna('<空白>')                                      # 填充缺失值为 '<空白>'

        elif clean_option == 'ffill':
            df[clean_col] = df[clean_col].ffill()                                               # 填充缺失值为 重复上一行

        elif clean_option == 'strip_lower':
            df[clean_col] = df[clean_col].str.strip().str.lower()                               # 标准化文本（去除首尾空格及转换为小写英文字母）

        elif clean_option == 'to_str':
            df[clean_col] = df[clean_col].astype(str)                                           # 将数据类型转换为字符型

        elif clean_option == 'to_int':
            df[clean_col] = df[clean_col].astype(str).str.replace(',', '')
            df[clean_col] = pd.to_numeric(df[clean_col], errors='coerce').fillna(0).astype(int) # 转换为整数，支持缺失值

        elif clean_option == 'to_float':
            df[clean_col] = df[clean_col].astype(str).str.replace(',', '')
            df[clean_col] = pd.to_numeric(df[clean_col], errors='coerce').fillna(0)             # 转换为浮点数，支持缺失值

        elif clean_option == 'to_datetime':
            df[clean_col] = pd.to_datetime(df[clean_col], errors='coerce')                      # 将数据类型转换为时间日期类型


        info += 'Data cleaning successful!\n'
        return [True, info, df]
    
    except:

        info += 'Data cleaning failed!\n'
        return [False, info, df]