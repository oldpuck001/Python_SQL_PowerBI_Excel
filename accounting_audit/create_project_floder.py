# create_project_floder.py

# 创建项目文件夹

import os
import sys
import ast
import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText


class App:

    # 默认值
    path_fill = '''[
    ['项目数据'],

    ['审计底稿', 
                    [
                        ['1.初步业务活动'],
                        ['2.风险评估'],
                        ['3.控制测试'],
                        ['4.实质性程序'],
                        ['5.其他项目'],
                        ['6.完成审计工作'],
                        ['7.永久性档案'],
                        ['8.底稿附件'],
                        ['9.记账凭证检查拍照'],
                    ]
    ],
    
    ['审计报告'],

    ['原始资料']
]'''

    def __init__(self):

        self.root = tk.Tk()                                             # 创建tk实例

        self.root.title('建立项目文件夹')                                 # 设置窗口标题

        self.root.geometry('720x480+50+50')                             # 设置窗口的大小和位置

        self.root.resizable(False, False)                               # 设置窗口是否可以调整大小

        if sys.platform == 'darwin':
            self.root.after(200, self.bring_to_front)                   # macOS workaround: mainloop開始後再將視窗浮前

        # 文件夹结构
        self.frame_folder_structure = tk.Frame(self.root)
        self.frame_folder_structure.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tk.Label(self.frame_folder_structure, text='Folder Structure', anchor='w').pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        self.folder_structure = ScrolledText(self.frame_folder_structure, height=21)
        self.folder_structure.pack(side=tk.TOP, expand=True, fill=tk.X)
        self.folder_structure.insert(tk.INSERT, self.path_fill)
        self.folder_structure.see(tk.END)  

        # 按钮
        self.frame_button = tk.Frame(self.root)
        self.frame_folder_structure.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tk.Button(self.frame_folder_structure, text='建立文件夹结构',
                  command=lambda: self.add_folder(self.folder_structure,
                                                  self.text_area),
                  width=25).pack(side=tk.TOP, padx=5, pady=(15, 0))

        # 操作记录区
        self.frame_text_area = tk.Frame(self.root)
        self.frame_text_area.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=5, pady=(0, 5))
        tk.Label(self.frame_text_area, text='Operation Log', anchor='w').pack(side=tk.TOP, fill=tk.X, padx=5, pady=(0, 5))
        self.text_area = ScrolledText(self.frame_text_area, height=5)
        self.text_area.pack(side=tk.TOP, expand=True, fill=tk.X)
        self.text_area.config(state='disabled')


    # MacOS弹出窗口用
    def bring_to_front(self):
        self.root.lift()
        self.root.focus_force()
        self.root.call('wm', 'attributes', '.', '-topmost', '1')
        self.root.call('wm', 'attributes', '.', '-topmost', '0')


    def add_folder(self, folder_structure_widget, text_area):

        folder_structure = folder_structure_widget.get('1.0', 'end-1c')

        path_list = ast.literal_eval(folder_structure)

        path = filedialog.askdirectory()

        if path:

            for path_m in path_list:

                self.path_join(path, path_m)
            result_text = f'Path: {path}\nCreate successful!\n'

        else:

            result_text = f'Path: {path}\nCreate failed!\n'


        text_area.config(state='normal')                                        # 临时启用
        text_area.insert(tk.INSERT, result_text)
        text_area.see(tk.END)                                                   # 滚动到底部
        text_area.config(state='disabled')                                      # 重新禁用


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



app = App()
app.root.mainloop()