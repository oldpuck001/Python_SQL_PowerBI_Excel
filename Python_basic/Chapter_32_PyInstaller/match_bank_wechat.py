# match_bank_wechat.py

import os
import re
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd

class App:

    bank_file_path = ''
    wechat_file_path = ''

    title = '银行流水与微信支付记录匹配工具'
    geometry = '720x480+50+35'
    minsize_x = 640
    minsize_y = 540
    maxsize_x = 1920
    maxsize_y = 1080
    resizable_x = False
    resizable_y = False

    def __init__(self, title=title, geometry=geometry,
                       minsize_x=minsize_x, minsize_y=minsize_y,
                       maxsize_x=maxsize_x, maxsize_y=maxsize_y,
                       resizable_x=resizable_x, resizable_y=resizable_y):

        options_blank = []

        self.root = tk.Tk()                                                     # 创建tk实例

        self.root.title(title)                                                  # 设置窗口标题

        self.root.geometry(geometry)                                            # 设置窗口的大小和位置

        self.root.minsize(minsize_x, minsize_y)                                 # 设置窗口的最小大小

        self.root.maxsize(maxsize_x, maxsize_y)                                 # 设置窗口的最大大小

        self.root.resizable(resizable_x, resizable_y)                           # 设置窗口是否可以调整大小
    
        # macOS workaround: mainloop開始後再將視窗浮前
        self.root.after(200, self.bring_to_front)

        def on_entry_changed(*args):
            self.on_sheet_change(None, entry_path_bank, combobox_sheet_bank, entry_header_bank,
                                 combobox_date_bank, combobox_amount_bank, combobox_summary_bank, 
                                 combobox_counterparty_bank)

        # 银行流水
        frame_path_bank = tk.Frame(self.root)
        frame_path_bank.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_path_bank, text='银行流水文件', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=(10, 5))
        entry_path_bank = tk.Entry(frame_path_bank, state='readonly', readonlybackground='white')
        entry_path_bank.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 10), pady=(10, 5))

        frame_bank_one = tk.Frame(self.root)
        frame_bank_one.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_bank_one, text='表头所在行号', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        entry_header_bank = tk.Entry(frame_bank_one, width=16)
        entry_header_bank.pack(side=tk.LEFT, padx=(5, 25), pady=5)
        entry_header_bank.bind("<Return>", on_entry_changed)
        entry_header_bank.bind("<FocusOut>", on_entry_changed)
        tk.Label(frame_bank_one, text='交易日期列号', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        combobox_date_bank = ttk.Combobox(frame_bank_one, values=options_blank, state='readonly', width=16)
        combobox_date_bank.pack(side=tk.LEFT, padx=(5, 25), pady=5)
        tk.Label(frame_bank_one, text='交易金额列号', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        combobox_amount_bank = ttk.Combobox(frame_bank_one, values=options_blank, state='readonly', width=16)
        combobox_amount_bank.pack(side=tk.LEFT, padx=5, pady=5)

        frame_bank_two = tk.Frame(self.root)
        frame_bank_two.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_bank_two, text='选择工作表', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        combobox_sheet_bank = ttk.Combobox(frame_bank_two, values=options_blank, state='readonly', width=13)
        combobox_sheet_bank.pack(side=tk.LEFT, padx=(5, 25), pady=5)
        tk.Label(frame_bank_two, text='摘要列号', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        combobox_summary_bank = ttk.Combobox(frame_bank_two, values=options_blank, state='readonly', width=16)
        combobox_summary_bank.pack(side=tk.LEFT, padx=(5, 25), pady=5)
        tk.Label(frame_bank_two, text='对方账号列号', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        combobox_counterparty_bank = ttk.Combobox(frame_bank_two, values=options_blank, state='readonly', width=16)
        combobox_counterparty_bank.pack(side=tk.LEFT, padx=5, pady=5)

        # 微信流水文件路径
        frame_path_wechat = tk.Frame(self.root)
        frame_path_wechat.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_path_wechat, text='微信流水文件', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        entry_path_wechat = tk.Entry(frame_path_wechat, state='readonly', readonlybackground='white')
        entry_path_wechat.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(5, 10), pady=5)

        frame_wechat_one = tk.Frame(self.root)
        frame_wechat_one.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_wechat_one, text='表头所在行号', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        entry_header_wechat = tk.Entry(frame_wechat_one, width=16)
        entry_header_wechat.pack(side=tk.LEFT, padx=(5, 25), pady=5)
        entry_header_wechat.bind("<Return>", on_entry_changed)
        entry_header_wechat.bind("<FocusOut>", on_entry_changed)
        tk.Label(frame_wechat_one, text='交易日期列号', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        combobox_date_wechat = ttk.Combobox(frame_wechat_one, values=options_blank, state='readonly', width=16)
        combobox_date_wechat.pack(side=tk.LEFT, padx=(5, 25), pady=5)
        tk.Label(frame_wechat_one, text='交易金额列号', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        combobox_amount_wechat = ttk.Combobox(frame_wechat_one, values=options_blank, state='readonly', width=16)
        combobox_amount_wechat.pack(side=tk.LEFT, padx=5, pady=5)

        frame_wechat_two = tk.Frame(self.root)
        frame_wechat_two.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_wechat_two, text='选择工作表', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        combobox_sheet_wechat = ttk.Combobox(frame_wechat_two, values=options_blank, state='readonly', width=13)
        combobox_sheet_wechat.pack(side=tk.LEFT, padx=(5, 25), pady=5)
        tk.Label(frame_wechat_two, text='交易类型列号', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        combobox_summary_wechat = ttk.Combobox(frame_wechat_two, values=options_blank, state='readonly', width=16)
        combobox_summary_wechat.pack(side=tk.LEFT, padx=(5, 25), pady=5)
        tk.Label(frame_wechat_two, text='交易对方列号', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        combobox_counterparty_wechat = ttk.Combobox(frame_wechat_two, values=options_blank, state='readonly', width=16)
        combobox_counterparty_wechat.pack(side=tk.LEFT, padx=5, pady=5)

        # 按钮行
        frame_button = tk.Frame(self.root)
        frame_button.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Button(frame_button, text='读取银行流水文件',
                  command=lambda: self.select_file_bank(entry_path_bank,
                                                        combobox_sheet_bank,
                                                        entry_header_bank,
                                                        combobox_date_bank,
                                                        combobox_amount_bank,
                                                        combobox_summary_bank,
                                                        combobox_counterparty_bank,
                                                        text_area),
                  width=17).pack(side=tk.LEFT, padx=(15, 5), pady=5)

        tk.Button(frame_button, text='预览银行流水数据',
                  command=lambda: self.review_data(entry_path_bank,
                                                   combobox_sheet_bank,
                                                   entry_header_bank,
                                                   combobox_date_bank,
                                                   combobox_amount_bank,
                                                   combobox_summary_bank,
                                                   combobox_counterparty_bank,
                                                   text_area),
                  width=17).pack(side=tk.LEFT, padx=5, pady=5)
        
        tk.Button(frame_button, text='读取微信流水文件',
                  command=lambda: self.select_file_wechat(entry_path_wechat,
                                                          combobox_sheet_wechat,
                                                          entry_header_wechat,
                                                          combobox_date_wechat,
                                                          combobox_amount_wechat,
                                                          combobox_summary_wechat,
                                                          combobox_counterparty_wechat,
                                                          text_area),
                  width=17).pack(side=tk.LEFT, padx=5, pady=5)

        tk.Button(frame_button, text='预览微信流水数据',
                  command=lambda: self.review_data(entry_path_wechat,
                                                   combobox_sheet_wechat,
                                                   entry_header_wechat,
                                                   combobox_date_wechat,
                                                   combobox_amount_wechat,
                                                   combobox_summary_wechat,
                                                   combobox_counterparty_wechat,
                                                   text_area),
                  width=17).pack(side=tk.LEFT, padx=5, pady=5)

        tk.Button(frame_button, text='开始匹配',
                  command=lambda: self.match_data(entry_path_bank,
                                                  combobox_sheet_bank,
                                                  entry_header_bank,
                                                  combobox_date_bank,
                                                  combobox_amount_bank,
                                                  combobox_summary_bank,
                                                  combobox_counterparty_bank,
                                                  entry_path_wechat,
                                                  combobox_sheet_wechat,
                                                  entry_header_wechat,
                                                  combobox_date_wechat,
                                                  combobox_amount_wechat,
                                                  combobox_summary_wechat,
                                                  combobox_counterparty_wechat,
                                                  text_area),
                  width=17).pack(side=tk.LEFT, padx=5, pady=5)

        # 操作记录区
        frame_text_area = tk.Frame(self.root)
        frame_text_area.pack(side=tk.BOTTOM, fill=tk.BOTH)
        tk.Label(frame_text_area, text='操作记录', width=10, anchor='w').pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        text_area = ScrolledText(frame_text_area, height=19)
        text_area.pack(side=tk.TOP, expand=True, fill=tk.X, padx=5, pady=5)
        text_area.config(state='disabled')


    def bring_to_front(self):
        self.root.lift()
        self.root.focus_force()
        self.root.call('wm', 'attributes', '.', '-topmost', '1')
        self.root.call('wm', 'attributes', '.', '-topmost', '0')

    def select_file_bank(self, entry_path_bank, combobox_sheet_bank, entry_header_bank, combobox_date_bank,
                               combobox_amount_bank, combobox_summary_bank, combobox_counterparty_bank,
                               text_area):

        fill_text = ''
        path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx'),
                                                     ('Excel Files', '*.xls')])

        if path:
            entry_path_bank.config(state='normal')
            entry_path_bank.delete(0, tk.END)
            entry_path_bank.insert(0, path)
            entry_path_bank.config(state='readonly')
            fill_text += f'Selected: {path}\n'
            fill_text += 'File selection successful!\n'

            sheets_name_result = self.sheetnames_import(path)

            if sheets_name_result[0]:

                sheets_name_list = sheets_name_result[2]

                combobox_sheet_bank['values'] = sheets_name_list
                combobox_sheet_bank.set(sheets_name_list[0])               # 设置默认选择第一个
                combobox_sheet_bank.config(state='readonly')

            else:

                combobox_sheet_bank.set('')
                combobox_sheet_bank.config(state='disabled')

            fill_text += sheets_name_result[1]

        else:
            fill_text += f'File selection failed!\n'

        self.on_sheet_change(None, entry_path_bank, combobox_sheet_bank, entry_header_bank, combobox_date_bank,
                             combobox_amount_bank, combobox_summary_bank, combobox_counterparty_bank)

        self.text_area_fill(text_area, fill_text)

    def select_file_wechat(self, entry_path_wechat, combobox_sheet_wechat, entry_header_wechat, combobox_date_wechat,
                                 combobox_amount_wechat, combobox_summary_wechat, combobox_counterparty_wechat,
                                 text_area):

        fill_text = ''
        path = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx'),
                                                     ('Excel Files', '*.xls')])

        if path:
            entry_path_wechat.config(state='normal')
            entry_path_wechat.delete(0, tk.END)
            entry_path_wechat.insert(0, path)
            entry_path_wechat.config(state='readonly')
            fill_text += f'Selected: {path}\n'
            fill_text += 'File selection successful!\n'

            sheets_name_result = self.sheetnames_import(path)

            if sheets_name_result[0]:

                sheets_name_list = sheets_name_result[2]

                combobox_sheet_wechat['values'] = sheets_name_list
                combobox_sheet_wechat.set(sheets_name_list[0])               # 设置默认选择第一个
                combobox_sheet_wechat.config(state='readonly')

            else:

                combobox_sheet_wechat.set('')
                combobox_sheet_wechat.config(state='disabled')

            fill_text += sheets_name_result[1]

        else:
            fill_text += f'File selection failed!\n'

        self.on_sheet_change(None, entry_path_wechat, combobox_sheet_wechat, entry_header_wechat, combobox_date_wechat,
                             combobox_amount_wechat, combobox_summary_wechat, combobox_counterparty_wechat)

        self.text_area_fill(text_area, fill_text)

    def review_data(self, entry_path, combobox_sheet, entry_header, combobox_date, combobox_amount,
                          combobox_summary, combobox_counterparty, text_area):

        fill_text = ''

        file_path = entry_path.get()
        sheet_name = combobox_sheet.get()
        header_num = entry_header.get()
        if not header_num:
            header_num = 0
        date_col = combobox_date.get()
        amount_col = combobox_amount.get()
        summary_col = combobox_summary.get()
        counterparty_col = combobox_counterparty.get()

        result = self.read_xlsx_xls_csv_txt(file_path=file_path, sheet_name=sheet_name, header=header_num,
                                            usecols=[date_col, amount_col, summary_col, counterparty_col])

        if result[0]:

            df = result[2]
            fill_text += result[1]

            temp_folder = os.path.dirname(file_path)
            temp_path = os.path.join(temp_folder, 'bank_temp.xlsx')
            df.to_excel(temp_path, index=False)

            # macOS
            if os.name == 'posix':
                os.system(f'open "{temp_path}"')

            # Windows
            elif os.name == 'nt':
                os.startfile(temp_path)

            info = f'Preview file: {temp_path}\n'

            return [True, info, temp_path]

        else:

            fill_text += result[1]

        self.text_area_fill(text_area, fill_text)

    def match_data(self, entry_path_bank, combobox_sheet_bank, entry_header_bank, combobox_date_bank,
                         combobox_amount_bank, combobox_summary_bank, combobox_counterparty_bank,
                         entry_path_wechat, combobox_sheet_wechat, entry_header_wechat, combobox_date_wechat,
                         combobox_amount_wechat, combobox_summary_wechat, combobox_counterparty_wechat,
                   text_area):

        fill_text = ''

        path_bank = entry_path_bank.get()
        sheet_bank = combobox_sheet_bank.get()
        header_bank = entry_header_bank.get()
        if not header_bank:
            header_bank = 0
        date_bank = combobox_date_bank.get()
        amount_bank = combobox_amount_bank.get()
        summary_bank = combobox_summary_bank.get()
        counterparty_bank = combobox_counterparty_bank.get()
        path_wechat = entry_path_wechat.get()
        sheet_wechat = combobox_sheet_wechat.get()
        header_wechat = entry_header_wechat.get()
        if not header_wechat:
            header_wechat = 0
        date_wechat = combobox_date_wechat.get()
        amount_wechat = combobox_amount_wechat.get()
        summary_wechat = combobox_summary_wechat.get()
        counterparty_wechat = combobox_counterparty_wechat.get()

        # 读取银行流水
        result = self.read_xlsx_xls_csv_txt(file_path=path_bank, sheet_name=sheet_bank, header=header_bank,
                                            usecols=[date_bank, amount_bank, summary_bank, counterparty_bank])
        if result[0]:
            bank_data = result[2]
            fill_text += f'银行流水: {len(bank_data)} 条\n'
        else:
            fill_text += '没有解析到银行流水记录'
        self.text_area_fill(text_area, fill_text)
        fill_text = ''

        # 读取微信流水
        result = self.read_xlsx_xls_csv_txt(file_path=path_wechat, sheet_name=sheet_wechat, header=header_wechat,
                                            usecols=[date_wechat, amount_wechat, summary_wechat, counterparty_wechat])
        if result[0]:
            wechat_data = result[2]
            fill_text += f'微信流水: {len(wechat_data)} 条\n'
        else:
            fill_text += '没有解析到微信流水记录'
        self.text_area_fill(text_area, fill_text)
        fill_text = ''

        # 匹配
        result_df, matched_count, used_indices = self.match_records(bank_data, date_bank, amount_bank,
                                                                    wechat_data, date_wechat, amount_wechat, summary_wechat,
                                                                    text_area)
        
        fill_text = f'匹配完成！\n'
        fill_text += f'银行流水: {len(bank_data)} 条，匹配: {matched_count} 条'
        if len(bank_data) > 0:
            fill_text += f'匹配率: {matched_count/len(bank_data)*100:.1f}%'

        # 保存
        output_file = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel Files', '*.xlsx')])
        
        try:
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
                result_df.to_excel(writer, sheet_name='匹配结果', index=False)
                
                summary = pd.DataFrame({
                    '项目': ['时间', '银行文件', '微信文件', '银行总数', '匹配数', '匹配率'],
                    '内容': [
                        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        os.path.basename(path_bank),
                        os.path.basename(path_wechat),
                        len(bank_data),
                        matched_count,
                        f"{matched_count/len(bank_data)*100:.1f}%" if len(bank_data) > 0 else "0%"
                    ]
                })
                summary.to_excel(writer, sheet_name='统计信息', index=False)
                
                unmatched = result_df[result_df['匹配状态'] == '未匹配']
                if len(unmatched) > 0:
                    unmatched.to_excel(writer, sheet_name='未匹配银行流水', index=False)
                
                unused = set(range(len(wechat_data))) - used_indices
                if unused:
                    wechat_data.iloc[list(unused)].to_excel(writer, sheet_name='未匹配微信记录', index=False)
            
            fill_text = f'已保存: {output_file}\n'

        except Exception as e:

            fill_text = f'保存Excel失败: {e}\n'
            csv_file = output_file.replace('.xlsx', '.csv')
            result_df.to_csv(csv_file, index=False, encoding='utf-8-sig')
            fill_text =+ f'已保存CSV: {csv_file}\n'
        
        self.text_area_fill(text_area, fill_text)


    def extract_date(self, date_str):
        """提取日期"""
        if not date_str:
            return ''
        date_str = str(date_str).strip()
        match = re.search(r'(\d{4})[/-](\d{1,2})[/-](\d{1,2})', date_str)
        if match:
            return f"{match.group(1)}{int(match.group(2)):02d}{int(match.group(3)):02d}"
        match = re.search(r'(\d{4})(\d{2})(\d{2})', date_str)
        if match:
            return match.group()
        return re.sub(r'[^\d]', '', date_str)

    def is_withdrawal(self, trans_type):
        """判断是否提现"""
        if not trans_type:
            return False
        t = str(trans_type).lower()
        return any(k in t for k in ['提现', 'withdraw'])

    def is_consumption(self, trans_type):
        """判断是否消费"""
        if not trans_type:
            return True
        t = str(trans_type).lower()
        return any(k in t for k in ['转账', '消费', '付款', '支付', 'transfer', 'payment'])

    def match_records(self, bank_df, date_bank, amount_bank,
                            wechat_df, date_wechat, amount_wechat, summary_wechat,
                            text_area):
        
        """匹配记录"""
        if bank_df.empty or wechat_df.empty:
            return bank_df, 0, set()
        
        bank_df['匹配日期'] = bank_df[date_bank].apply(self.extract_date)
        wechat_df['匹配日期'] = wechat_df[date_wechat].apply(self.extract_date)
        
        matched_count = 0
        used_indices = set()
        
        result_df = bank_df.copy()
        result_df['微信交易类型'] = ''
        result_df['微信流水金额'] = ''
        result_df['微信转账对方'] = ''
        result_df['匹配状态'] = '未匹配'

        messagebox.showinfo('开始匹配', '开始匹配...\n窗口会无响应较长时间，请耐心等待！')

        for idx in range(len(bank_df)):
            try:
                bank_row = bank_df.iloc[idx]
                bank_amount = bank_row[amount_bank]
                bank_date = bank_row['匹配日期']
                
                if bank_amount == 0 or not bank_date:
                    continue
                
                bank_abs = abs(bank_amount)
                is_income = bank_amount > 0
                
                best_match = None
                best_idx = -1
                min_diff = float('inf')
                
                for w_idx in range(len(wechat_df)):
                    if w_idx in used_indices:
                        continue
                    
                    w_row = wechat_df.iloc[w_idx]
                    if w_row['匹配日期'] != bank_date:
                        continue
                    
                    w_amount = w_row[amount_wechat]
                    w_type = str(w_row[summary_wechat])
                    w_abs = abs(w_amount)
                    
                    # 方向匹配
                    if self.is_withdrawal(w_type) and not is_income:
                        continue
                    if self.is_consumption(w_type) and is_income:
                        continue
                    
                    diff = abs(bank_abs - w_abs)
                    diff_fee = abs(bank_abs - w_abs * 0.999)
                    cur_diff = min(diff, diff_fee)
                    
                    if cur_diff <= 1.0 and cur_diff < min_diff:
                        min_diff = cur_diff
                        best_match = w_row
                        best_idx = w_idx
                
                if best_match is not None:
                    result_df.loc[idx, '微信交易类型'] = str(best_match['交易类型'])
                    result_df.loc[idx, '微信流水金额'] = str(best_match['金额(元)'])
                    result_df.loc[idx, '微信转账对方'] = str(best_match['交易对方'])
                    result_df.loc[idx, '匹配状态'] = '已匹配'
                    used_indices.add(best_idx)
                    matched_count += 1
                    # print(f"✓ #{matched_count}: {bank_date} | 银行:{bank_abs:.2f} | 微信:{best_match['交易类型']} {w_abs:.2f}")
            except:
                continue
        
        result_df = result_df.drop('匹配日期', axis=1)
        return result_df, matched_count, used_indices

    def sheetnames_import(self, file_path):

        try:
            sheet_file = pd.ExcelFile(file_path)
            sheetnames = sheet_file.sheet_names
            info = 'Worksheet list successfully read!\n'
            return [True, info, sheetnames]
        
        except:
            sheetnames = []
            info = 'Failed to read worksheet list!\nThis feature is only supported for xlsx and xls format files.\n'
            return [False, info, sheetnames]

    # 自动更新列名列表
    def on_sheet_change(self, event, entry_path, combobox_sheet, entry_header, combobox_date,
                              combobox_amount, combobox_summary, combobox_counterparty):

        file_path = entry_path.get()
        sheet_name = combobox_sheet.get()
        header_num = entry_header.get()
        if not header_num:
            header_num = 0

        result = self.columns_title(file_path, sheet_name, header_num)

        if result[0]:

            new_options = result[2]

            combobox_date['values'] = new_options
            if new_options[0]:
                combobox_date.set(new_options[0])
            combobox_date.config(state='readonly')

            combobox_amount['values'] = new_options
            if new_options[0]:
                combobox_amount.set(new_options[0])
            combobox_amount.config(state='readonly')

            combobox_summary['values'] = new_options
            if new_options[0]:
                combobox_summary.set(new_options[0])
            combobox_summary.config(state='readonly')

            combobox_counterparty['values'] = new_options
            if new_options[0]:
                combobox_counterparty.set(new_options[0])
            combobox_counterparty.config(state='readonly')

    def columns_title(self, file_path, sheet_name, header_num):

        result = self.read_xlsx_xls_csv_txt(file_path=file_path, sheet_name=sheet_name, header=header_num)

        info = result[1]

        if result[0]:

            df = result[2]
            columns_title = df.columns.tolist()
            return [True, info, columns_title]
        
        else:

            columns_title = []
            return [False, info, columns_title]

    def read_xlsx_xls_csv_txt(self,
                              file_path = None,
                              sheet_name = 0,                     # 默认读取第一个工作表 (索引0)
                              skiprows = None,                    # 默认不跳过任何行
                              usecols = None,                     # 默认读取所有列
                              nrows = None,                       # 默认读取所有行
                              index_col = None,                   # 默认无索引列（生成RangeIndex）
                              header = 0,                         # 默认第0行（第一行）作为列名，设为 None 时无列名
                              names = None,                       # 默认使用Excel中的列名（由header决定）。提供列表将覆盖现有列名，通常与 header=None 配合使用
                              na_values = None,                   # 默认无额外空值标识。提供字符串、列表或字典（按列指定），将指定值识别为NaN
                              keep_default_na = True,             # 默认启用pandas内置空值识别（如"", "#N/A", "NULL"等）。设为False则仅识别na_values指定的空值
                              dtype = None,                       # 默认自动推断列数据类型。字典格式：{列名: 数据类型}，强制指定列的数据类型
                              converters = None,                  # 默认无列转换函数。字典格式：{列索引/列名: 函数}，在读取时对指定列应用函数
                              sep=',',                            # csv参数，默认逗号
                              encoding='utf-8',                   # csv参数，默认utf-8
                              engine_csv='c'                      # csv参数，默认c
                              ):

        skiprows        = None if skiprows == 'None'        or skiprows == None         else int(skiprows)
        usecols         = None if usecols == 'None'         or usecols == None          else usecols
        nrows           = None if nrows == 'None'           or nrows == None            else nrows
        index_col       = None if index_col == 'None'       or index_col == None        else index_col 
        header          = 0    if header == '0'             or header == 0              else int(header)
        names           = None if names == 'None'           or names == None            else names
        na_values       = None if na_values == 'None'       or na_values == None        else na_values
        keep_default_na = True if keep_default_na == 'True' or keep_default_na == True  else False
        dtype           = None if dtype == 'None'           or dtype == None            else dtype
        converters      = None if converters == 'None'      or converters == None       else converters

        try:
            file_extension = os.path.splitext(file_path)[1].lower()

            if file_extension in ['.xlsx', '.xls']:
                if file_extension == '.xlsx':
                    engine = 'openpyxl'
                elif file_extension == '.xls':
                    engine = 'xlrd'
                df = pd.read_excel(file_path,
                                sheet_name = sheet_name,             # 默认读取第一个工作表 (索引0)
                                skiprows = skiprows,                 # 默认不跳过任何行
                                usecols = usecols,                   # 默认读取所有列
                                nrows = nrows,                       # 默认读取所有行
                                index_col = index_col,               # 默认无索引列（生成RangeIndex）
                                header = header,                     # 默认第0行（第一行）作为列名，设为 None 时无列名
                                names = names,                       # 默认使用Excel中的列名（由header决定）。提供列表将覆盖现有列名，通常与 header=None 配合使用
                                na_values = na_values,               # 默认无额外空值标识。提供字符串、列表或字典（按列指定），将指定值识别为NaN
                                keep_default_na = keep_default_na,   # 默认启用pandas内置空值识别（如"", "#N/A", "NULL"等）。设为False则仅识别na_values指定的空值
                                dtype = dtype,                       # 默认自动推断列数据类型。字典格式：{列名: 数据类型}，强制指定列的数据类型
                                converters = converters,             # 默认无列转换函数。字典格式：{列索引/列名: 函数}，在读取时对指定列应用函数
                                engine = engine)

            elif file_extension in ['.csv', '.txt']:
                if file_extension == '.csv':
                    engine = engine_csv
                elif file_extension == '.txt':
                    engine = 'python'
                df = pd.read_csv(file_path,
                                sep = sep,                          # 默认逗号
                                encoding = encoding,                # 默认utf-8
                                skiprows = skiprows,                # 默认不跳过任何行
                                usecols = usecols,                  # 默认读取所有列
                                nrows = nrows,                      # 默认读取所有行
                                index_col = index_col,              # 默认无索引列（生成RangeIndex）
                                header = header,                    # 默认第0行（第一行）作为列名，设为 None 时无列名
                                names = names,                      # 默认使用Excel中的列名（由header决定）。提供列表将覆盖现有列名，通常与 header=None 配合使用
                                na_values = na_values,              # 默认无额外空值标识。提供字符串、列表或字典（按列指定），将指定值识别为NaN
                                keep_default_na = keep_default_na,  # 默认启用pandas内置空值识别（如"", "#N/A", "NULL"等）。设为False则仅识别na_values指定的空值
                                dtype = dtype,                      # 默认自动推断列数据类型。字典格式：{列名: 数据类型}，强制指定列的数据类型
                                converters = converters,            # 默认无列转换函数。字典格式：{列索引/列名: 函数}，在读取时对指定列应用函数
                                engine = engine)

            else:
                info = 'Data file format is not supported.\nPlease try importing again.\n'
                df = pd.DataFrame()
                return [False, info, df]

        except Exception as e:
            info = f'Data file reading failed.\nPlease try importing again.\n{e}\n'
            df = pd.DataFrame()
            return [False, info, df]

        info = 'Data file read successfully!\n'
        df = df.fillna('')
        return [True, info, df]

    def text_area_fill(self, text_area, result_text):

        text_area.config(state='normal')                                        # 临时启用
        text_area.insert(tk.INSERT, result_text)
        text_area.see(tk.END)                                                   # 滚动到底部
        text_area.config(state='disabled')                                      # 重新禁用

app = App()
app.root.mainloop()