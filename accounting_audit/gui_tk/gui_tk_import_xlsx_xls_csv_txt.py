# gui_tk_import_xlsx_xls_csv_txt.py

import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from gui_tk import gui_tk_area_text
from dataframe_tools_pd import sheetnames_import_fun
from dataframe_tools_pd import read_xlsx_xls_csv_txt_fun
from dataframe_tools_pd import df_review_xlsx_fun
from dataframe_tools_pd import df_cleaning_fun

class gui_tk_import_xlsx_xls_csv_txt_class:

    def __init__(self):

        self.result_df = None
        self.path = ''
        self.sheet_name = ''

    def gui_tk_import_xlsx_xls_csv_txt_frame(self, root):

        import_sheet_win = tk.Toplevel(root)
        import_sheet_win.title('Import Sheet Data')
        import_sheet_win.geometry('1280x480+120+120')
        import_sheet_win.resizable(False, False)

        options_blank = []  
        options_T_F = [True, False]
        options_clean = ['删除指定列的重复行',
                         '填充缺失值为 0',
                         '填充缺失值为 <空白>',
                         '填充缺失值为 重复上一行',
                         '标准化文本（去除首尾空格及转换为小写英文字母）',
                         '将数据类型转换为字符型',
                         '转换为整数，支持缺失值',
                         '转换为浮点数，支持缺失值',
                         '将数据类型转换为时间日期类型']

        # 地址栏行
        frame_1 = tk.Frame(import_sheet_win)
        frame_1.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_1, text='File Path', width=6, anchor='w').pack(side=tk.LEFT, padx=5, pady=(10, 5))
        frame_1.entry_path = tk.Entry(frame_1, state='readonly', readonlybackground='white', width=105)           # 创建Entry并保存引用
        frame_1.entry_path.pack(side=tk.LEFT, expand=True, padx=5, pady=(10, 5))
        tk.Button(frame_1, text='选择导入文件',
                  command=lambda: self.select_open_file_path(frame_1.entry_path, frame_8.text_area),
                  width=17).pack(side=tk.LEFT, padx=(5, 15), pady=(10, 5))

        # 选择工作表与按钮列
        frame_2 = tk.Frame(import_sheet_win)
        frame_2.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_2, text='Excel sheet', width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_2.combobox_sheet = ttk.Combobox(frame_2, values=options_blank, height=10, width=55, state='readonly')     # 使用 ttk.Combobox（现代下拉选框）
        frame_2.combobox_sheet.pack(side=tk.LEFT, padx=(5,30), pady=5)
        tk.Button(frame_2, text='读取工作表清单',
                  command=lambda: self.button_sheets_fun(frame_1.entry_path, frame_2.combobox_sheet, frame_8.text_area),
                  width=17).pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Button(frame_2, text='读取参数说明',
                  command=lambda: self.button_manual_fun(),
                  width=17).pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Button(frame_2, text='读取数据',
                  command=lambda: self.button_load_fun(frame_1.entry_path,
                                                       frame_2.combobox_sheet,
                                                       frame_3.entry_skiprows,
                                                       frame_3.entry_usecols,
                                                       frame_3.entry_nrows,
                                                       frame_3.entry_index_col,
                                                       frame_4.entry_header,
                                                       frame_4.entry_names,
                                                       frame_4.entry_na_values,
                                                       frame_4.combobox_keep_default_na,
                                                       frame_5.entry_dtype,
                                                       frame_5.entry_sep,
                                                       frame_5.entry_encoding,
                                                       frame_6.entry_converters,
                                                       frame_6.entry_engine_csv,
                                                       frame_7.combobox_col,
                                                       frame_8.text_area),
                  width=17).pack(side=tk.LEFT, padx=(5, 5), pady=5)

        # 读取文件参数区
        frame_3 = tk.Frame(import_sheet_win)
        frame_3.pack(side=tk.TOP, fill=tk.BOTH)

        tk.Label(frame_3, text='skiprows', width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_3.entry_skiprows = tk.Entry(frame_3, width=20)
        frame_3.entry_skiprows.pack(side=tk.LEFT, padx=(5, 40), pady=5)
        frame_3.entry_skiprows.insert(0, 'None')

        tk.Label(frame_3, text='usecols', width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_3.entry_usecols = tk.Entry(frame_3, width=20)
        frame_3.entry_usecols.pack(side=tk.LEFT, padx=(5, 40), pady=5)
        frame_3.entry_usecols.insert(0, 'None')

        tk.Label(frame_3, text='nrows', width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_3.entry_nrows = tk.Entry(frame_3, width=20)
        frame_3.entry_nrows.pack(side=tk.LEFT, padx=(5, 40), pady=5)
        frame_3.entry_nrows.insert(0, 'None')

        tk.Label(frame_3, text='index_col', width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_3.entry_index_col = tk.Entry(frame_3, width=20)
        frame_3.entry_index_col.pack(side=tk.LEFT, padx=(5, 5), pady=5)
        frame_3.entry_index_col.insert(0, 'None')

        frame_4 = tk.Frame(import_sheet_win)
        frame_4.pack(side=tk.TOP, fill=tk.BOTH)

        tk.Label(frame_4, text='header', width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_4.entry_header = tk.Entry(frame_4, width=20)
        frame_4.entry_header.pack(side=tk.LEFT, padx=(5, 40), pady=5)
        frame_4.entry_header.insert(0, 0)

        tk.Label(frame_4, text='names', width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_4.entry_names = tk.Entry(frame_4, width=20)
        frame_4.entry_names.pack(side=tk.LEFT, padx=(5, 40), pady=5)
        frame_4.entry_names.insert(0, 'None')

        tk.Label(frame_4, text='na_values', width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_4.entry_na_values = tk.Entry(frame_4, width=20)
        frame_4.entry_na_values.pack(side=tk.LEFT, padx=(5, 40), pady=5)
        frame_4.entry_na_values.insert(0, 'None')

        tk.Label(frame_4, text='keep_default_na', width=12, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_4.combobox_keep_default_na = ttk.Combobox(frame_4, values=options_T_F, height=2, width=15, state='readonly')
        frame_4.combobox_keep_default_na.set('True')
        frame_4.combobox_keep_default_na.pack(side=tk.LEFT, padx=(5, 5), pady=5)

        frame_5 = tk.Frame(import_sheet_win)
        frame_5.pack(side=tk.TOP, fill=tk.BOTH)

        tk.Label(frame_5, text='dtype', width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_5.entry_dtype = tk.Entry(frame_5, width=56)
        frame_5.entry_dtype.pack(side=tk.LEFT, padx=(5, 40), pady=5)
        frame_5.entry_dtype.insert(0, 'None')

        tk.Label(frame_5, text='sep', width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_5.entry_sep = tk.Entry(frame_5, width=20)
        frame_5.entry_sep.pack(side=tk.LEFT, padx=(5, 40), pady=5)
        frame_5.entry_sep.insert(0, ',')

        tk.Label(frame_5, text='encoding', width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_5.entry_encoding = tk.Entry(frame_5, width=20)
        frame_5.entry_encoding.pack(side=tk.LEFT, padx=(5, 5), pady=5)
        frame_5.entry_encoding.insert(0, 'utf-8')

        frame_6 = tk.Frame(import_sheet_win)
        frame_6.pack(side=tk.TOP, fill=tk.BOTH)

        tk.Label(frame_6, text='converters', width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_6.entry_converters = tk.Entry(frame_6, width=92)
        frame_6.entry_converters.pack(side=tk.LEFT, padx=(5, 40), pady=5)
        frame_6.entry_converters.insert(0, 'None')

        tk.Label(frame_6, text='engine_csv', width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_6.entry_engine_csv = tk.Entry(frame_6, width=20)
        frame_6.entry_engine_csv.pack(side=tk.LEFT, padx=(5, 5), pady=5)
        frame_6.entry_engine_csv.insert(0, 'c')

        frame_7 = tk.Frame(import_sheet_win)
        frame_7.pack(side=tk.TOP, fill=tk.BOTH)

        tk.Label(frame_7, text='DataFrame column', width=15, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        options_col = []
        frame_7.combobox_col = ttk.Combobox(frame_7, values=options_col, height=10, width=25, state='readonly')
        frame_7.combobox_col.pack(side=tk.LEFT, padx=(5, 20), pady=5)

        tk.Label(frame_7, text='数据清洗选项', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_7.combobox_clean = ttk.Combobox(frame_7, values=options_clean, height=10, width=33, state='readonly')
        frame_7.combobox_clean.set(options_clean[7])
        frame_7.combobox_clean.pack(side=tk.LEFT, padx=(5, 20), pady=5)

        tk.Button(frame_7, text='数据预览',
                  command=lambda: self.button_preview_fun(frame_8.text_area),
                  width=10).pack(side=tk.LEFT, padx=(5, 5), pady=5)
        tk.Button(frame_7, text='数据清洗',
                  command=lambda: self.button_clean_fun(frame_7.combobox_col, frame_7.combobox_clean, frame_8.text_area),
                  width=10).pack(side=tk.LEFT, padx=(5, 5), pady=5)
        tk.Button(frame_7, text='返回数据',
                  command=lambda: self.button_return_fun(import_sheet_win),
                  width=10).pack(side=tk.LEFT, padx=(5, 5), pady=5)

        # 操作记录
        frame_8 = tk.Frame(import_sheet_win)
        frame_8.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_8, text='Operation Log', anchor='w').pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        frame_8.text_area = ScrolledText(frame_8, height=15)
        frame_8.text_area.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        frame_8.text_area.config(state='disabled')

        return import_sheet_win


    # 选择文件按钮函数
    def select_open_file_path(self, entry_path, sub_text_area):

        fill_text = ''

        path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx'),
                                                     ('Excel Files', '*.xls'),
                                                     ('CSV Files', '*.csv'),
                                                     ('Text Files', '*.txt'),
                                                     ('All Files', '*.*')])

        if path:
            entry_path.config(state='normal')
            entry_path.delete(0, tk.END)
            entry_path.insert(0, path)
            entry_path.config(state='readonly')
            fill_text += f'Selected: {path}\n'
            fill_text += 'File selection successful!\n'
        else:
            fill_text += f'File selection failed!\n'

        gui_tk_area_text.text_area_fill(sub_text_area, fill_text)


    # 读取工作表列表按钮函数
    def button_sheets_fun(self, entry_path, combobox_sheets, sub_text_area):

        path = entry_path.get()

        if path:
            result_info = sheetnames_import_fun.sheetnames_import(path)
            if result_info[0]:
                combobox_sheets['values'] = result_info[2]
                combobox_sheets.set(result_info[2][0])                                     # 设置默认选择第一个
                combobox_sheets.config(state='readonly')
            else:
                combobox_sheets.set('')
                combobox_sheets.config(state='disabled')

        fill_text = result_info[1]
        gui_tk_area_text.text_area_fill(sub_text_area, fill_text)


    # 读取参数说明按钮函数
    def button_manual_fun(self):
    
        win = tk.Toplevel()
        win.title('Pandas 参数说明')
        win.geometry("780x600")

        text = ScrolledText(win, wrap=tk.WORD, font=('Arial', 12))
        text.pack(expand=True, fill=tk.BOTH)

        params_text = """
    Pandas 文件读取常用参数说明（含输入格式）

    1. skiprows
    - 跳过开头的行数或指定跳过的行。
    - 输入格式：
        int → 跳过前 N 行
        list[int] → 指定跳过哪些行
        callable → 函数决定要跳过的行
        None → 不跳过

    2. usecols
    - 指定读取哪些列。
    - 输入格式：
        list[int] 或 list[str]
        callable
        字符串（如 "A:C"）
        None → 读取所有列

    3. nrows
    - 只读取前 N 行。
    - 输入格式：int 或 None

    4. index_col
    - 设置为索引的列。
    - 输入格式：int, str, list[int], list[str], None

    5. header
    - 指定哪一行作为列名。
    - 输入格式：
        int → 第 N 行作为列名
        list[int] → 多层表头
        None → 无列名

    6. names
    - 自定义列名（常与 header=None 搭配）。
    - 输入格式：list[str] 或 None

    7. na_values
    - 指定哪些值视为 NaN。
    - 输入格式：
        str、list[str]、dict、None

    8. keep_default_na
    - 是否保留 pandas 内建的空值识别。
    - 输入格式：True 或 False

    9. dtype
    - 指定各列的数据类型。
    - 输入格式：
        str → 整表统一类型（较少用）
        dict → {列名: 类型}
        None → 自动推断

    10. converters
        - 指定列转换函数。
        - 输入格式：{列名: 函数} 或 None

    11. sep
        - CSV 分隔符。
        - 输入格式：字符串（如 ',', '\\t', '|'）

    12. encoding
        - 文件编码格式。
        - 输入格式：'utf-8', 'utf-8-sig', 'latin1', 'gbk' 等

    13. engine_csv
        - CSV 解析引擎。
        - 输入格式：
            'c' → 默认、速度最快
            'python' → 更灵活但较慢
    """
        text.insert(tk.END, params_text)
        text.config(state="disabled")


    # 读取数据按钮函数
    def button_load_fun(self, entry_file, combobox_sheet, entry_skiprows, entry_usecols, entry_nrows, entry_index_col,
                        entry_header, entry_names, entry_na_values, combobox_keep_default_na, entry_dtype, entry_sep,
                        entry_encoding, entry_converters, entry_engine_csv, combobox_col, sub_text_area):

        self.path = entry_file.get()
        self.sheet_name = combobox_sheet.get()
        skiprows = entry_skiprows.get()
        usecols = entry_usecols.get()
        nrows = entry_nrows.get()
        index_col = entry_index_col.get()
        header = entry_header.get()
        names = entry_names.get()
        na_values = entry_na_values.get()
        keep_default_na = combobox_keep_default_na.get()
        dtype = entry_dtype.get()
        sep = entry_sep.get()
        encoding = entry_encoding.get()
        converters = entry_converters.get()
        engine_csv = entry_engine_csv.get()

        if self.path:
            result_info = read_xlsx_xls_csv_txt_fun.read_xlsx_xls_csv_txt(file_path=self.path,
                                                                          sheet_name=self.sheet_name,
                                                                          skiprows=skiprows,
                                                                          usecols=usecols,
                                                                          nrows=nrows,
                                                                          index_col=index_col,
                                                                          header=header,
                                                                          names=names,
                                                                          na_values=na_values,
                                                                          keep_default_na=keep_default_na,
                                                                          dtype=dtype,
                                                                          converters=converters,
                                                                          sep=sep,
                                                                          encoding=encoding,
                                                                          engine_csv=engine_csv)
            if result_info[0]:
                self.result_df = result_info[2]
                option_clean_cols = self.result_df.columns.tolist()
                combobox_col['values'] = option_clean_cols
                combobox_col.set(option_clean_cols[0])
                combobox_col.config(state='readonly')
            fill_text = result_info[1]
        else:
            fill_text = f'Please select a file first!\n'

        gui_tk_area_text.text_area_fill(sub_text_area, fill_text)


    # 数据预览
    def button_preview_fun(self, sub_text_area):

        fill_text = ''

        result_info = df_review_xlsx_fun.df_review_xlsx(self.result_df)

        fill_text += result_info[1]
        
        gui_tk_area_text.text_area_fill(sub_text_area, fill_text)


    # 数据清洗按钮函数
    def button_clean_fun(self, combobox_col, combobox_clean, sub_text_area):

        clean_col = combobox_col.get()
        clean_option = combobox_clean.get()

        if clean_option == '删除指定列的重复行':
            clean_option_label = 'drop_duplicates'
        elif clean_option == '填充缺失值为 0':
            clean_option_label = 'fillna_0'
        elif clean_option == '填充缺失值为 <空白>':
            clean_option_label = 'fillna_<blank>'
        elif clean_option == '填充缺失值为 重复上一行':
            clean_option_label = 'ffill'
        elif clean_option == '标准化文本（去除首尾空格及转换为小写英文字母）':
            clean_option_label = 'strip_lower'
        elif clean_option == '将数据类型转换为字符型':
            clean_option_label = 'to_str'
        elif clean_option == '转换为整数，支持缺失值':
            clean_option_label = 'to_int'
        elif clean_option == '转换为浮点数，支持缺失值':
            clean_option_label = 'to_float'
        elif clean_option == '将数据类型转换为时间日期类型':
            clean_option_label = 'to_datetime'

        result_info = df_cleaning_fun.df_cleaning(self.result_df, clean_col, clean_option_label)

        fill_text = result_info[1]
        gui_tk_area_text.text_area_fill(sub_text_area, fill_text)


    # 返回数据按钮函数
    def button_return_fun(self, import_sheet_win):

        import_sheet_win.destroy()