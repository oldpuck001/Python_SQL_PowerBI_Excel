# gui_tk_sheet_subtotals.py

import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from gui_tk import gui_tk_area_text
from dataframe_tools_pd import sheetnames_import_fun
from dataframe_tools_pd import columns_title_fun
from dataframe_tools_pd import sheet_pivot_table_fun
from xlsx_tools_openxl import export_pivot_new_xlsx_fun

class sheet_subtotals_ui_class:

    def gui_tk_sheet_subtotals_frame(self, root, control_frame_config, text_area):
        
        options_blank = []

        frame_result = tk.Frame(root)
        frame_result.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=(10, 5))

        frame_result.frame_path = tk.Frame(frame_result)
        frame_result.frame_path.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_path, text=control_frame_config['widget_text'][0], width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_path.entry_path = tk.Entry(frame_result.frame_path, state='readonly', readonlybackground='white')         # 创建Entry并保存引用
        frame_result.frame_path.entry_path.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        frame_result.frame_sheet_row = tk.Frame(frame_result)
        frame_result.frame_sheet_row.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_sheet_row, text=control_frame_config['widget_text'][1], width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_row.combobox_sheet = ttk.Combobox(frame_result.frame_sheet_row, values=options_blank, state='readonly', width=24)
        frame_result.frame_sheet_row.combobox_sheet.pack(side=tk.LEFT, padx=(5, 40), pady=5)
        tk.Label(frame_result.frame_sheet_row, text=control_frame_config['widget_text'][2], width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_row.combobox_row = ttk.Combobox(frame_result.frame_sheet_row, values=options_blank, state='readonly', width=24)
        frame_result.frame_sheet_row.combobox_row.pack(side=tk.LEFT, padx=5, pady=5)

        frame_result.frame_col_value = tk.Frame(frame_result)
        frame_result.frame_col_value.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_col_value, text=control_frame_config['widget_text'][3], width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_col_value.combobox_col = ttk.Combobox(frame_result.frame_col_value, values=options_blank, state='readonly', width=24)
        frame_result.frame_col_value.combobox_col.pack(side=tk.LEFT, padx=(5, 40), pady=5)
        tk.Label(frame_result.frame_col_value, text=control_frame_config['widget_text'][4], width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_col_value.combobox_value = ttk.Combobox(frame_result.frame_col_value, values=options_blank, state='readonly', width=24)
        frame_result.frame_col_value.combobox_value.pack(side=tk.LEFT, padx=5, pady=5)

        frame_result.frame_button = tk.Frame(frame_result)
        frame_result.frame_button.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][5],
                  command=lambda: self.input_sheet(frame_result.frame_path.entry_path,
                                                   frame_result.frame_sheet_row.combobox_sheet,
                                                   frame_result.frame_sheet_row.combobox_row,
                                                   frame_result.frame_col_value.combobox_col,
                                                   frame_result.frame_col_value.combobox_value,
                                                   text_area),
                  width=15).pack(side=tk.LEFT, padx=(180, 5), pady=5)
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][6],
                  command=lambda: self.subtotals_generate(frame_result.frame_path.entry_path,
                                                          frame_result.frame_sheet_row.combobox_sheet,
                                                          frame_result.frame_sheet_row.combobox_row,
                                                          frame_result.frame_col_value.combobox_col,
                                                          frame_result.frame_col_value.combobox_value,
                                                          text_area),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)

        frame_result.frame_sheet_row.combobox_sheet.bind('<<ComboboxSelected>>',
                                                 lambda event: self.on_sheet_change(event,
                                                                                    frame_result.frame_path.entry_path,
                                                                                    frame_result.frame_sheet_row.combobox_sheet,
                                                                                    frame_result.frame_sheet_row.combobox_row,
                                                                                    frame_result.frame_col_value.combobox_col,
                                                                                    frame_result.frame_col_value.combobox_value))

        return frame_result


    # 导入按钮函数
    def input_sheet(self, entry_path, combobox_sheet, combobox_row, combobox_col, combobox_value, text_area):

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

        self.on_sheet_change(None, entry_path, combobox_sheet, combobox_row, combobox_col, combobox_value)

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 自动更新列名列表
    def on_sheet_change(self, event, entry_path, combobox_sheet, combobox_row, combobox_col, combobox_value):

        file_path = entry_path.get()
        sheet_name = combobox_sheet.get()

        result = columns_title_fun.columns_title(file_path, sheet_name)

        if result[0]:

            new_options = result[2]

            combobox_row['values'] = new_options
            if new_options[0]:
                combobox_row.set(new_options[0])
            combobox_row.config(state='readonly')

            combobox_col['values'] = new_options
            if new_options[0]:
                combobox_col.set(new_options[0])
            combobox_col.config(state='readonly')

            combobox_value['values'] = new_options
            if new_options[0]:
                combobox_value.set(new_options[0])
            combobox_value.config(state='readonly')


    # 导出按钮函数
    def subtotals_generate(self, file_path, sheet_name, combobox_row, combobox_col, combobox_value, text_area):

        fill_text = ''
        file_path = file_path.get()
        sheet_name = sheet_name.get()
        row_value = combobox_row.get()
        column_value = combobox_col.get()
        subtotal_value = combobox_value.get()

        if column_value == row_value or column_value == subtotal_value or row_value == subtotal_value:

            fill_text += '行目录分类列、列标题分类列、数值列必须为不同列，请重新选择！'
        
        else:

            df_pivot_result = sheet_pivot_table_fun.sheet_pivot_table(file_path, sheet_name, row_value, column_value, subtotal_value)

            fill_text += df_pivot_result[1]

            if df_pivot_result[0]:

                df_pivot_table = df_pivot_result[2]

                result_info = export_pivot_new_xlsx_fun.export_pivot_new_xlsx(df_pivot_table)

                if result_info[0]:

                    fill_text += result_info[1]

                    subprocess.run(['open', result_info[2]])

                else:
                    fill_text += 'Export failed.'

        gui_tk_area_text.text_area_fill(text_area, fill_text)