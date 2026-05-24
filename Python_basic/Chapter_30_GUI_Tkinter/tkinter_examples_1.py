# tkinter_examples_1.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

def show_info():
    messagebox.showinfo("訊息", "你按下了 Button")

root = tk.Tk()
root.title("Tkinter 控件示範")
root.geometry("800x700")

# ============= Label =============
# 顯示文字或圖片
tk.Label(root, text="這是 Label").pack(pady=5)

# ============= Button =============
# 一般按鈕
tk.Button(root, text="一般 Button", command=show_info).pack(pady=5)

# ============= Entry =============
# 單行文字輸入框
tk.Label(root, text="Entry：").pack()
entry = tk.Entry(root)
entry.pack(pady=5)

# ============= ScrolledText =============
# 有捲動條的多行文字輸入框
tk.Label(root, text="ScrolledText：").pack()
st = ScrolledText(root, width=40, height=5)
st.insert(tk.END, "這是 ScrolledText，可以捲動的多行文字框\n")
st.pack(pady=5)

# ============= Checkbutton =============
# 勾選方塊
check_var = tk.IntVar()
tk.Checkbutton(root, text="Checkbutton", variable=check_var).pack(pady=5)

# ============= Radiobutton =============
# 單選按鈕
radio_var = tk.StringVar(value="A")
tk.Radiobutton(root, text="選項 A", variable=radio_var, value="A").pack()
tk.Radiobutton(root, text="選項 B", variable=radio_var, value="B").pack()

# ============= Listbox =============
# 列表框
tk.Label(root, text="Listbox：").pack()
lb = tk.Listbox(root, height=4)
for item in ["蘋果", "香蕉", "葡萄"]:
    lb.insert(tk.END, item)
lb.pack(pady=5)

# ============= Scale =============
# 滑桿（水平 / 垂直）
tk.Label(root, text="Scale：").pack()
tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL).pack(pady=5)

# ============= Spinbox =============
# 數值上下調整框
tk.Label(root, text="Spinbox：").pack()
tk.Spinbox(root, from_=1, to=10).pack(pady=5)

# ============= OptionMenu =============
# 下拉式選單（簡易版）
tk.Label(root, text="OptionMenu：").pack()
opt_var = tk.StringVar(value="A")
tk.OptionMenu(root, opt_var, "A", "B", "C").pack(pady=5)

# ============= ttk.Combobox =============
# 下拉式選單（進階版，建議用 ttk 版本）
tk.Label(root, text="ttk.Combobox：").pack()
combo = ttk.Combobox(root, values=["台北", "台中", "高雄"])
combo.current(0)
combo.pack(pady=5)

root.mainloop()