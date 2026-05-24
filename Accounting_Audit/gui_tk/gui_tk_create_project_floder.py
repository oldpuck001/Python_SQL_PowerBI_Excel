# gui_tk_create_project_floder.py

import os
import ast
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from gui_tk import gui_tk_area_text

class gui_tk_create_project_floder_class:

    # 默认值
    path_fill = '''[
    ['项目数据'],

    ['审计底稿', 
                    [
                        ['营业执照+公司章程+基本存款账户信息'],
                        ['记账凭证检查拍照'],
                    ]
    ],
    
    ['审计报告'],

    ['原始资料']
]'''

    def gui_tk_create_project_floder_frame(self, root, control_frame_config, text_area):

        frame_result = tk.Frame(root)
        frame_result.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=(10, 5))

        # 文件夹结构
        frame_result.frame_folder_structure = tk.Frame(frame_result)
        frame_result.frame_folder_structure.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_folder_structure, text=control_frame_config['widget_text'][0], anchor='w').pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        frame_result.folder_structure = ScrolledText(frame_result.frame_folder_structure, height=15)
        frame_result.folder_structure.pack(side=tk.TOP, fill=tk.X, expand=True)
        frame_result.folder_structure.insert(tk.INSERT, self.path_fill)
        frame_result.folder_structure.see(tk.END)  

        # 按钮
        frame_result.frame_button = tk.Frame(frame_result)
        frame_result.frame_folder_structure.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Button(frame_result.frame_folder_structure, text=control_frame_config['widget_text'][1],
                  command=lambda: self.add_folder(frame_result.folder_structure,
                                                  text_area),
                  width=25).pack(side=tk.TOP, padx=5, pady=5)

        return frame_result


    def add_folder(self, folder_structure_widget, text_area):

        folder_structure = folder_structure_widget.get('1.0', 'end-1c')

        path_list = ast.literal_eval(folder_structure)

        path = filedialog.askdirectory()

        if path:

            for path_m in path_list:

                self.path_join(path, path_m)

            fill_text = f'Path: {path}\nCreate successful!\n'

        else:

            fill_text = f'Path: {path}\nCreate failed!\n'

        # 复制文件
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        source_file_path = os.path.join(current_script_dir, '..', 'xlsx_file', 'audit_data_analysis.xlsx')
        target_file_path = os.path.join(path, '项目数据', 'audit_data_analysis.xlsx')
        shutil.copy(source_file_path, target_file_path)

        source_file_path = os.path.join(current_script_dir, '..', 'xlsx_file', 'depreciation_amortization_line.xlsx')
        target_file_path = os.path.join(path, '项目数据', 'depreciation_amortization_line.xlsx')
        shutil.copy(source_file_path, target_file_path)

        source_file_path = os.path.join(current_script_dir, '..', 'xlsx_file', 'bank_account.xlsx')
        target_file_path = os.path.join(path, '项目数据', 'bank_account.xlsx')
        shutil.copy(source_file_path, target_file_path)

        source_file_path = os.path.join(current_script_dir, '..', 'xlsx_file', 'adjusting_entries.xlsx')
        target_file_path = os.path.join(path, '审计底稿', '调整分录.xlsx')
        shutil.copy(source_file_path, target_file_path)

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 创建文件夹递归函数
    def path_join(self, path, path_m):

        if isinstance(path_m, list):
            
            if len(path_m) == 1:

                path = os.path.join(path, path_m[0])

                os.makedirs(path, exist_ok=True)

            else:

                for n in path_m[1]:

                    self.path_join(os.path.join(path, path_m[0]), n)

        else:

            os.makedirs(path, exist_ok=True)