# gui_tk_in_out_value_check.py

import os
import pandas as pd
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from gui_tk import gui_tk_area_text
from gui_tk import gui_tk_import_xlsx_xls_csv_txt
from dataframe_tools_pd import df_review_xlsx_fun
from dataframe_tools_pd import df_col_label_fun
from dataframe_tools_pd import in_out_value_check_sum_fun
from dataframe_tools_pd import in_out_value_check_layering_fun
from xlsx_tools_openxl import create_new_xlsx_fun

gui_tk_import_xlsx_xls_csv_txt_py = gui_tk_import_xlsx_xls_csv_txt.gui_tk_import_xlsx_xls_csv_txt_class()

class gui_tk_in_out_value_check_class:

    sheet_1_df = pd.DataFrame()
    sheet_2_df = pd.DataFrame()

    def gui_tk_in_out_value_check_frame(self, root, control_frame_config, text_area):

        options_blank = []
        options_time_series = control_frame_config['widget_text'][0]
        options_in_out_mode = control_frame_config['widget_text'][1]

        frame_result = tk.Frame(root)
        frame_result.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=5, pady=(10, 5))

        # sheet_1
        frame_result.frame_sheet_1_path = tk.Frame(frame_result)
        frame_result.frame_sheet_1_path.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_sheet_1_path, text=control_frame_config['widget_text'][2], width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_1_path.entry_sheet_1_path = tk.Entry(frame_result.frame_sheet_1_path, state='readonly', readonlybackground='white')
        frame_result.frame_sheet_1_path.entry_sheet_1_path.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)


        frame_result.frame_sheet_1_first = tk.Frame(frame_result)
        frame_result.frame_sheet_1_first.pack(side=tk.TOP, fill=tk.BOTH)

        tk.Label(frame_result.frame_sheet_1_first, text=control_frame_config['widget_text'][3], width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_1_first.entry_sheet_1_name = tk.Entry(frame_result.frame_sheet_1_first, state='readonly', readonlybackground='white', width=21)
        frame_result.frame_sheet_1_first.entry_sheet_1_name.pack(side=tk.LEFT, padx=5, pady=5)

        tk.Label(frame_result.frame_sheet_1_first, text=control_frame_config['widget_text'][4], width=14, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_1_first.combobox_sheet_1_time_series = ttk.Combobox(frame_result.frame_sheet_1_first, values=options_time_series, height=10, width=15, state='readonly')
        frame_result.frame_sheet_1_first.combobox_sheet_1_time_series.set(options_time_series[0])
        frame_result.frame_sheet_1_first.combobox_sheet_1_time_series.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_1_first, text=control_frame_config['widget_text'][5], width=9, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_1_first.combobox_sheet_1_item = ttk.Combobox(frame_result.frame_sheet_1_first, values=options_blank, height=10, width=20, state='readonly')
        frame_result.frame_sheet_1_first.combobox_sheet_1_item.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_1_first, text=control_frame_config['widget_text'][6], width=14, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_1_first.combobox_sheet_1_in_out_mode = ttk.Combobox(frame_result.frame_sheet_1_first, values=options_in_out_mode, height=10, width=15, state='readonly')
        frame_result.frame_sheet_1_first.combobox_sheet_1_in_out_mode.set(options_in_out_mode[0])
        frame_result.frame_sheet_1_first.combobox_sheet_1_in_out_mode.pack(side=tk.LEFT, padx=(5, 5), pady=5)


        frame_result.frame_sheet_1_second = tk.Frame(frame_result)
        frame_result.frame_sheet_1_second.pack(side=tk.TOP, fill=tk.BOTH)

        tk.Label(frame_result.frame_sheet_1_second, text=control_frame_config['widget_text'][7], width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_1_second.combobox_sheet_1_in_col = ttk.Combobox(frame_result.frame_sheet_1_second, values=options_blank, height=10, width=19, state='readonly')
        frame_result.frame_sheet_1_second.combobox_sheet_1_in_col.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_1_second, text=control_frame_config['widget_text'][8], width=12, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_1_second.combobox_sheet_1_out_col = ttk.Combobox(frame_result.frame_sheet_1_second, values=options_blank, height=10, width=17, state='readonly')
        frame_result.frame_sheet_1_second.combobox_sheet_1_out_col.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_1_second, text=control_frame_config['widget_text'][9], width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_1_second.combobox_sheet_1_reserved_1 = ttk.Combobox(frame_result.frame_sheet_1_second, values=options_blank, height=10, width=21, state='readonly')
        frame_result.frame_sheet_1_second.combobox_sheet_1_reserved_1.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_1_second, text=control_frame_config['widget_text'][10], width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_1_second.combobox_sheet_1_reserved_2 = ttk.Combobox(frame_result.frame_sheet_1_second, values=options_blank, height=10, width=21, state='readonly')
        frame_result.frame_sheet_1_second.combobox_sheet_1_reserved_2.pack(side=tk.LEFT, padx=(5, 12), pady=5)


        frame_result.frame_sheet_1_third = tk.Frame(frame_result)
        frame_result.frame_sheet_1_third.pack(side=tk.TOP, fill=tk.BOTH)

        tk.Label(frame_result.frame_sheet_1_third, text=control_frame_config['widget_text'][11], width=13, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_1_third.combobox_sheet_1_in_out_col = ttk.Combobox(frame_result.frame_sheet_1_third, values=options_blank, height=10, width=16, state='readonly')
        frame_result.frame_sheet_1_third.combobox_sheet_1_in_out_col.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_1_third, text=control_frame_config['widget_text'][12], width=12, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_1_third.combobox_sheet_1_in_label = ttk.Combobox(frame_result.frame_sheet_1_third, values=options_blank, height=10, width=17, state='readonly')
        frame_result.frame_sheet_1_third.combobox_sheet_1_in_label.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_1_third, text=control_frame_config['widget_text'][13], width=13, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_1_third.combobox_sheet_1_out_label = ttk.Combobox(frame_result.frame_sheet_1_third, values=options_blank, height=10, width=16, state='readonly')
        frame_result.frame_sheet_1_third.combobox_sheet_1_out_label.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_1_third, text=control_frame_config['widget_text'][14], width=14, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_1_third.combobox_sheet_1_in_out_value = ttk.Combobox(frame_result.frame_sheet_1_third, values=options_blank, height=10, width=15, state='readonly')
        frame_result.frame_sheet_1_third.combobox_sheet_1_in_out_value.pack(side=tk.LEFT, padx=(5, 5), pady=5)


        # sheet 2
        frame_result.frame_sheet_2_path = tk.Frame(frame_result)
        frame_result.frame_sheet_2_path.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_sheet_2_path, text=control_frame_config['widget_text'][15], width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_2_path.entry_sheet_2_path = tk.Entry(frame_result.frame_sheet_2_path, state='readonly', readonlybackground='white')
        frame_result.frame_sheet_2_path.entry_sheet_2_path.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)


        frame_result.frame_sheet_2_first = tk.Frame(frame_result)
        frame_result.frame_sheet_2_first.pack(side=tk.TOP, fill=tk.BOTH)

        tk.Label(frame_result.frame_sheet_2_first, text=control_frame_config['widget_text'][16], width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_2_first.entry_sheet_2_name = tk.Entry(frame_result.frame_sheet_2_first, state='readonly', readonlybackground='white', width=21)
        frame_result.frame_sheet_2_first.entry_sheet_2_name.pack(side=tk.LEFT, padx=5, pady=5)

        tk.Label(frame_result.frame_sheet_2_first, text=control_frame_config['widget_text'][17], width=14, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_2_first.combobox_sheet_2_time_series = ttk.Combobox(frame_result.frame_sheet_2_first, values=options_time_series, height=10, width=15, state='readonly')
        frame_result.frame_sheet_2_first.combobox_sheet_2_time_series.set(options_time_series[0])
        frame_result.frame_sheet_2_first.combobox_sheet_2_time_series.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_2_first, text=control_frame_config['widget_text'][18], width=9, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_2_first.combobox_sheet_2_item = ttk.Combobox(frame_result.frame_sheet_2_first, values=options_blank, height=10, width=20, state='readonly')
        frame_result.frame_sheet_2_first.combobox_sheet_2_item.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_2_first, text=control_frame_config['widget_text'][19], width=14, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_2_first.combobox_sheet_2_in_out_mode = ttk.Combobox(frame_result.frame_sheet_2_first, values=options_in_out_mode, height=10, width=15, state='readonly')
        frame_result.frame_sheet_2_first.combobox_sheet_2_in_out_mode.set(options_in_out_mode[0])
        frame_result.frame_sheet_2_first.combobox_sheet_2_in_out_mode.pack(side=tk.LEFT, padx=(5, 5), pady=5)


        frame_result.frame_sheet_2_second = tk.Frame(frame_result)
        frame_result.frame_sheet_2_second.pack(side=tk.TOP, fill=tk.BOTH)

        tk.Label(frame_result.frame_sheet_2_second, text=control_frame_config['widget_text'][20], width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_2_second.combobox_sheet_2_in_col = ttk.Combobox(frame_result.frame_sheet_2_second, values=options_blank, height=10, width=19, state='readonly')
        frame_result.frame_sheet_2_second.combobox_sheet_2_in_col.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_2_second, text=control_frame_config['widget_text'][21], width=12, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_2_second.combobox_sheet_2_out_col = ttk.Combobox(frame_result.frame_sheet_2_second, values=options_blank, height=10, width=17, state='readonly')
        frame_result.frame_sheet_2_second.combobox_sheet_2_out_col.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_2_second, text=control_frame_config['widget_text'][22], width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_2_second.combobox_sheet_2_reserved_1 = ttk.Combobox(frame_result.frame_sheet_2_second, values=options_blank, height=10, width=21, state='readonly')
        frame_result.frame_sheet_2_second.combobox_sheet_2_reserved_1.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_2_second, text=control_frame_config['widget_text'][23], width=8, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_2_second.combobox_sheet_2_reserved_2 = ttk.Combobox(frame_result.frame_sheet_2_second, values=options_blank, height=10, width=21, state='readonly')
        frame_result.frame_sheet_2_second.combobox_sheet_2_reserved_2.pack(side=tk.LEFT, padx=(5, 12), pady=5)


        frame_result.frame_sheet_2_third = tk.Frame(frame_result)
        frame_result.frame_sheet_2_third.pack(side=tk.TOP, fill=tk.BOTH)

        tk.Label(frame_result.frame_sheet_2_third, text=control_frame_config['widget_text'][24], width=13, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_2_third.combobox_sheet_2_in_out_col = ttk.Combobox(frame_result.frame_sheet_2_third, values=options_blank, height=10, width=16, state='readonly')
        frame_result.frame_sheet_2_third.combobox_sheet_2_in_out_col.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_2_third, text=control_frame_config['widget_text'][25], width=12, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_2_third.combobox_sheet_2_in_label = ttk.Combobox(frame_result.frame_sheet_2_third, values=options_blank, height=10, width=17, state='readonly')
        frame_result.frame_sheet_2_third.combobox_sheet_2_in_label.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_2_third, text=control_frame_config['widget_text'][26], width=13, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_2_third.combobox_sheet_2_out_label = ttk.Combobox(frame_result.frame_sheet_2_third, values=options_blank, height=10, width=16, state='readonly')
        frame_result.frame_sheet_2_third.combobox_sheet_2_out_label.pack(side=tk.LEFT, padx=(5, 12), pady=5)

        tk.Label(frame_result.frame_sheet_2_third, text=control_frame_config['widget_text'][27], width=14, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_sheet_2_third.combobox_sheet_2_in_out_value = ttk.Combobox(frame_result.frame_sheet_2_third, values=options_blank, height=10, width=15, state='readonly')
        frame_result.frame_sheet_2_third.combobox_sheet_2_in_out_value.pack(side=tk.LEFT, padx=(5, 5), pady=5)


        # 按钮行
        frame_result.frame_button = tk.Frame(frame_result)
        frame_result.frame_button.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][28],
                  command=lambda:self.import_sheet(root,
                                                   frame_result.frame_sheet_1_path.entry_sheet_1_path,
                                                   frame_result.frame_sheet_1_first.entry_sheet_1_name,
                                                   frame_result.frame_sheet_1_first.combobox_sheet_1_item,
                                                   frame_result.frame_sheet_1_second.combobox_sheet_1_in_col,
                                                   frame_result.frame_sheet_1_second.combobox_sheet_1_out_col,
                                                   frame_result.frame_sheet_1_third.combobox_sheet_1_in_out_col,
                                                   frame_result.frame_sheet_1_third.combobox_sheet_1_in_out_value,
                                                   text_area,
                                                   1),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)
        
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][29],
                  command=lambda: self.button_preview_fun(text_area, 1),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)
        
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][30],
                  command=lambda: self.button_label_fun(frame_result.frame_sheet_1_third.combobox_sheet_1_in_out_col,
                                                        frame_result.frame_sheet_1_third.combobox_sheet_1_in_label,
                                                        frame_result.frame_sheet_1_third.combobox_sheet_1_out_label,
                                                        1),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)

        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][31],
                  command=lambda:self.import_sheet(root,
                                                   frame_result.frame_sheet_2_path.entry_sheet_2_path,
                                                   frame_result.frame_sheet_2_first.entry_sheet_2_name,
                                                   frame_result.frame_sheet_2_first.combobox_sheet_2_item,
                                                   frame_result.frame_sheet_2_second.combobox_sheet_2_in_col,
                                                   frame_result.frame_sheet_2_second.combobox_sheet_2_out_col,
                                                   frame_result.frame_sheet_2_third.combobox_sheet_2_in_out_col,
                                                   frame_result.frame_sheet_2_third.combobox_sheet_2_in_out_value,
                                                   text_area,
                                                   2),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)
        
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][32],
                  command=lambda: self.button_preview_fun(text_area, 2),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)
        
        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][33],
                  command=lambda: self.button_label_fun(frame_result.frame_sheet_2_third.combobox_sheet_2_in_out_col,
                                                        frame_result.frame_sheet_2_third.combobox_sheet_2_in_label,
                                                        frame_result.frame_sheet_2_third.combobox_sheet_2_out_label,
                                                        2),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)

        tk.Button(frame_result.frame_button, text=control_frame_config['widget_text'][34],
                  command=lambda: self.button_comparison_fun(frame_result.frame_sheet_1_first.entry_sheet_1_name,
                                                             frame_result.frame_sheet_1_first.combobox_sheet_1_time_series,
                                                             frame_result.frame_sheet_1_first.combobox_sheet_1_item,
                                                             frame_result.frame_sheet_1_first.combobox_sheet_1_in_out_mode,
                                                             frame_result.frame_sheet_1_second.combobox_sheet_1_in_col,
                                                             frame_result.frame_sheet_1_second.combobox_sheet_1_out_col,
                                                             frame_result.frame_sheet_1_third.combobox_sheet_1_in_out_col,
                                                             frame_result.frame_sheet_1_third.combobox_sheet_1_in_label,
                                                             frame_result.frame_sheet_1_third.combobox_sheet_1_out_label,
                                                             frame_result.frame_sheet_1_third.combobox_sheet_1_in_out_value,
                                                             frame_result.frame_sheet_2_first.entry_sheet_2_name,
                                                             frame_result.frame_sheet_2_first.combobox_sheet_2_time_series,
                                                             frame_result.frame_sheet_2_first.combobox_sheet_2_item,
                                                             frame_result.frame_sheet_2_first.combobox_sheet_2_in_out_mode,
                                                             frame_result.frame_sheet_2_second.combobox_sheet_2_in_col,
                                                             frame_result.frame_sheet_2_second.combobox_sheet_2_out_col,
                                                             frame_result.frame_sheet_2_third.combobox_sheet_2_in_out_col,
                                                             frame_result.frame_sheet_2_third.combobox_sheet_2_in_label,
                                                             frame_result.frame_sheet_2_third.combobox_sheet_2_out_label,
                                                             frame_result.frame_sheet_2_third.combobox_sheet_2_in_out_value,
                                                             text_area),
                  width=15).pack(side=tk.LEFT, padx=5, pady=5)


    # 导入数据按钮函数
    def import_sheet(self, root, entry_path, entry_sheet_name, combobox_sheet_item, combobox_sheet_in_col,
                     combobox_sheet_out_col, combobox_sheet_in_out_col, combobox_sheet_in_out_value, text_area, num):

        fill_text = ''

        result_df = gui_tk_import_xlsx_xls_csv_txt_py.gui_tk_import_xlsx_xls_csv_txt_frame(root)

        root.wait_window(result_df)

        if gui_tk_import_xlsx_xls_csv_txt_py.result_df is not None:

            if num ==1:
                path = gui_tk_import_xlsx_xls_csv_txt_py.path
                sheet_name = gui_tk_import_xlsx_xls_csv_txt_py.sheet_name
                self.sheet_1_df = gui_tk_import_xlsx_xls_csv_txt_py.result_df
                columns_title = self.sheet_1_df.columns.tolist()
                fill_text += 'Sheet 1 read successfully!\n'
            else:
                path = gui_tk_import_xlsx_xls_csv_txt_py.path
                sheet_name = gui_tk_import_xlsx_xls_csv_txt_py.sheet_name
                self.sheet_2_df = gui_tk_import_xlsx_xls_csv_txt_py.result_df
                columns_title = self.sheet_2_df.columns.tolist()
                fill_text += 'Sheet 2 read successfully!\n'

            entry_path.config(state='normal')
            entry_path.delete(0, tk.END)
            entry_path.insert(0, path)
            entry_path.config(state='readonly')

            entry_sheet_name.config(state='normal')
            entry_sheet_name.delete(0, tk.END)
            entry_sheet_name.insert(0, sheet_name)
            entry_sheet_name.config(state='readonly')

            combobox_sheet_item['values'] = columns_title
            combobox_sheet_item.set(columns_title[0])
            combobox_sheet_item.config(state='readonly')

            combobox_sheet_in_col['values'] = columns_title
            combobox_sheet_in_col.set(columns_title[0])
            combobox_sheet_in_col.config(state='readonly')

            combobox_sheet_out_col['values'] = columns_title
            combobox_sheet_out_col.set(columns_title[0])
            combobox_sheet_out_col.config(state='readonly')

            combobox_sheet_in_out_col['values'] = columns_title
            combobox_sheet_in_out_col.set(columns_title[0])
            combobox_sheet_in_out_col.config(state='readonly')

            combobox_sheet_in_out_value['values'] = columns_title
            combobox_sheet_in_out_value.set(columns_title[0])
            combobox_sheet_in_out_value.config(state='readonly')

            gui_tk_area_text.text_area_fill(text_area, fill_text)

        else:

            if num ==1:
                fill_text += 'Failed to read Sheet 1!\n'
            else:
                fill_text += 'Failed to read Sheet 2!\n'

            gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 数据预览
    def button_preview_fun(self, text_area, num):

        fill_text = ''

        if num == 1:
            result_info = df_review_xlsx_fun.df_review_xlsx(self.sheet_1_df)
            fill_text += result_info[1]
            gui_tk_area_text.text_area_fill(text_area, fill_text)
        else:
            result_info = df_review_xlsx_fun.df_review_xlsx(self.sheet_2_df)
            fill_text += result_info[1]
            gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 读取In/Out标签按钮函数
    def button_label_fun(self, combobox_col_in_out_label, combobox_col_in_label, combobox_col_out_label, num):

        sheet_in_out_col = combobox_col_in_out_label.get()
        unique_index_list_cleaned = []

        if num == 1:
            result_info = df_col_label_fun.df_col_label(self.sheet_1_df, sheet_in_out_col)
        else:
            result_info = df_col_label_fun.df_col_label(self.sheet_2_df, sheet_in_out_col)

        if result_info[0]:
            unique_index_list_cleaned = result_info[2]

        combobox_col_in_label['values'] = unique_index_list_cleaned
        if unique_index_list_cleaned[0]:
            combobox_col_in_label.set(unique_index_list_cleaned[0])
        combobox_col_in_label.config(state='readonly')
        
        combobox_col_out_label['values'] = unique_index_list_cleaned
        if unique_index_list_cleaned[0]:
            combobox_col_out_label.set(unique_index_list_cleaned[0])
        combobox_col_out_label.config(state='readonly')


    # 对比数据按钮函数
    def button_comparison_fun(self,
                              entry_sheet_1_name,
                              combobox_sheet_1_time_series, combobox_sheet_1_item,      combobox_sheet_1_in_out_mode,
                              combobox_sheet_1_in_col,      combobox_sheet_1_out_col,   combobox_sheet_1_in_out_col,
                              combobox_sheet_1_in_label,    combobox_sheet_1_out_label, combobox_sheet_1_in_out_value,
                              entry_sheet_2_name,
                              combobox_sheet_2_time_series, combobox_sheet_2_item,      combobox_sheet_2_in_out_mode,
                              combobox_sheet_2_in_col,      combobox_sheet_2_out_col,   combobox_sheet_2_in_out_col,
                              combobox_sheet_2_in_label,    combobox_sheet_2_out_label, combobox_sheet_2_in_out_value,
                              text_area):

        fill_text = ''

        sheet_1_name = entry_sheet_1_name.get()
        sheet_1_time_series = combobox_sheet_1_time_series.get()
        sheet_1_item = combobox_sheet_1_item.get()
        sheet_1_in_out_mode = combobox_sheet_1_in_out_mode.get()
        sheet_1_in_col = combobox_sheet_1_in_col.get()
        sheet_1_out_col = combobox_sheet_1_out_col.get()
        sheet_1_in_out_col = combobox_sheet_1_in_out_col.get()
        sheet_1_in_label = combobox_sheet_1_in_label.get()
        sheet_1_out_label = combobox_sheet_1_out_label.get()
        sheet_1_in_out_value = combobox_sheet_1_in_out_value.get()
        sheet_2_name = entry_sheet_2_name.get()
        sheet_2_time_series = combobox_sheet_2_time_series.get()
        sheet_2_item = combobox_sheet_2_item.get()
        sheet_2_in_out_mode = combobox_sheet_2_in_out_mode.get()
        sheet_2_in_col = combobox_sheet_2_in_col.get()
        sheet_2_out_col = combobox_sheet_2_out_col.get()
        sheet_2_in_out_col = combobox_sheet_2_in_out_col.get()
        sheet_2_in_label = combobox_sheet_2_in_label.get()
        sheet_2_out_label = combobox_sheet_2_out_label.get()
        sheet_2_in_out_value = combobox_sheet_2_in_out_value.get()

        file_path = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel Files', '*.xlsx')])

        sheet_name_list = ['数值合计对比',
                           '共同数值但计数不同sheet_in_1',  '共同数值但计数不同sheet_in_2',
                           '只在sheet_in_1中出现的数值',    '只在sheet_in_2中出现的数值',
                           '共同数值但计数不同sheet_out_1', '共同数值但计数不同sheet_out_2',
                           '只在sheet_out_1中出现的数值',   '只在sheet_out_2中出现的数值',
                           'sheet_in按item分类汇总',       'sheet_out按item分类汇总',
                           'sheet_in按时序排列',           'sheet_out按时序排列'                          
                           ]
        fill_text += create_new_xlsx_fun.create_new_xlsx(file_path, sheet_name_list)

        # sheet_1
        if sheet_1_time_series == '反向':
            self.sheet_1_df[:] = self.sheet_1_df.iloc[::-1].values

        # sheet_2
        if sheet_2_time_series == '反向':
            self.sheet_2_df[:] = self.sheet_2_df.iloc[::-1].values

        # 对比模式一：对比交易记录的数量与金额
        fill_text += in_out_value_check_sum_fun.in_out_value_check_sum(sheet_1_name, sheet_1_in_out_mode,
                                                                       self.sheet_1_df, sheet_1_in_col, sheet_1_out_col,
                                                                       sheet_1_in_out_value, sheet_1_in_out_col,
                                                                       sheet_1_in_label, sheet_1_out_label,
                                                                       sheet_2_name, sheet_2_in_out_mode,
                                                                       self.sheet_2_df, sheet_2_in_col, sheet_2_out_col,
                                                                       sheet_2_in_out_value, sheet_2_in_out_col,
                                                                       sheet_2_in_label, sheet_2_out_label,
                                                                       file_path)

        # 对比模式二：数值分层对比 + 对比模式三：按item分类汇总 + 对比模式四：按时序排列
        fill_text += in_out_value_check_layering_fun.in_out_value_check_layering(sheet_1_name, sheet_2_name,
                                                                                 sheet_1_in_out_mode, self.sheet_1_df,
                                                                                 sheet_1_in_col, sheet_1_out_col,
                                                                                 sheet_1_in_out_value, sheet_1_in_out_col,
                                                                                 sheet_1_in_label, sheet_1_out_label,
                                                                                 sheet_2_in_out_mode, self.sheet_2_df,
                                                                                 sheet_2_in_col, sheet_2_out_col,
                                                                                 sheet_2_in_out_value, sheet_2_in_out_col,
                                                                                 sheet_2_in_label, sheet_2_out_label,
                                                                                 sheet_1_item, sheet_2_item,
                                                                                 file_path)

        subprocess.run(['open', file_path])
        gui_tk_area_text.text_area_fill(text_area, fill_text)