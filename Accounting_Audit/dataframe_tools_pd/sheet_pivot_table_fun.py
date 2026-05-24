# sheet_pivot_table_fun.py

import pandas as pd
from dataframe_tools_pd import read_xlsx_xls_csv_txt_fun
from dataframe_tools_pd import df_cleaning_fun

def sheet_pivot_table(file_path, sheet_name, row_value, column_value, subtotal_value):

    result = read_xlsx_xls_csv_txt_fun.read_xlsx_xls_csv_txt(file_path=file_path, sheet_name=sheet_name)

    if result[0]:

        df = result[2]
        
        result_info = df_cleaning_fun.df_cleaning(df, subtotal_value, 'to_float')

        if result_info[0]:

            df_cleaned = result_info[2]
            df_export = pd.pivot_table(df_cleaned.iloc[0:], values=subtotal_value, index=row_value, columns=column_value, aggfunc='sum')
            info = 'Data pivoting was successful.'

            return [True, info, df_export]
        
        else:

            info = 'Data pivoting failed.'
            return [False, info]

    else:

        info = 'Data import failed.'
        return [False, info]






