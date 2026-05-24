# gui_tk_area_text.py

import tkinter as tk

# 操作日志填写
def text_area_fill(text_area, result_text):
    
    text_area.config(state='normal')                                        # 临时启用
    text_area.insert(tk.INSERT, result_text)
    text_area.see(tk.END)                                                   # 滚动到底部
    text_area.config(state='disabled')                                      # 重新禁用


# 清除内容
def text_area_clear(text_area):

    text_area.config(state='normal')                                        # 临时启用
    text_area.delete('1.0', 'end')
    text_area.see(tk.END)                                                   # 滚动到底部
    text_area.config(state='disabled')                                      # 重新禁用