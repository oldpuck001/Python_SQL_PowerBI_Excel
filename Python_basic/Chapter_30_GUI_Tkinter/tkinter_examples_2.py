# tkinter_examples_2.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog


def select_directory():
    path = filedialog.askdirectory()
    if path:
        messagebox.showinfo("選擇的資料夾", path)


root = tk.Tk()
root.title("Tkinter 控件示範")
root.geometry("800x700")

# ============= Treeview =============
# 樹狀表格（顯示資料表用）
tk.Label(root, text="ttk.Treeview：").pack()
tree = ttk.Treeview(root, columns=("col1", "col2"), show="headings", height=4)
tree.heading("col1", text="姓名")
tree.heading("col2", text="年齡")
tree.insert("", tk.END, values=("小明", 20))
tree.insert("", tk.END, values=("小美", 18))
tree.pack(pady=5)

# ============= Progressbar =============
# 進度條
tk.Label(root, text="ttk.Progressbar：").pack()
p = ttk.Progressbar(root, length=200, mode='determinate')
p["value"] = 60
p.pack(pady=5)

# ============= Notebook Tabs =============
# 分頁頁籤（Tabs）
tk.Label(root, text="ttk.Notebook：").pack()
notebook = ttk.Notebook(root)
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
notebook.add(tab1, text="分頁 1")
notebook.add(tab2, text="分頁 2")
notebook.pack(pady=5)

tk.Label(tab1, text="這是分頁 1").pack()
tk.Label(tab2, text="這是分頁 2").pack()

# ============= Canvas =============
# 用來畫線、矩形、圖片等
tk.Label(root, text="Canvas：").pack()
canvas = tk.Canvas(root, width=150, height=100, bg="white")
canvas.pack()
canvas.create_line(10, 10, 140, 10)
canvas.create_rectangle(20, 30, 80, 80, outline="blue")
canvas.create_text(75, 90, text="Canvas")

# ============= Frame / LabelFrame =============
# 一般容器框架 / 帶標題的框架
frame = tk.LabelFrame(root, text="LabelFrame 範例")
frame.pack(pady=10)
tk.Label(frame, text="這是放在 LabelFrame 裡的 Label").pack()

# ============= Directory Dialog =============
# 選擇資料夾
tk.Button(root, text="選擇資料夾 (askdirectory)", command=select_directory).pack(pady=10)

root.mainloop()