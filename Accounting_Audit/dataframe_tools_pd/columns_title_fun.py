# columns_title_fun.py

from dataframe_tools_pd import read_xlsx_xls_csv_txt_fun

def columns_title(file_path, sheet_name):

    result = read_xlsx_xls_csv_txt_fun.read_xlsx_xls_csv_txt(file_path=file_path, sheet_name=sheet_name)

    info = result[1]

    if result[0]:

        df = result[2]
        columns_title = df.columns.tolist()
        return [True, info, columns_title]
    
    else:

        columns_title = []
        return [False, info, columns_title]