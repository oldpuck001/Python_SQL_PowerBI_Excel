# gui_tk_root.py

import sys
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

from gui_tk import gui_tk_find_subset
from gui_tk import gui_tk_sheets_script
from gui_tk import gui_tk_sheet_comparision
from gui_tk import gui_tk_sheet_subtotals
from gui_tk import gui_tk_sheet_regex
from gui_tk import gui_tk_in_out_sort
from gui_tk import gui_tk_in_out_value_check
from gui_tk import gui_tk_account_data_clean


gui_tk_find_subset_py = gui_tk_find_subset.gui_tk_find_subset_class()
gui_tk_sheets_script_py = gui_tk_sheets_script.gui_tk_sheets_script_class()
gui_tk_sheet_comparision_py = gui_tk_sheet_comparision.gui_tk_sheet_comparision_class()
gui_tk_sheet_subtotals_py = gui_tk_sheet_subtotals.sheet_subtotals_ui_class()
gui_tk_sheet_regex_py = gui_tk_sheet_regex.gui_tk_sheet_regex_class()
gui_tk_in_out_sort_py = gui_tk_in_out_sort.gui_tk_in_out_sort_class()
gui_tk_in_out_value_check_py = gui_tk_in_out_value_check.gui_tk_in_out_value_check_class()
gui_tk_account_data_clean_py = gui_tk_account_data_clean.gui_tk_account_data_clean_class()



class App:
    def __init__(self, title='My Application', geometry='1024x768+140+130', minsize_x=640, minsize_y=360, maxsize_x=1920, maxsize_y=1080,
                    resizable_x=True, resizable_y=True, control_frame_n=0, control_frame_config=[]):

        self.root = tk.Tk()                                             # 创建tk实例

        self.root.title(title)                                          # 设置窗口标题

        self.root.geometry(geometry)                                    # 设置窗口的大小和位置

        self.root.minsize(minsize_x, minsize_y)                         # 设置窗口的最小大小

        self.root.maxsize(maxsize_x, maxsize_y)                         # 设置窗口的最大大小

        self.root.resizable(resizable_x, resizable_y)                   # 设置窗口是否可以调整大小

        if sys.platform == 'darwin':
            self.root.after(200, self.bring_to_front)                   # macOS workaround: mainloop開始後再將視窗浮前

        self.control_frame_n =control_frame_n                           # 自定义UI模块个数

        self.control_frame_config = control_frame_config                # 自定义UI模块参数                                           

        self.root.control_frame_list = []                               # 自定义模块框架列表

        # 操作记录区
        self.frame_text_area = tk.Frame(self.root)
        self.frame_text_area.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))
        tk.Label(self.frame_text_area, text='Operation Log', anchor='w').pack(side=tk.TOP, fill=tk.X, padx=5, pady=(0, 5))
        try:
            height_value = self.control_frame_config[self.control_frame_n]['text_area_hight']
            self.text_area = ScrolledText(self.frame_text_area, height=height_value)
        except:
            self.text_area = ScrolledText(self.frame_text_area)
        self.text_area.pack(side=tk.TOP, expand=True, fill=tk.X)
        self.text_area.config(state='disabled')

        # 选择选取控件区
        for n in range(control_frame_n):

            if self.control_frame_config[n]['name'] in ['find_subset']:
                self.root.control_frame_list.append(gui_tk_find_subset_py.
                                                    gui_tk_find_subset_frame(root=self.root,
                                                                             control_frame_config=self.control_frame_config[n],
                                                                             text_area=self.text_area))

            elif self.control_frame_config[n]['name'] in ['sheets_script']:
                self.root.control_frame_list.append(gui_tk_sheets_script_py.
                                                    gui_tk_sheets_script_frame(root=self.root,
                                                                               control_frame_config=self.control_frame_config[n],
                                                                               text_area=self.text_area))

            elif self.control_frame_config[n]['name'] in ['sheet_comparision']:
                self.root.control_frame_list.append(gui_tk_sheet_comparision_py.
                                                    gui_tk_sheet_comparision_frame(root=self.root,
                                                                                   control_frame_config=self.control_frame_config[n],
                                                                                   text_area=self.text_area))

            elif self.control_frame_config[n]['name'] in ['sheet_subtotals']:
                self.root.control_frame_list.append(gui_tk_sheet_subtotals_py.
                                                    gui_tk_sheet_subtotals_frame(root=self.root,
                                                                             control_frame_config=self.control_frame_config[n],
                                                                             text_area=self.text_area))

            elif self.control_frame_config[n]['name'] in ['sheet_regex']:
                self.root.control_frame_list.append(gui_tk_sheet_regex_py.
                                                    gui_tk_sheet_regex_frame(root=self.root,
                                                                             control_frame_config=self.control_frame_config[n],
                                                                             text_area=self.text_area))

            elif self.control_frame_config[n]['name'] in ['in_out_sort']:
                self.root.control_frame_list.append(gui_tk_in_out_sort_py.
                                                    gui_tk_in_out_sort_frame(root=self.root,
                                                                             control_frame_config=self.control_frame_config[n],
                                                                             text_area=self.text_area))

            elif self.control_frame_config[n]['name'] in ['in_out_value_check']:
                self.root.control_frame_list.append(gui_tk_in_out_value_check_py.
                                                    gui_tk_in_out_value_check_frame(root=self.root,
                                                                                    control_frame_config=self.control_frame_config[n],
                                                                                    text_area=self.text_area))

            elif self.control_frame_config[n]['name'] in ['account_data_clean']:
                 self.root.control_frame_list.append(gui_tk_account_data_clean_py.
                                                     gui_tk_account_data_clean_frame(root=self.root,
                                                                                     control_frame_config=self.control_frame_config[n],
                                                                                     text_area=self.text_area))

            # elif self.control_frame_config[n]['name'] in ['SQLite Database']:
            #      self.root.control_frame_list.append(gui_tk_sql_sqlite_py.gui_tk_sql_sqlite_frame(root=self.root,
            #                                                                                       control_frame_config=self.control_frame_config[n],
            #                                                                                       text_area=self.text_area))


    def bring_to_front(self):
        self.root.lift()
        self.root.focus_force()
        self.root.call('wm', 'attributes', '.', '-topmost', '1')
        self.root.call('wm', 'attributes', '.', '-topmost', '0')