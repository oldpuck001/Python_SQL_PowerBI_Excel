# gui_tk_account_data_clean.py

import subprocess
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from dataframe_tools_pd import columns_title_fun
from dataframe_tools_pd import sheetnames_import_fun
from dataframe_tools_pd import read_xlsx_xls_csv_txt_fun
from dataframe_tools_pd import df_review_xlsx_fun
from xlsx_tools_openxl import export_account_data_fun
from gui_tk import gui_tk_area_text

class gui_tk_account_data_clean_class:

    file_path_result = ''
    df_balance = pd.DataFrame(columns=['科目编码', '科目名称', '期初借方', '期初贷方', '本期借方', '本期贷方', '期末借方', '期末贷方'])
    df_chronological = pd.DataFrame(columns=['涉及科目', '日期', '凭证字号', '科目编码', '科目名称', '摘要', '对方科目',
                                             '借方金额', '贷方金额', '现金流量表项目'])

    def gui_tk_account_data_clean_frame(self, root, control_frame_config, text_area):

        frame_result = tk.Frame(root)
        frame_result.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=(10, 5))

        # 按钮
        self.frame_button = tk.Frame(frame_result)
        self.frame_button.pack(side=tk.TOP, fill=tk.BOTH)

        tk.Button(self.frame_button, text=control_frame_config['widget_text'][0],
                  command=lambda: self.account_balance(root),
                  width=15).pack(side=tk.LEFT, padx=(50, 5), pady=5)
        
        tk.Button(self.frame_button, text=control_frame_config['widget_text'][1],
                  command=lambda: self.account_chronological(root),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)
        
        tk.Button(self.frame_button, text=control_frame_config['widget_text'][2],
                  command=lambda: self.export_file(text_area),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)

        return frame_result


    # 导入科目余额表子窗口
    def account_balance(self, root):

        option_blank = []
        option_model = ['借方列贷方列双列模式', '借贷方向列借贷金额列模式']
        widget_text = ['File Path', '选择工作表', '期初期末列模式', '科目编码列', '科目名称列', '期初借方列', '期初贷方列',
                       '期初方向列', '期初金额列', '本期借方列', '本期贷方列', '期末借方列', '期末贷方列', '期末方向列', '期末金额列',
                       '选择文件', '导入并预览', '关闭窗口']

        top = tk.Toplevel(root)
        top.title('导入科目余额表')
        top.geometry('680x340+200+200')
        top.resizable(False, False)

        frame_path = tk.Frame(top)
        frame_path.pack(side=tk.TOP, fill=tk.BOTH, pady=(5, 0))
        tk.Label(frame_path, text=widget_text[0], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_path.entry_path = tk.Entry(frame_path, state='readonly', readonlybackground='white')
        frame_path.entry_path.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 10), pady=5)

        frame_sheet_model = tk.Frame(top)
        frame_sheet_model.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_sheet_model, text=widget_text[1], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_sheet_model.combobox_sheet = ttk.Combobox(frame_sheet_model, values=option_blank, state='readonly', width=20)
        frame_sheet_model.combobox_sheet.pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Label(frame_sheet_model, text=widget_text[2], width=10, anchor='w').pack(side=tk.LEFT, padx=(20, 5), pady=5)
        frame_sheet_model.combobox_model = ttk.Combobox(frame_sheet_model, values=option_model, state='readonly', width=20)
        frame_sheet_model.combobox_model.set(option_model[0])
        frame_sheet_model.combobox_model.pack(side=tk.LEFT, padx=(5, 10), pady=5)

        frame_num_name = tk.Frame(top)
        frame_num_name.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_num_name, text=widget_text[3], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_num_name.combobox_num = ttk.Combobox(frame_num_name, values=option_blank, state='readonly', width=20)
        frame_num_name.combobox_num.pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Label(frame_num_name, text=widget_text[4], width=10, anchor='w').pack(side=tk.LEFT, padx=(20, 5), pady=5)
        frame_num_name.combobox_name = ttk.Combobox(frame_num_name, values=option_blank, state='readonly', width=20)
        frame_num_name.combobox_name.pack(side=tk.LEFT, padx=(5, 10), pady=5)

        frame_begin_double = tk.Frame(top)
        frame_begin_double.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_begin_double, text=widget_text[5], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_begin_double.combobox_begin_debit = ttk.Combobox(frame_begin_double, values=option_blank, state='readonly', width=20)
        frame_begin_double.combobox_begin_debit.pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Label(frame_begin_double, text=widget_text[6], width=10, anchor='w').pack(side=tk.LEFT, padx=(20, 5), pady=5)
        frame_begin_double.combobox_begin_credit = ttk.Combobox(frame_begin_double, values=option_blank, state='readonly', width=20)
        frame_begin_double.combobox_begin_credit.pack(side=tk.LEFT, padx=(5, 10), pady=5)

        frame_begin_single = tk.Frame(top)
        frame_begin_single.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_begin_single, text=widget_text[7], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_begin_single.combobox_begin_dc = ttk.Combobox(frame_begin_single, values=option_blank, state='readonly', width=20)
        frame_begin_single.combobox_begin_dc.pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Label(frame_begin_single, text=widget_text[8], width=10, anchor='w').pack(side=tk.LEFT, padx=(20, 5), pady=5)
        frame_begin_single.combobox_begin_value = ttk.Combobox(frame_begin_single, values=option_blank, state='readonly', width=20)
        frame_begin_single.combobox_begin_value.pack(side=tk.LEFT, padx=(5, 10), pady=5)

        frame_this = tk.Frame(top)
        frame_this.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_this, text=widget_text[9], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_this.combobox_this_debit = ttk.Combobox(frame_this, values=option_blank, state='readonly', width=20)
        frame_this.combobox_this_debit.pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Label(frame_this, text=widget_text[10], width=10, anchor='w').pack(side=tk.LEFT, padx=(20, 5), pady=5)
        frame_this.combobox_this_credit = ttk.Combobox(frame_this, values=option_blank, state='readonly', width=20)
        frame_this.combobox_this_credit.pack(side=tk.LEFT, padx=(5, 10), pady=5)

        frame_end_double = tk.Frame(top)
        frame_end_double.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_end_double, text=widget_text[11], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_end_double.combobox_end_debit = ttk.Combobox(frame_end_double, values=option_blank, state='readonly', width=20)
        frame_end_double.combobox_end_debit.pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Label(frame_end_double, text=widget_text[12], width=10, anchor='w').pack(side=tk.LEFT, padx=(20, 5), pady=5)
        frame_end_double.combobox_end_credit = ttk.Combobox(frame_end_double, values=option_blank, state='readonly', width=20)
        frame_end_double.combobox_end_credit.pack(side=tk.LEFT, padx=(5, 10), pady=5)

        frame_end_single = tk.Frame(top)
        frame_end_single.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_end_single, text=widget_text[13], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_end_single.combobox_end_dc = ttk.Combobox(frame_end_single, values=option_blank, state='readonly', width=20)
        frame_end_single.combobox_end_dc.pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Label(frame_end_single, text=widget_text[14], width=10, anchor='w').pack(side=tk.LEFT, padx=(20, 5), pady=5)
        frame_end_single.combobox_end_value = ttk.Combobox(frame_end_single, values=option_blank, state='readonly', width=20)
        frame_end_single.combobox_end_value.pack(side=tk.LEFT, padx=(5, 10), pady=5)

        frame_button = tk.Frame(top)
        frame_button.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)

        tk.Button(frame_button, text=widget_text[15],
                  command=lambda: self.select_balance(frame_path.entry_path,
                                                      frame_sheet_model.combobox_sheet,
                                                      frame_num_name.combobox_num,
                                                      frame_num_name.combobox_name,
                                                      frame_begin_double.combobox_begin_debit,
                                                      frame_begin_double.combobox_begin_credit,
                                                      frame_begin_single.combobox_begin_dc,
                                                      frame_begin_single.combobox_begin_value,
                                                      frame_this.combobox_this_debit,
                                                      frame_this.combobox_this_credit,
                                                      frame_end_double.combobox_end_debit,
                                                      frame_end_double.combobox_end_credit,
                                                      frame_end_single.combobox_end_dc,
                                                      frame_end_single.combobox_end_value),
                  width=15).pack(side=tk.LEFT, padx=(65, 5), pady=5)

        tk.Button(frame_button, text=widget_text[16],
                  command=lambda: self.import_review_balance(frame_path.entry_path,
                                                             frame_sheet_model.combobox_sheet,
                                                             frame_sheet_model.combobox_model,
                                                             frame_num_name.combobox_num,
                                                             frame_num_name.combobox_name,
                                                             frame_begin_double.combobox_begin_debit,
                                                             frame_begin_double.combobox_begin_credit,
                                                             frame_begin_single.combobox_begin_dc,
                                                             frame_begin_single.combobox_begin_value,
                                                             frame_this.combobox_this_debit,
                                                             frame_this.combobox_this_credit,
                                                             frame_end_double.combobox_end_debit,
                                                             frame_end_double.combobox_end_credit,
                                                             frame_end_single.combobox_end_dc,
                                                             frame_end_single.combobox_end_value),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)
    
        tk.Button(frame_button, text=widget_text[17],
                  command=top.destroy,
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)

        frame_sheet_model.combobox_sheet.bind('<<ComboboxSelected>>',
                                              lambda event: self.balance_change(event,
                                                                                frame_path.entry_path,
                                                                                frame_sheet_model.combobox_sheet,
                                                                                frame_num_name.combobox_num,
                                                                                frame_num_name.combobox_name,
                                                                                frame_begin_double.combobox_begin_debit,
                                                                                frame_begin_double.combobox_begin_credit,
                                                                                frame_begin_single.combobox_begin_dc,
                                                                                frame_begin_single.combobox_begin_value,
                                                                                frame_this.combobox_this_debit,
                                                                                frame_this.combobox_this_credit,
                                                                                frame_end_double.combobox_end_debit,
                                                                                frame_end_double.combobox_end_credit,
                                                                                frame_end_single.combobox_end_dc,
                                                                                frame_end_single.combobox_end_value))

        top.transient(root)                    # 依附主窗口
        top.grab_set()                         # 禁止操作主窗口
        root.wait_window(top)                  # 等待子窗口关闭


    # 更新下拉列表框
    def balance_change(self, event, entry_path, combobox_sheet, combobox_num, combobox_name,
                       combobox_begin_debit, combobox_begin_credit, combobox_begin_dc, combobox_begin_value,
                       combobox_this_debit, combobox_this_credit,
                       combobox_end_debit, combobox_end_credit, combobox_end_dc, combobox_end_value):

        path = entry_path.get()
        sheet_name = combobox_sheet.get()

        result = columns_title_fun.columns_title(path, sheet_name)

        if result[0]:

            new_options = result[2]

            combobox_num['values'] = new_options
            combobox_num.set(new_options[0])
            combobox_num.config(state='readonly')
            
            combobox_name['values'] = new_options
            combobox_name.set(new_options[0])
            combobox_name.config(state='readonly')

            combobox_begin_debit['values'] = new_options
            combobox_begin_debit.set(new_options[0])
            combobox_begin_debit.config(state='readonly')

            combobox_begin_credit['values'] = new_options
            combobox_begin_credit.set(new_options[0])
            combobox_begin_credit.config(state='readonly')

            combobox_begin_dc['values'] = new_options
            combobox_begin_dc.set(new_options[0])
            combobox_begin_dc.config(state='readonly')

            combobox_begin_value['values'] = new_options
            combobox_begin_value.set(new_options[0])
            combobox_begin_value.config(state='readonly')

            combobox_this_debit['values'] = new_options
            combobox_this_debit.set(new_options[0])
            combobox_this_debit.config(state='readonly')

            combobox_this_credit['values'] = new_options
            combobox_this_credit.set(new_options[0])
            combobox_this_credit.config(state='readonly')

            combobox_end_debit['values'] = new_options
            combobox_end_debit.set(new_options[0])
            combobox_end_debit.config(state='readonly')

            combobox_end_credit['values'] = new_options
            combobox_end_credit.set(new_options[0])
            combobox_end_credit.config(state='readonly')

            combobox_end_dc['values'] = new_options
            combobox_end_dc.set(new_options[0])
            combobox_end_dc.config(state='readonly')

            combobox_end_value['values'] = new_options
            combobox_end_value.set(new_options[0])
            combobox_end_value.config(state='readonly')


    # 选择科目余额表文件
    def select_balance(self, entry_path, combobox_sheet, combobox_num, combobox_name,
                       combobox_begin_debit, combobox_begin_credit, combobox_begin_dc, combobox_begin_value,
                       combobox_this_debit, combobox_this_credit,
                       combobox_end_debit, combobox_end_credit, combobox_end_dc, combobox_end_value):

        path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx'),
                                                     ('Excel Files', '*.xls')])
        
        if path:
            
            entry_path.config(state='normal')
            entry_path.delete(0, tk.END)
            entry_path.insert(0, path)
            entry_path.config(state='readonly')

            sheets_name_result = sheetnames_import_fun.sheetnames_import(path)

            if sheets_name_result[0]:

                sheets_name_list = sheets_name_result[2]

                combobox_sheet['values'] = sheets_name_list
                combobox_sheet.set(sheets_name_list[0])
                combobox_sheet.config(state='readonly')

                self.balance_change(None, entry_path, combobox_sheet, combobox_num, combobox_name,
                                    combobox_begin_debit, combobox_begin_credit, combobox_begin_dc, combobox_begin_value,
                                    combobox_this_debit, combobox_this_credit,
                                    combobox_end_debit, combobox_end_credit, combobox_end_dc, combobox_end_value)


    # 导入、预览科目余额表
    def import_review_balance(self, entry_path, combobox_sheet, combobox_model, combobox_num, combobox_name,
                              combobox_begin_debit, combobox_begin_credit, combobox_begin_dc, combobox_begin_value,
                              combobox_this_debit, combobox_this_credit,
                              combobox_end_debit, combobox_end_credit, combobox_end_dc, combobox_end_value):

        path = entry_path.get()
        sheet_name = combobox_sheet.get()
        model = combobox_model.get()
        num = combobox_num.get()
        name = combobox_name.get()
        begin_debit = combobox_begin_debit.get()
        begin_credit = combobox_begin_credit.get()
        begin_dc = combobox_begin_dc.get()
        begin_value = combobox_begin_value.get()
        this_debit = combobox_this_debit.get()
        this_credit = combobox_this_credit.get()
        end_debit = combobox_end_debit.get()
        end_credit = combobox_end_credit.get()
        end_dc = combobox_end_dc.get()
        end_value = combobox_end_value.get()

        # 读入数据
        result_info = read_xlsx_xls_csv_txt_fun.read_xlsx_xls_csv_txt(file_path=path, sheet_name=sheet_name)

        if result_info[0]:

            df = result_info[2]

            self.df_balance[['科目编码']] = df[[num]]
            self.df_balance[['科目名称']] = df[[name]]
            self.df_balance[['本期借方']] = df[[this_debit]]
            self.df_balance[['本期贷方']] = df[[this_credit]]

            if model == '借方列贷方列双列模式':

                self.df_balance[['期初借方']] = df[[begin_debit]]
                self.df_balance[['期初贷方']] = df[[begin_credit]]
                self.df_balance[['期末借方']] = df[[end_debit]]
                self.df_balance[['期末贷方']] = df[[end_credit]]

            else:

                self.df_balance['期初借方'] = df.loc[df[begin_dc] == '借', begin_value]
                self.df_balance['期初贷方'] = df.loc[df[begin_dc] == '贷', begin_value]
                self.df_balance['期末借方'] = df.loc[df[end_dc] == '借', end_value]
                self.df_balance['期末贷方'] = df.loc[df[end_dc] == '贷', end_value]

        df_review_xlsx_fun.df_review_xlsx(self.df_balance)


    # 导入序时账子窗口
    def account_chronological(self, root):

        option_blank = []
        widget_text = ['File Path', '选择工作表', '凭证日期列', '凭证字号列', '摘要文本列', '科目编码列', '科目名称列',
                       '对方科目列', '现流项目列', '借方金额列', '贷方金额列', '选择文件', '导入并预览', '关闭窗口']

        top = tk.Toplevel(root)
        top.title('导入序时账')
        top.geometry('680x275+200+200')
        top.resizable(False, False)

        frame_path = tk.Frame(top)
        frame_path.pack(side=tk.TOP, fill=tk.BOTH, pady=(5, 0))
        tk.Label(frame_path, text=widget_text[0], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_path.entry_path = tk.Entry(frame_path, state='readonly', readonlybackground='white')
        frame_path.entry_path.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 10), pady=5)

        frame_sheet_date = tk.Frame(top)
        frame_sheet_date.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_sheet_date, text=widget_text[1], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_sheet_date.combobox_sheet = ttk.Combobox(frame_sheet_date, values=option_blank, state='readonly', width=20)
        frame_sheet_date.combobox_sheet.pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Label(frame_sheet_date, text=widget_text[2], width=10, anchor='w').pack(side=tk.LEFT, padx=(20, 5), pady=5)
        frame_sheet_date.combobox_date = ttk.Combobox(frame_sheet_date, values=option_blank, state='readonly', width=20)
        frame_sheet_date.combobox_date.pack(side=tk.LEFT, padx=(5, 10), pady=5)

        frame_num_summary = tk.Frame(top)
        frame_num_summary.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_num_summary, text=widget_text[3], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_num_summary.combobox_num = ttk.Combobox(frame_num_summary, values=option_blank, state='readonly', width=20)
        frame_num_summary.combobox_num.pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Label(frame_num_summary, text=widget_text[4], width=10, anchor='w').pack(side=tk.LEFT, padx=(20, 5), pady=5)
        frame_num_summary.combobox_summary = ttk.Combobox(frame_num_summary, values=option_blank, state='readonly', width=20)
        frame_num_summary.combobox_summary.pack(side=tk.LEFT, padx=(5, 10), pady=5)

        frame_account_num_name = tk.Frame(top)
        frame_account_num_name.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_account_num_name, text=widget_text[5], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_account_num_name.combobox_account_num = ttk.Combobox(frame_account_num_name, values=option_blank, state='readonly', width=20)
        frame_account_num_name.combobox_account_num.pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Label(frame_account_num_name, text=widget_text[6], width=10, anchor='w').pack(side=tk.LEFT, padx=(20, 5), pady=5)
        frame_account_num_name.combobox_account_name = ttk.Combobox(frame_account_num_name, values=option_blank, state='readonly', width=20)
        frame_account_num_name.combobox_account_name.pack(side=tk.LEFT, padx=(5, 10), pady=5)

        frame_opposite_cash = tk.Frame(top)
        frame_opposite_cash.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_opposite_cash, text=widget_text[7], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_opposite_cash.combobox_opposite = ttk.Combobox(frame_opposite_cash, values=option_blank, state='readonly', width=20)
        frame_opposite_cash.combobox_opposite.pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Label(frame_opposite_cash, text=widget_text[8], width=10, anchor='w').pack(side=tk.LEFT, padx=(20, 5), pady=5)
        frame_opposite_cash.combobox_cash = ttk.Combobox(frame_opposite_cash, values=option_blank, state='readonly', width=20)
        frame_opposite_cash.combobox_cash.pack(side=tk.LEFT, padx=(5, 10), pady=5)

        frame_debit_credit = tk.Frame(top)
        frame_debit_credit.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_debit_credit, text=widget_text[9], width=10, anchor='w').pack(side=tk.LEFT, padx=(10, 5), pady=5)
        frame_debit_credit.combobox_debit = ttk.Combobox(frame_debit_credit, values=option_blank, state='readonly', width=20)
        frame_debit_credit.combobox_debit.pack(side=tk.LEFT, padx=(5, 20), pady=5)
        tk.Label(frame_debit_credit, text=widget_text[10], width=10, anchor='w').pack(side=tk.LEFT, padx=(20, 5), pady=5)
        frame_debit_credit.combobox_credit = ttk.Combobox(frame_debit_credit, values=option_blank, state='readonly', width=20)
        frame_debit_credit.combobox_credit.pack(side=tk.LEFT, padx=(5, 10), pady=5)

        frame_button = tk.Frame(top)
        frame_button.pack(side=tk.TOP, fill=tk.BOTH, padx=(65, 5), pady=5)

        tk.Button(frame_button, text=widget_text[11],
                  command=lambda: self.select_chronological(frame_path.entry_path,
                                                            frame_sheet_date.combobox_sheet,
                                                            frame_sheet_date.combobox_date,
                                                            frame_num_summary.combobox_num,
                                                            frame_num_summary.combobox_summary,
                                                            frame_account_num_name.combobox_account_num,
                                                            frame_account_num_name.combobox_account_name,
                                                            frame_opposite_cash.combobox_opposite,
                                                            frame_opposite_cash.combobox_cash,
                                                            frame_debit_credit.combobox_debit,
                                                            frame_debit_credit.combobox_credit),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)

        tk.Button(frame_button, text=widget_text[12],
                  command=lambda: self.import_review_chronological(frame_path.entry_path,
                                                                   frame_sheet_date.combobox_sheet,
                                                                   frame_sheet_date.combobox_date,
                                                                   frame_num_summary.combobox_num,
                                                                   frame_num_summary.combobox_summary,
                                                                   frame_account_num_name.combobox_account_num,
                                                                   frame_account_num_name.combobox_account_name,
                                                                   frame_opposite_cash.combobox_opposite,
                                                                   frame_opposite_cash.combobox_cash,
                                                                   frame_debit_credit.combobox_debit,
                                                                   frame_debit_credit.combobox_credit),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)

        tk.Button(frame_button, text=widget_text[13],
                  command=top.destroy,
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)

        frame_sheet_date.combobox_sheet.bind('<<ComboboxSelected>>',
                                    lambda event: self.chronological_change(event,
                                                                            frame_path.entry_path,
                                                                            frame_sheet_date.combobox_sheet,
                                                                            frame_sheet_date.combobox_date,
                                                                            frame_num_summary.combobox_num,
                                                                            frame_num_summary.combobox_summary,
                                                                            frame_account_num_name.combobox_account_num,
                                                                            frame_account_num_name.combobox_account_name,
                                                                            frame_opposite_cash.combobox_opposite,
                                                                            frame_opposite_cash.combobox_cash,
                                                                            frame_debit_credit.combobox_debit,
                                                                            frame_debit_credit.combobox_credit))

        top.transient(root)                    # 依附主窗口
        top.grab_set()                         # 禁止操作主窗口
        root.wait_window(top)                  # 等待子窗口关闭


    # 更新下拉列表框
    def chronological_change(self, event, entry_path, combobox_sheet, combobox_date, combobox_num, combobox_summary,
                             combobox_account_num, combobox_account_name, combobox_opposite, combobox_cash, combobox_debit, combobox_credit):

        path = entry_path.get()
        sheet_name = combobox_sheet.get()

        result = columns_title_fun.columns_title(path, sheet_name)

        if result[0]:

            new_options = result[2]

            combobox_date['values'] = new_options
            combobox_date.set(new_options[0])
            combobox_date.config(state='readonly')

            combobox_num['values'] = new_options
            combobox_num.set(new_options[0])
            combobox_num.config(state='readonly')
            
            combobox_summary['values'] = new_options
            combobox_summary.set(new_options[0])
            combobox_summary.config(state='readonly')

            combobox_account_num['values'] = new_options
            combobox_account_num.set(new_options[0])
            combobox_account_num.config(state='readonly')

            combobox_account_name['values'] = new_options
            combobox_account_name.set(new_options[0])
            combobox_account_name.config(state='readonly')

            combobox_opposite['values'] = new_options
            combobox_opposite.set(new_options[0])
            combobox_opposite.config(state='readonly')

            combobox_cash['values'] = new_options
            combobox_cash.set(new_options[0])
            combobox_cash.config(state='readonly')

            combobox_debit['values'] = new_options
            combobox_debit.set(new_options[0])
            combobox_debit.config(state='readonly')

            combobox_credit['values'] = new_options
            combobox_credit.set(new_options[0])
            combobox_credit.config(state='readonly')


    # 选择序时账文件
    def select_chronological(self, entry_path, combobox_sheet, combobox_date, combobox_num, combobox_summary,
                             combobox_account_num, combobox_account_name, combobox_opposite, combobox_cash,
                             combobox_debit, combobox_credit):

        path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx'),
                                                     ('Excel Files', '*.xls')])
        
        if path:
            entry_path.config(state='normal')
            entry_path.delete(0, tk.END)
            entry_path.insert(0, path)
            entry_path.config(state='readonly')

            sheets_name_result = sheetnames_import_fun.sheetnames_import(path)

            if sheets_name_result[0]:

                sheets_name_list = sheets_name_result[2]

                combobox_sheet['values'] = sheets_name_list
                combobox_sheet.set(sheets_name_list[0])
                combobox_sheet.config(state='readonly')

                self.chronological_change(None, entry_path, combobox_sheet, combobox_date, combobox_num, combobox_summary,
                                          combobox_account_num, combobox_account_name, combobox_opposite, combobox_cash,
                                          combobox_debit, combobox_credit)


    # 导入、预览序时账
    def import_review_chronological(self, entry_file, combobox_sheet, combobox_date, combobox_num, combobox_summary,
                                    combobox_account_num, combobox_account_name, combobox_opposite, combobox_cash,
                                    combobox_debit, combobox_credit):

        path = entry_file.get()
        sheet_name = combobox_sheet.get()
        date = combobox_date.get()
        number = combobox_num.get()
        summary = combobox_summary.get()
        account_num = combobox_account_num.get()
        account_name = combobox_account_name.get()
        opposite = combobox_opposite.get()
        cash = combobox_cash.get()
        debit = combobox_debit.get()
        credit = combobox_credit.get()

        # 读入数据
        result_info = read_xlsx_xls_csv_txt_fun.read_xlsx_xls_csv_txt(file_path=path, sheet_name=sheet_name)

        if result_info[0]:

            df = result_info[2]

            # 对借方、贷方发生额进行数据清洗
            df[debit] = df[debit].apply(self.convert_to_numeric)
            df[credit] = df[credit].apply(self.convert_to_numeric)

            # 日期列列填充空行（重复上一行），转换制单日期为datetime类型并提取月份
            df[date] = df[date].ffill()
            df[date] = pd.to_datetime(df[date], errors='coerce')
            df['月份'] = df[date].dt.month

            # 凭证号列填充空行（重复上一行）
            df[number] = df[number].ffill()

            # 遍历每个凭证号和月份，找出对应的科目
            voucher_groups = df.groupby(['月份', number])
            for (month, voucher_no), group in voucher_groups:
                primary_subjects = set()
                for subject in group[account_num]:
                    primary_subjects.add(str(subject))
                primary_subjects_str = ', '.join(primary_subjects)
                df.loc[(df['月份'] == month) & (df[number] == voucher_no), '涉及科目'] = primary_subjects_str

            self.df_chronological['涉及科目'] = df['涉及科目']
            self.df_chronological['日期'] = df[date]
            self.df_chronological['凭证字号'] = df[number]
            self.df_chronological['摘要'] = df[summary]
            self.df_chronological['科目编码'] = df[account_num]
            self.df_chronological['科目名称'] = df[account_name]
            self.df_chronological['对方科目'] = df[opposite]
            self.df_chronological['借方金额'] = df[debit]
            self.df_chronological['贷方金额'] = df[credit]
            self.df_chronological['现金流量表项目'] = df[cash]

        df_review_xlsx_fun.df_review_xlsx(self.df_chronological)


    # 数据清洗
    def convert_to_numeric(self, value):

        try:

            return pd.to_numeric(value.replace(',', ''))
        
        except:

            return 0 if pd.isna(value) else value


    # 导出按钮
    def export_file(self, text_area):

        fill_text = ''

        result_info = export_account_data_fun.export_account_data(self.df_balance, self.df_chronological)

        if result_info[0]:

            subprocess.run(['open', result_info[2]])

        fill_text += result_info[1]

        gui_tk_area_text.text_area_fill(text_area, fill_text)