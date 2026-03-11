# df_review_xlsx_fun.py

# 在Excel中预览DataFrame

import os
import tempfile

def df_review_xlsx(df):

    with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as temp_file:
        temp_path = temp_file.name

    df.to_excel(temp_path, index=False)

    # macOS
    if os.name == 'posix':
        os.system(f'open "{temp_path}"')

    # Windows
    elif os.name == 'nt':
        os.startfile(temp_path)

    info = f'Preview file: {temp_path}\n'

    return [True, info, temp_path]
