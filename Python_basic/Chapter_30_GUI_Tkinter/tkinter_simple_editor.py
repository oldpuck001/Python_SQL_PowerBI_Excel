# simple_editor.py

# 大型文本區域的控件：
# 要創建可滾動的多行文本區域，可結合使用控件Text和Scrollbar，但模塊tkinter.scrolledtext已經提供了一種實現。
# 對於ScrolledText對象，將使用其方法delete和insert來刪除文本。
# 調用方法delete和insert時，需要使用合適的參數來指定文本的位置。
# 例如，使用‘1.0’來指定第1行的第0個字符（即第一個字符前面），使用END來指定文本末尾，並使用INSERT來指定當前插入點。

# 簡單的GUI文本編輯器

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename

class App:

    file_path = ''

    def __init__(self, title='My Application', geometry='1280x720+50+35', minsize_x=640, minsize_y=360,
                 maxsize_x=1920, maxsize_y=1080, resizable_x=True, resizable_y=True):

        self.root = tk.Tk()                                                     # 创建tk实例

        self.root.title(title)                                                  # 设置窗口标题

        self.root.geometry(geometry)                                            # 设置窗口的大小和位置

        self.root.minsize(minsize_x, minsize_y)                                 # 设置窗口的最小大小

        self.root.maxsize(maxsize_x, maxsize_y)                                 # 设置窗口的最大大小

        self.root.resizable(resizable_x, resizable_y)                           # 设置窗口是否可以调整大小
    
        # macOS workaround: mainloop開始後再將視窗浮前
        self.root.after(200, self.bring_to_front)

        self.contents = ScrolledText(self.root)
        self.contents.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

        tk.Button(text='Open', command=self.open_file).pack(side=tk.LEFT)

        tk.Button(text='Save', command=self.save_file).pack(side=tk.LEFT)

        tk.Button(text='Save as…', command=self.save_as_file).pack(side=tk.LEFT)

    def bring_to_front(self):
        self.root.lift()
        self.root.focus_force()
        self.root.call('wm', 'attributes', '.', '-topmost', '1')
        self.root.call('wm', 'attributes', '.', '-topmost', '0')

    # Open
    def open_file(self, event=None):
        if self.contents.get('1.0',tk.END).strip() != '\n':
            answer = messagebox.askyesnocancel("Save changes?", "Do you want to save changes?")
            if answer is True:
                self.save_file()
            elif answer is False:
                pass            
            else:
                return
        self.file_path = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if self.file_path:
            self.contents.delete('1.0', tk.END)
            with open(self.file_path, 'r') as input_file:
                self.contents.insert(tk.INSERT, input_file.read())
        self.root.title("Text Editor - " + self.file_path)

    # # Save
    def save_file(self, event=None):
        if not self.file_path:
            self.save_as_file()
        else:
            with open(self.file_path, 'w') as output_file:
                output_file.write(self.contents.get('1.0', 'end-1c'))
        self.root.title("Text Editor - " + self.file_path)

    # Save As…
    def save_as_file(self, event=None):
        self.file_path = asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt"),("All Files","*.*")])
        if self.file_path:
            with open(self.file_path, 'w') as output_file:
                output_file.write(self.contents.get('1.0',tk.END+'-1c'))
        self.root.title("Text Editor - " + self.file_path)


app = App('Simple Editor', '1024x768+50+35')
app.root.mainloop()