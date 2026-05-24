# gui_tk_in_out_sort.py

import os
import re
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from gui_tk import gui_tk_area_text
from dataframe_tools_pd import sheetnames_import_fun
from dataframe_tools_pd import columns_title_fun
from dataframe_tools_pd import read_xlsx_xls_csv_txt_fun
from dataframe_tools_pd import df_col_label_fun
from dataframe_tools_pd import df_cleaning_fun
from dataframe_tools_pd import df_export_xlsx_fun
from xlsx_tools_openxl import export_tree_new_xlsx_fun

class gui_tk_in_out_sort_class:

    def gui_tk_in_out_sort_frame(self, root, control_frame_config, text_area):

        options_blank = []

        frame_result = tk.Frame(root)
        frame_result.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=(10, 5))

        frame_result.frame_path = tk.Frame(frame_result)
        frame_result.frame_path.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_path, text=control_frame_config['widget_text'][0], width=12, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_path.entry_path = tk.Entry(frame_result.frame_path, state='readonly', readonlybackground='white')
        frame_result.frame_path.entry_path.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        frame_result.frame_sheet_in_out = tk.Frame(frame_result)
        frame_result.frame_sheet_in_out.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_sheet_in_out, text=control_frame_config['widget_text'][1], width=12, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_in_out.combobox_sheet = ttk.Combobox(frame_result.frame_sheet_in_out, values=options_blank, state='readonly', width=23)
        frame_result.frame_sheet_in_out.combobox_sheet.pack(side=tk.LEFT, padx=(5, 90), pady=5)
        tk.Label(frame_result.frame_sheet_in_out, text=control_frame_config['widget_text'][2], width=12, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_in_out.combobox_in_out = ttk.Combobox(frame_result.frame_sheet_in_out, values=options_blank, state='readonly', width=23)
        frame_result.frame_sheet_in_out.combobox_in_out.pack(side=tk.LEFT, padx=5, pady=5)

        frame_result.frame_in_out = tk.Frame(frame_result)
        frame_result.frame_in_out.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_in_out, text=control_frame_config['widget_text'][3], width=12, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_in_out.combobox_in = ttk.Combobox(frame_result.frame_in_out, values=options_blank, state='readonly', width=23)
        frame_result.frame_in_out.combobox_in.pack(side=tk.LEFT, padx=(5, 90), pady=5)
        tk.Label(frame_result.frame_in_out, text=control_frame_config['widget_text'][4], width=12, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_in_out.combobox_out = ttk.Combobox(frame_result.frame_in_out, values=options_blank, state='readonly', width=23)
        frame_result.frame_in_out.combobox_out.pack(side=tk.LEFT, padx=5, pady=5)

        frame_result.frame_groupby_value = tk.Frame(frame_result)
        frame_result.frame_groupby_value.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_groupby_value, text=control_frame_config['widget_text'][5], width=12, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_groupby_value.combobox_groupby_2 = ttk.Combobox(frame_result.frame_groupby_value, values=options_blank, state='readonly', width=23)
        frame_result.frame_groupby_value.combobox_groupby_2.pack(side=tk.LEFT, padx=(5, 90), pady=5)
        tk.Label(frame_result.frame_groupby_value, text=control_frame_config['widget_text'][6], width=12, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_groupby_value.combobox_groupby_3 = ttk.Combobox(frame_result.frame_groupby_value, values=options_blank, state='readonly', width=23)
        frame_result.frame_groupby_value.combobox_groupby_3.pack(side=tk.LEFT, padx=(5, 90), pady=5)
        tk.Label(frame_result.frame_groupby_value, text=control_frame_config['widget_text'][7], width=9, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_groupby_value.combobox_value = ttk.Combobox(frame_result.frame_groupby_value, values=options_blank, state='readonly', width=26)
        frame_result.frame_groupby_value.combobox_value.pack(side=tk.LEFT, padx=5, pady=5)

        frame_result.frame_priority = tk.Frame(frame_result)
        frame_result.frame_priority.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_priority, text=control_frame_config['widget_text'][8], width=12, anchor='nw').pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)
        frame_result.frame_priority.text_area_in = ScrolledText(frame_result.frame_priority, width=62, height=15)
        frame_result.frame_priority.text_area_in.pack(side=tk.LEFT, padx=(5, 85), pady=5)
        tk.Label(frame_result.frame_priority, text=control_frame_config['widget_text'][9], width=12, anchor='nw').pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5)
        frame_result.frame_priority.text_area_out = ScrolledText(frame_result.frame_priority, width=62, height=15)
        frame_result.frame_priority.text_area_out.pack(side=tk.LEFT, padx=5, pady=5)

        frame_result.frame_button = tk.Frame(frame_result)
        frame_result.frame_button.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][10],
                  command=lambda: self.input_sheet(frame_result.frame_path.entry_path,
                                                   frame_result.frame_sheet_in_out.combobox_sheet,
                                                   frame_result.frame_sheet_in_out.combobox_in_out,
                                                   frame_result.frame_groupby_value.combobox_groupby_2,
                                                   frame_result.frame_groupby_value.combobox_groupby_3,
                                                   frame_result.frame_groupby_value.combobox_value,
                                                   text_area),
                  width=15).pack(side=tk.LEFT, padx=(450, 5), pady=5)
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][11],
                  command=lambda: self.export_result(frame_result.frame_path.entry_path,
                                                     frame_result.frame_sheet_in_out.combobox_sheet,
                                                     frame_result.frame_sheet_in_out.combobox_in_out,
                                                     frame_result.frame_in_out.combobox_in,
                                                     frame_result.frame_in_out.combobox_out,
                                                     frame_result.frame_groupby_value.combobox_groupby_2,
                                                     frame_result.frame_groupby_value.combobox_groupby_3,
                                                     frame_result.frame_groupby_value.combobox_value,
                                                     frame_result.frame_priority.text_area_in,
                                                     frame_result.frame_priority.text_area_out,
                                                     text_area),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)

        frame_result.frame_sheet_in_out.combobox_sheet.bind('<<ComboboxSelected>>',
                                                            lambda event: self.on_sheet_change(event,
                                                                                                frame_result.frame_path.entry_path,
                                                                                                frame_result.frame_sheet_in_out.combobox_sheet,
                                                                                                frame_result.frame_sheet_in_out.combobox_in_out,
                                                                                                frame_result.frame_groupby_value.combobox_groupby_2,
                                                                                                frame_result.frame_groupby_value.combobox_groupby_3,
                                                                                                frame_result.frame_groupby_value.combobox_value))

        frame_result.frame_sheet_in_out.combobox_in_out.bind('<<ComboboxSelected>>',
                                                             lambda event: self.on_in_out_change(event,
                                                                                                 frame_result.frame_path.entry_path,
                                                                                                 frame_result.frame_sheet_in_out.combobox_sheet,
                                                                                                 frame_result.frame_sheet_in_out.combobox_in_out,
                                                                                                 frame_result.frame_in_out.combobox_in,
                                                                                                 frame_result.frame_in_out.combobox_out))


        return frame_result


    # 导入按钮函数
    def input_sheet(self, entry_path, combobox_sheet, combobox_in_out, combobox_groupby_2, combobox_groupby_3, combobox_value, text_area):

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

        self.on_sheet_change(None, entry_path, combobox_sheet, combobox_in_out, combobox_groupby_2, combobox_groupby_3, combobox_value)

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 自动更新列名列表
    def on_sheet_change(self, event, entry_path, combobox_sheet, combobox_in_out, combobox_groupby_2, combobox_groupby_3, combobox_value):

        file_path = entry_path.get()
        sheet_name = combobox_sheet.get()

        result = columns_title_fun.columns_title(file_path, sheet_name)

        if result[0]:

            new_options = result[2]

            combobox_in_out['values'] = new_options
            if new_options[0]:
                combobox_in_out.set(new_options[0])
            combobox_in_out.config(state='readonly')

            combobox_groupby_2['values'] = new_options
            if new_options[0]:
                combobox_groupby_2.set(new_options[0])
            combobox_groupby_2.config(state='readonly')

            combobox_groupby_3['values'] = new_options
            if new_options[0]:
                combobox_groupby_3.set(new_options[0])
            combobox_groupby_3.config(state='readonly')

            combobox_value['values'] = new_options
            if new_options[0]:
                combobox_value.set(new_options[0])
            combobox_value.config(state='readonly')


    # 自动更新in标签/out标签列表
    def on_in_out_change(self, event, entry_path, combobox_sheet, combobox_in_out, combobox_in, combobox_out):

        file_path = entry_path.get()
        sheet_name = combobox_sheet.get()
        in_out_col = combobox_in_out.get()

        # 读入数据
        result_info = read_xlsx_xls_csv_txt_fun.read_xlsx_xls_csv_txt(file_path=file_path, sheet_name=sheet_name)

        if result_info[0]:
            
            df = result_info[2]

        result_in_out = df_col_label_fun.df_col_label(df, in_out_col)

        if result_in_out[0]:

            in_out_options = result_in_out[2]

            combobox_in['values'] = in_out_options
            if in_out_options[0]:
                combobox_in.set(in_out_options[0])
            combobox_in.config(state='readonly')

            combobox_out['values'] = in_out_options
            if in_out_options[1]:
                combobox_out.set(in_out_options[1])
            combobox_out.config(state='readonly')


    # 导出按钮函数
    def export_result(self, source_file_path, sheet_name, in_out_column,
                            in_column, out_column, groupby_2_column, groupby_3_column, value_column, in_priority, out_priority,
                            text_area):

        fill_text = ''
        source_file_path = source_file_path.get()
        sheet_name = sheet_name.get()
        in_out_column = in_out_column.get()
        in_column = in_column.get()
        out_column = out_column.get()
        groupby_2_column = groupby_2_column.get()
        groupby_3_column = groupby_3_column.get()
        value_column = value_column.get()
        in_priority = in_priority.get('1.0', 'end-1c')
        in_priority_list = [name.strip() for name in in_priority.split(',')]
        out_priority = out_priority.get('1.0', 'end-1c')
        out_priority_list = [name.strip() for name in out_priority.split(',')]

        file_path = os.path.dirname(source_file_path)
        file_name = os.path.splitext(source_file_path)[0]
        target_file_path = os.path.join(file_path, f'{file_name}In_Out值分类.xlsx')
        export_path = os.path.join(file_path, f'{file_name}In_Out值分类')                       # 建立输出文件夹
        os.makedirs(export_path, exist_ok=True)

        in_groupby_2_summary = {'in_groupby_2_sort': [], 'in_groupby_2_value': []}
        in_groupby_3_summary_dict = {}
        in_groupby_3_summary = {'in_groupby_3_sort': [], 'in_groupby_3_value': []}
        out_groupby_2_summary = {'out_groupby_2_sort': [], 'out_groupby_2_value': []}
        out_groupby_3_summary_dict = {}
        out_groupby_3_summary = {'out_groupby_3_sort': [], 'out_groupby_3_value': []}

        if in_out_column == value_column:
            fill_text += 'In/Out分类列不可以与数值列相同，请重新选择。\n'
            gui_tk_area_text.text_area_fill(text_area, fill_text)

        # 读入数据
        result_info = read_xlsx_xls_csv_txt_fun.read_xlsx_xls_csv_txt(file_path=source_file_path, sheet_name=sheet_name)
        if result_info[0]:
            df = result_info[2]

        # 数据清洗
        result_cleaned = df_cleaning_fun.df_cleaning(df, groupby_2_column, 'fillna_<blank>')
        if result_cleaned[0]:
            df = result_cleaned[2]
        result_cleaned = df_cleaning_fun.df_cleaning(df, groupby_3_column, 'fillna_<blank>')
        if result_cleaned[0]:
            df = result_cleaned[2]
        result_cleaned = df_cleaning_fun.df_cleaning(df, value_column, 'to_float')
        if result_cleaned[0]:
            df = result_cleaned[2]


        # 第一层分组，划分In与Out
        df[in_out_column] = df[in_out_column].astype(str).str.strip()
        df_grouped = df.groupby(in_out_column)
        in_df = df_grouped.get_group(in_column)
        out_df = df_grouped.get_group(out_column)
        in_summary_total = in_df[value_column].sum()
        out_summary_total = out_df[value_column].sum()

        # 第二层分组，按groupby列进行分组
        # 第二层分组的In部分
        in_groupby_2_sorts = in_df[groupby_2_column].unique()
        in_groupby_2_dfs = {in_groupby_2_sort: in_df.loc[in_df[groupby_2_column] == in_groupby_2_sort] for in_groupby_2_sort in in_groupby_2_sorts}

        for in_groupby_2_sort, in_groupby_2_df in in_groupby_2_dfs.items():
            in_groupby_2_sort_cleaned = in_groupby_2_sort.replace('\t', '') if not isinstance(in_groupby_2_sort, float) else in_groupby_2_sort
            in_groupby_2_total = in_groupby_2_df[value_column].sum()
            in_groupby_2_summary['in_groupby_2_sort'].append(in_groupby_2_sort_cleaned)
            in_groupby_2_summary['in_groupby_2_value'].append(in_groupby_2_total)

            # 第三层分组，按group_by列进行分组
            # 第三层分组的In部分
            in_groupby_3_sorts = in_groupby_2_df[groupby_3_column].unique()
            in_groupby_3_dfs = {in_groupby_3_sort: in_groupby_2_df.loc[in_groupby_2_df[groupby_3_column] == in_groupby_3_sort] for in_groupby_3_sort in in_groupby_3_sorts}

            for in_groupby_3_sort, in_groupby_3_df in in_groupby_3_dfs.items():
                # 输出单个分类项为xlsx文件
                in_column_save = self.sanitize_filename(in_column)
                in_groupby_2_sort_save = self.sanitize_filename(in_groupby_2_sort)
                in_groupby_3_sort_save = self.sanitize_filename(in_groupby_3_sort)
                # 初始文件名
                base_filename = f'{in_groupby_2_sort_save}_{in_groupby_3_sort_save}_{in_column_save}_1.xlsx'
                df_export_path = os.path.join(export_path, base_filename)
                # 检查文件是否存在，如果存在则添加后缀
                counter = 2
                while os.path.exists(df_export_path):
                    # 如果文件存在，修改文件名，例如：filename_1.xlsx, filename_2.xlsx
                    new_filename = f'{in_groupby_2_sort_save}_{in_groupby_3_sort_save}_{in_column_save}_{counter}.xlsx'
                    df_export_path = os.path.join(export_path, new_filename)
                    counter += 1
                # 保存文件
                df_export_xlsx_fun.df_export_xlsx(in_groupby_3_df, df_export_path, index=False)

                in_number_total = in_groupby_3_df[value_column].sum()
                in_groupby_3_summary['in_groupby_3_sort'].append(in_groupby_3_sort)
                in_groupby_3_summary['in_groupby_3_value'].append(in_number_total)

            in_groupby_3_summary_dict[in_groupby_2_sort_cleaned] = pd.DataFrame(in_groupby_3_summary).sort_values(by='in_groupby_3_value', ascending=False)

            in_groupby_3_summary['in_groupby_3_sort'].clear()
            in_groupby_3_summary['in_groupby_3_value'].clear()

            in_groupby_2_summary_df_not_sorted = pd.DataFrame(in_groupby_2_summary)
            in_groupby_2_summary_df = in_groupby_2_summary_df_not_sorted.sort_values(by='in_groupby_2_value', ascending=False)

        # 第二层分组的Out部分
        out_groupby_2_sorts = out_df[groupby_2_column].unique()
        out_groupby_2_dfs = {out_groupby_2_sort: out_df.loc[out_df[groupby_2_column] == out_groupby_2_sort] for out_groupby_2_sort in out_groupby_2_sorts}

        for out_groupby_2_sort, out_groupby_2_df in out_groupby_2_dfs.items():
            out_groupby_2_sort_cleaned = out_groupby_2_sort.replace('\t', '') if not isinstance(out_groupby_2_sort, float) else out_groupby_2_sort
            out_groupby_2_total = out_groupby_2_df[value_column].sum()
            out_groupby_2_summary['out_groupby_2_sort'].append(out_groupby_2_sort_cleaned)
            out_groupby_2_summary['out_groupby_2_value'].append(out_groupby_2_total)

            # 第三层分组，按group_by进行分组
            # 第三层分组的Out部分
            out_groupby_3_sorts = out_groupby_2_df[groupby_3_column].unique()
            out_groupby_3_dfs = {out_groupby_3_sort: out_groupby_2_df.loc[out_groupby_2_df[groupby_3_column] == out_groupby_3_sort] for out_groupby_3_sort in out_groupby_3_sorts}

            for out_groupby_3_sort, out_groupby_3_df in out_groupby_3_dfs.items():
                # 输出单个分类项为xlsx文件
                out_column_save = self.sanitize_filename(out_column)
                out_groupby_2_sort_save = self.sanitize_filename(out_groupby_2_sort)
                out_groupby_3_sort_save = self.sanitize_filename(out_groupby_3_sort)
                # 初始文件名
                base_filename = f'{out_groupby_2_sort_save}_{out_groupby_3_sort_save}_{out_column_save}_1.xlsx'
                df_export_path = os.path.join(export_path, base_filename)
                # 检查文件是否存在，如果存在则添加后缀
                counter = 2
                while os.path.exists(df_export_path):
                    # 如果文件存在，修改文件名，例如：filename_1.xlsx, filename_2.xlsx
                    new_filename = f'{out_groupby_2_sort_save}_{out_groupby_3_sort_save}_{out_column_save}_{counter}.xlsx'
                    df_export_path = os.path.join(export_path, new_filename)
                    counter += 1
                # 保存文件
                df_export_xlsx_fun.df_export_xlsx(out_groupby_3_df, df_export_path, index=False)

                out_number_total = out_groupby_3_df[value_column].sum()
                out_groupby_3_summary['out_groupby_3_sort'].append(out_groupby_3_sort)
                out_groupby_3_summary['out_groupby_3_value'].append(out_number_total)

            out_groupby_3_summary_dict[out_groupby_2_sort_cleaned] = pd.DataFrame(out_groupby_3_summary).sort_values(by='out_groupby_3_value', ascending=False)

            out_groupby_3_summary['out_groupby_3_sort'].clear()
            out_groupby_3_summary['out_groupby_3_value'].clear()

            out_groupby_2_summary_df_not_sorted = pd.DataFrame(out_groupby_2_summary)
            out_groupby_2_summary_df = out_groupby_2_summary_df_not_sorted.sort_values(by='out_groupby_2_value', ascending=False)

        fill_text += export_tree_new_xlsx_fun.export_tree_new_xlsx(target_file_path,
                                                                   in_groupby_2_summary_df, 'in_groupby_2_sort', in_priority_list, in_groupby_3_summary_dict,
                                                                   in_summary_total, out_summary_total,
                                                                   out_groupby_2_summary_df, 'out_groupby_2_sort', out_priority_list, out_groupby_3_summary_dict)
        
        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 将文件名中的非法字符替换为下划线 _
    def sanitize_filename(self, filename):

        try:
            # 正则表达式匹配非法字符
            sanitized = re.sub(r'[\\\/:*?"<>|]', '_', filename)
        except:
            sanitized = filename

        return sanitized