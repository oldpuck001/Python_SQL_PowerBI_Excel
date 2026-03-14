# gui_tk_sheet_regex.py

import os
import operator
import pandas as pd
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
from gui_tk import gui_tk_area_text
from dataframe_tools_pd import sheetnames_import_fun
from dataframe_tools_pd import columns_title_fun
from dataframe_tools_pd import read_xlsx_xls_csv_txt_fun
from dataframe_tools_pd import df_review_xlsx_fun
from xlsx_tools_openxl import export_new_xlsx_fun

class gui_tk_sheet_regex_class:

    regex_list = []
    left_right = False
    data_df = pd.DataFrame()

    def gui_tk_sheet_regex_frame(self, root, control_frame_config, text_area):

        options_banlk = []
        options_label = ['', '~']

        frame_result = tk.Frame(root)
        frame_result.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=(10, 5))

        frame_result.frame_path = tk.Frame(frame_result)
        frame_result.frame_path.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_path, text=control_frame_config['widget_text'][0], width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_path.entry_path = tk.Entry(frame_result.frame_path, state='readonly', readonlybackground='white')         # 创建Entry并保存引用
        frame_result.frame_path.entry_path.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        frame_result.frame_sheet_col_label = tk.Frame(frame_result)
        frame_result.frame_sheet_col_label.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_sheet_col_label, text=control_frame_config['widget_text'][1], width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_col_label.combobox_sheet = ttk.Combobox(frame_result.frame_sheet_col_label, values=options_banlk, state='readonly', width=26)
        frame_result.frame_sheet_col_label.combobox_sheet.pack(side=tk.LEFT, padx=5, pady=5)
        tk.Label(frame_result.frame_sheet_col_label, text=control_frame_config['widget_text'][2], width=8, anchor='w').pack(side=tk.LEFT, padx=(105, 5), pady=5)
        frame_result.frame_sheet_col_label.combobox_col = ttk.Combobox(frame_result.frame_sheet_col_label, values=options_banlk, state='readonly', width=26)
        frame_result.frame_sheet_col_label.combobox_col.pack(side=tk.LEFT, padx=(5, 105), pady=5)
        tk.Label(frame_result.frame_sheet_col_label, text=control_frame_config['widget_text'][3], width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_col_label.combobox_label = ttk.Combobox(frame_result.frame_sheet_col_label, values=options_label, state='readonly', width=26)
        frame_result.frame_sheet_col_label.combobox_label.pack(side=tk.LEFT, padx=5, pady=5)

        frame_result.frame_regex = tk.Frame(frame_result)
        frame_result.frame_regex.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_regex, text=control_frame_config['widget_text'][4], width=17, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_regex.entry_regex = tk.Entry(frame_result.frame_regex)
        frame_result.frame_regex.entry_regex.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        # 正则表达式指令区
        frame_result.frame_regex_command = tk.Frame(frame_result)
        frame_result.frame_regex_command.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        tk.Label(frame_result.frame_regex_command, text=control_frame_config['widget_text'][5], anchor='w').pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        frame_result.frame_regex_command.regex_command_text_area = ScrolledText(frame_result.frame_regex_command, height=15)
        frame_result.frame_regex_command.regex_command_text_area.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        # 按钮行
        frame_result.frame_button = tk.Frame(frame_result)
        frame_result.frame_button.pack(side=tk.TOP, fill=tk.BOTH)
        # 选择文件按钮
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][6],
                  command=lambda: self.select_sheet(frame_result.frame_path.entry_path,
                                                    frame_result.frame_sheet_col_label.combobox_sheet,
                                                    frame_result.frame_sheet_col_label.combobox_col,
                                                    text_area),
                  width=10).pack(side=tk.LEFT, padx=5, pady=5)
        # 导入数据按钮
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][7],
                  command=lambda: self.import_sheet(frame_result.frame_path.entry_path,
                                                    frame_result.frame_sheet_col_label.combobox_sheet,
                                                    text_area),
                  width=10).pack(side=tk.LEFT, padx=5, pady=5)
        # 预览数据按钮
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][8],
                  command=lambda: self.button_preview_fun(text_area),
                  width=10).pack(side=tk.LEFT, padx=5, pady=5)
        # 添加regex按钮
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][9],
                  command=lambda: self.add_regex(frame_result.frame_sheet_col_label.combobox_col,
                                                 frame_result.frame_sheet_col_label.combobox_label,
                                                 frame_result.frame_regex.entry_regex,
                                                 frame_result.frame_regex_command.regex_command_text_area),
                  width=10).pack(side=tk.LEFT, padx=5, pady=5)
        # []按钮
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][10],
                  command=lambda: self.add_brackets(frame_result.frame_regex_command.regex_command_text_area),
                  width=10).pack(side=tk.LEFT, padx=5, pady=5)
        # AND按钮
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][11],
                  command=lambda: self.add_and(frame_result.frame_regex_command.regex_command_text_area),
                  width=10).pack(side=tk.LEFT, padx=5, pady=5)
        # OR按钮
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][12],
                  command=lambda: self.add_or(frame_result.frame_regex_command.regex_command_text_area),
                  width=10).pack(side=tk.LEFT, padx=5, pady=5)
        # 执行筛选按钮
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][13],
                  command=lambda: self.command_regex(frame_result.frame_regex_command.regex_command_text_area,
                                                     text_area),
                  width=10).pack(side=tk.LEFT, padx=5, pady=5)
        # 导出按钮
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][14],
                  command=lambda: self.export_data(text_area),
                  width=10).pack(side=tk.LEFT, padx=5, pady=5)

        frame_result.frame_sheet_col_label.combobox_sheet.bind('<<ComboboxSelected>>',
                                                               lambda event: self.on_sheet_change(event,
                                                                                                  frame_result.frame_path.entry_path,
                                                                                                  frame_result.frame_sheet_col_label.combobox_sheet,
                                                                                                  frame_result.frame_sheet_col_label.combobox_col))
        
        return frame_result


    # 选择文件按钮函数
    def select_sheet(self, entry_path, combobox_sheet, combobox_col, text_area):

        fill_text = ''
        path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx'),
                                                     ('Excel Files', '*.xls')])

        if path:
            entry_path.config(state='normal')
            entry_path.delete(0, tk.END)
            entry_path.insert(0, path)
            entry_path.config(state='readonly')
            fill_text += f'Selected: {path}\n'
            fill_text += 'File selection successful!\n'

            sheets_name_result = sheetnames_import_fun.sheetnames_import(path)
            if sheets_name_result[0]:

                sheets_name_list = sheets_name_result[2]
                combobox_sheet['values'] = sheets_name_list
                combobox_sheet.set(sheets_name_list[0])               # 设置默认选择第一个
                combobox_sheet.config(state='readonly')

            else:

                combobox_sheet.set('')
                combobox_sheet.config(state='disabled')

            fill_text += sheets_name_result[1]

        else:
            fill_text += f'File selection failed!\n'

        self.on_sheet_change(None, entry_path, combobox_sheet, combobox_col)

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 自动更新列名列表
    def on_sheet_change(self, event, entry_path, combobox_sheet, combobox_col):

        file_path = entry_path.get()
        sheet_name = combobox_sheet.get()

        result = columns_title_fun.columns_title(file_path, sheet_name)

        if result[0]:

            new_options = result[2]

            combobox_col['values'] = new_options
            if new_options[0]:
                combobox_col.set(new_options[0])
            combobox_col.config(state='readonly')


    # 导入按钮函数
    def import_sheet(self, entry_path, combobox_sheet, text_area):

        fill_text = ''
        path = entry_path.get()
        sheet_name = combobox_sheet.get()

        if path:

            result_info = read_xlsx_xls_csv_txt_fun.read_xlsx_xls_csv_txt(file_path=path, sheet_name=sheet_name)
            if result_info[0]:
                self.data_df = result_info[2]
                self.data_df.reset_index(drop=True, inplace=True)
                fill_text += result_info[1]
            else:
                fill_text += result_info[1]
        else:
            fill_text += f'Please select a file first!\n'

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 数据预览
    def button_preview_fun(self, text_area):

        fill_text = ''
        result_info = df_review_xlsx_fun.df_review_xlsx(self.data_df)
        fill_text += result_info[1]
        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 添加正则表达式按钮函数
    def add_regex(self, combobox_col, combobox_label, entry_regex, text_area_regex):

        col = combobox_col.get()
        label = combobox_label.get()
        regex = entry_regex.get()

        if self.left_right:
            fill_regex = f"  ['{label}', '{col}', '{regex}'],\n"
        else:
            fill_regex = f"['{label}', '{col}', '{regex}'],\n"

        text_area_regex.insert(tk.INSERT, fill_regex)
        text_area_regex.see(tk.END)


    # []按钮函数
    def add_brackets(self, text_area_regex):

        if self.left_right:

            self.left_right = False
            fill_regex = '],\n'

            text_area_regex.insert(tk.INSERT, fill_regex)
            text_area_regex.see(tk.END)

        else:

            self.left_right = True
            fill_regex = '[\n'

            text_area_regex.insert(tk.INSERT, fill_regex)
            text_area_regex.see(tk.END)


    # &按钮函数
    def add_and(self, text_area_regex):

        if self.left_right:
            fill_regex = f"  ['AND'],\n"
            text_area_regex.insert(tk.INSERT, fill_regex)
            text_area_regex.see(tk.END)


    # &按钮函数
    def add_or(self, text_area_regex):

        if self.left_right:
            fill_regex = f"  ['OR'],\n"
            text_area_regex.insert(tk.INSERT, fill_regex)
            text_area_regex.see(tk.END)
    

    # 执行筛选按钮
    def command_regex(self, text_area_regex, text_area):

        fill_text = ''
        l_r = False
        regex_list = []

        text = text_area_regex.get('1.0', 'end-1c')

        text = text.strip()

        for line in text.splitlines():
            text_split = line.split(', ')
            if text_split[0] == "[''":

                regex_col = text_split[1].strip('"\'')
                regex_text = ', '.join(text_split[2:])
                regex_text = regex_text[1:-3]
                regex_append = ['', regex_col, regex_text]
                regex_list.append(regex_append)

            elif text_split[0] == "['~'":

                regex_col = text_split[1].strip('"\'')
                regex_text = ', '.join(text_split[2:])
                regex_text = regex_text[1:-3]
                regex_append = ['~', regex_col, regex_text]
                regex_list.append(regex_append)

            elif text_split[0] == '[':

                l_r = True
                regex_list.append([])

            elif text_split[0] == "  [''":

                regex_col = text_split[1].strip('"\'')
                regex_text = ', '.join(text_split[2:])
                regex_text = regex_text[1:-3]
                regex_append = ['', regex_col, regex_text]
                regex_list[-1].append(regex_append)

            elif text_split[0] == "  ['~'":

                regex_col = text_split[1].strip('"\'')
                regex_text = ', '.join(text_split[2:])
                regex_text = regex_text[1:-3]
                regex_append = ['~', regex_col, regex_text]
                regex_list[-1].append(regex_append)

            elif text_split[0] == "  ['AND'],":

                regex_list[-1].append(['AND'])

            elif text_split[0] == "  ['OR'],":

                regex_list[-1].append(['OR'])

            elif text_split[0] == '],':

                l_r = False

        for regex_l in regex_list:

            if_label = regex_l[0]
            column_index = regex_l[1]
            regex_pattern = regex_l[2]
            # 使用正則表達式篩選列並更新 DataFrame
            if if_label == '':
                self.data_df = self.data_df[self.data_df[column_index].str.contains(regex_pattern, regex=True, na=False)]
            elif if_label == '~':
                self.data_df = self.data_df[~self.data_df[column_index].str.contains(regex_pattern, regex=True, na=False)]
            else:
                mask = self.build_mask(self.data_df, regex_l)
                self.data_df = self.data_df[mask]

        fill_text += '筛选成功！\n'
        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 多列筛选用函数
    def build_mask(self, df, conditions):

        final_mask = None
        pending_op = None   # 上一个 AND / OR

        for c in conditions:

            if len(c) == 3:
                regex_index = c[0]
                regex_col = c[1]
                regex_re = c[2]

                if regex_index == '~':
                    col_mask = ~df[regex_col].astype(str).str.contains(regex_re, regex=True, na=False)
                else:
                    col_mask = df[regex_col].astype(str).str.contains(regex_re, regex=True, na=False)

                if final_mask is None:
                    final_mask = col_mask
                else:
                    final_mask = pending_op(final_mask, col_mask)

            else:
                if c[0] == 'AND':
                    pending_op = operator.and_
                else:
                    pending_op = operator.or_

        return final_mask


    # 导出按钮函数
    def export_data(self, text_area):

        fill_text = ''

        result_info = export_new_xlsx_fun.export_new_xlsx(self.data_df)

        if result_info[0]:
            fill_text += result_info[1]
            subprocess.run(['open', result_info[2]])
        
        gui_tk_area_text.text_area_fill(text_area, fill_text)