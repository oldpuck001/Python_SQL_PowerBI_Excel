# tkinter_examples_3.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
from tkinter.scrolledtext import ScrolledText

def show_info():
    messagebox.showinfo("訊息", "Button 被按下")

def select_directory():
    path = filedialog.askdirectory()
    if path:
        messagebox.showinfo("選擇的資料夾", path)

# -------------------------
# 建立可滾動 Frame
# -------------------------
class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        canvas = tk.Canvas(self, height=600)  # 控制可視高度
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")


# -------------------------
# 主視窗
# -------------------------
root = tk.Tk()
root.title("Tkinter 控件示範（可滾動）")
root.geometry("420x650")

# 可滾動內容區
main = ScrollableFrame(root)
main.pack(fill="both", expand=True)

frame = main.scrollable_frame  # 之後把控件丟到 frame 即可

# -------------------------
# 加入所有控件
# -------------------------

ttk.Label(frame, text="Label 控件").pack(pady=5)
ttk.Button(frame, text="Button", command=show_info).pack(pady=5)

# Entry
ttk.Label(frame, text="Entry：").pack()
ttk.Entry(frame).pack(pady=5)

# ScrolledText
ttk.Label(frame, text="ScrolledText：").pack()
ScrolledText(frame, width=40, height=5).pack(pady=5)

# Checkbutton
check_var = tk.IntVar()
ttk.Checkbutton(frame, text="Checkbutton", variable=check_var).pack(pady=5)

# Radiobutton
ttk.Label(frame, text="Radiobutton：").pack()
radio_var = tk.StringVar(value="A")
ttk.Radiobutton(frame, text="A", variable=radio_var, value="A").pack()
ttk.Radiobutton(frame, text="B", variable=radio_var, value="B").pack()

# Listbox
ttk.Label(frame, text="Listbox：").pack()
lb = tk.Listbox(frame, height=4)
for i in ["蘋果", "香蕉", "葡萄"]:
    lb.insert(tk.END, i)
lb.pack(pady=5)

# Scale
ttk.Label(frame, text="Scale：").pack()
tk.Scale(frame, from_=0, to=100, orient="horizontal").pack(pady=5)

# Spinbox
ttk.Label(frame, text="Spinbox：").pack()
tk.Spinbox(frame, from_=1, to=10).pack(pady=5)

# OptionMenu
ttk.Label(frame, text="OptionMenu：").pack()
opt_var = tk.StringVar(value="A")
tk.OptionMenu(frame, opt_var, "A", "B", "C").pack(pady=5)

# Combobox
ttk.Label(frame, text="ttk.Combobox：").pack()
combo = ttk.Combobox(frame, values=["台北", "台中", "高雄"])
combo.current(0)
combo.pack(pady=5)

# Treeview
ttk.Label(frame, text="ttk.Treeview：").pack()
tree = ttk.Treeview(frame, columns=("姓名", "年齡"), show="headings", height=4)
tree.heading("姓名", text="姓名")
tree.heading("年齡", text="年齡")
tree.insert("", tk.END, values=("小明", 20))
tree.insert("", tk.END, values=("小美", 18))
tree.pack(pady=5)

# Progressbar
ttk.Label(frame, text="ttk.Progressbar：").pack()
progress = ttk.Progressbar(frame, length=200, mode='determinate')
progress["value"] = 55
progress.pack(pady=5)

# Notebook Tabs
ttk.Label(frame, text="Notebook Tabs：").pack()
nb = ttk.Notebook(frame)
tab1 = ttk.Frame(nb)
tab2 = ttk.Frame(nb)
nb.add(tab1, text="Tab 1")
nb.add(tab2, text="Tab 2")
nb.pack(pady=5)

ttk.Label(tab1, text="這是 Tab 1").pack()
ttk.Label(tab2, text="這是 Tab 2").pack()

# Canvas
ttk.Label(frame, text="Canvas：").pack()
canvas = tk.Canvas(frame, width=150, height=100, bg="white")
canvas.pack()
canvas.create_line(10, 10, 140, 10)
canvas.create_rectangle(20, 30, 80, 80, outline="blue")
canvas.create_text(70, 90, text="Canvas")

# LabelFrame
lf = ttk.LabelFrame(frame, text="LabelFrame 範例")
lf.pack(pady=10)
ttk.Label(lf, text="放在 LabelFrame 裡").pack()

# askdirectory
ttk.Button(frame, text="選擇資料夾 (askdirectory)", command=select_directory).pack(pady=10)

root.mainloop()