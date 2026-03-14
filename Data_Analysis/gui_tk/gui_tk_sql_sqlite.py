# gui_tk_sql_sqlite.py

import os
import shutil
import subprocess
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from Accounting_Audit.gui_tk import gui_tk_area_text
from Accounting_Audit.gui_tk import gui_tk_import_xlsx_xls_csv_txt
from Accounting_Audit.dataframe_tools_pd import df_review_xlsx_fun
from Accounting_Audit.dataframe_tools_pd import df_export_xlsx_fun
from sql_tools_sqlite import create_database_sqlite_fun
from sql_tools_sqlite import get_all_tables_sqlite_fun
from sql_tools_sqlite import get_table_columns_sqlite
from sql_tools_sqlite import import_dataframe_sqlite_fun
from sql_tools_sqlite import get_table_info_sqlite_fun
from sql_tools_sqlite import table_exists_sqlite
from sql_tools_sqlite import execute_query_sqlite_fun
from sql_tools_sqlite import command_sqlite_fun

gui_tk_import_xlsx_xls_csv_txt_py = gui_tk_import_xlsx_xls_csv_txt.gui_tk_import_xlsx_xls_csv_txt_class()

class gui_tk_sql_sqlite_class:

    def gui_tk_sql_sqlite_frame(self, root, control_frame_config, text_area):

        frame_result = tk.Frame(root)
        frame_result.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)

        # 连接数据库
        frame_result.frame_1 = tk.Frame(frame_result)
        frame_result.frame_1.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_1, text=control_frame_config['widget_text'][0][0], width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        frame_result.frame_1.entry_file = tk.Entry(frame_result.frame_1, state='readonly', readonlybackground='white')
        frame_result.frame_1.entry_file.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)
        tk.Button(frame_result.frame_1, text=control_frame_config['widget_text'][0][1],
                  command=lambda: self.create_select_database_sqlite_path(frame_result.frame_1.entry_file, text_area),
                  width=20).pack(side=tk.LEFT, padx=5, pady=5)

        # SQL指令区
        frame_result.frame_2 = tk.Frame(frame_result)
        frame_result.frame_2.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_result.frame_2, text=control_frame_config['widget_text'][1][0], anchor='w').pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        frame_result.frame_2.sql_command_text_area = ScrolledText(frame_result.frame_2, height=20)
        frame_result.frame_2.sql_command_text_area.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        # 第一行按钮
        frame_result.frame_3 = tk.Frame(frame_result)
        frame_result.frame_3.pack(side=tk.TOP, fill=tk.X)

        tk.Button(frame_result.frame_3, text=control_frame_config['widget_text'][2][0],
                  command=lambda: self.import_file_button(root,
                                                          frame_result.frame_1.entry_file,
                                                          text_area),
                  width=18).pack(side=tk.LEFT, padx=(3, 6), pady=5)
        
        tk.Button(frame_result.frame_3, text=control_frame_config['widget_text'][2][1],
                  command=lambda: self.show_tables_name_button(frame_result.frame_1.entry_file,
                                                               text_area),
                  width=18).pack(side=tk.LEFT, padx=6, pady=5)

        tk.Button(frame_result.frame_3, text=control_frame_config['widget_text'][2][2],
                  command=lambda: self.find_table_name_button(root,
                                                       frame_result.frame_1.entry_file,
                                                       text_area),
                  width=18).pack(side=tk.LEFT, padx=6, pady=5)

        tk.Button(frame_result.frame_3, text=control_frame_config['widget_text'][2][3],
                  command=lambda: self.show_table_info_button(root,
                                                              frame_result.frame_1.entry_file,
                                                              text_area),
                  width=18).pack(side=tk.LEFT, padx=6, pady=5)

        tk.Button(frame_result.frame_3, text=control_frame_config['widget_text'][2][4],
                  command=lambda: self.show_col_button(root,
                                                       frame_result.frame_1.entry_file,
                                                       text_area),
                  width=18).pack(side=tk.LEFT, padx=6, pady=5)

        tk.Button(frame_result.frame_3, text=control_frame_config['widget_text'][2][5],
                  command=lambda: self.backup_file_button(frame_result.frame_1.entry_file,
                                                          text_area),
                  width=18).pack(side=tk.LEFT, padx=(6, 3), pady=5)

        # 第二行按钮
        frame_result.frame_4 = tk.Frame(frame_result)
        frame_result.frame_4.pack(side=tk.TOP, fill=tk.X)
        tk.Button(frame_result.frame_4, text=control_frame_config['widget_text'][3][0],
                  command=lambda: self.review_button(frame_result.frame_1.entry_file,
                                                     frame_result.frame_2.sql_command_text_area,
                                                     text_area),
                  width=18).pack(side=tk.LEFT, padx=(3, 6), pady=5)
        
        tk.Button(frame_result.frame_4, text=control_frame_config['widget_text'][3][1],
                  command=lambda:self.export_button(frame_result.frame_1.entry_file,
                                                    frame_result.frame_2.sql_command_text_area,
                                                    text_area),
                  width=18).pack(side=tk.LEFT, padx=6, pady=5)
        
        tk.Button(frame_result.frame_4, text=control_frame_config['widget_text'][3][2],
                  command=lambda:self.command_button(frame_result.frame_1.entry_file,
                                                     frame_result.frame_2.sql_command_text_area,
                                                     text_area),
                  width=18).pack(side=tk.LEFT, padx=6, pady=5)
        
        tk.Button(frame_result.frame_4, text=control_frame_config['widget_text'][3][3],
                  command=lambda:self.save_select_button(frame_result.frame_2.sql_command_text_area,
                                                         text_area),
                  width=18).pack(side=tk.LEFT, padx=6, pady=5)
        
        tk.Button(frame_result.frame_4, text=control_frame_config['widget_text'][3][4],
                  command=lambda:self.clear_button(root,
                                                   frame_result.frame_2.sql_command_text_area,
                                                   text_area),
                  width=18).pack(side=tk.LEFT, padx=6, pady=5)
        
        tk.Button(frame_result.frame_4, text=control_frame_config['widget_text'][3][5],
                  command=lambda: self.manual_button(),
                  width=18).pack(side=tk.LEFT, padx=(6, 3), pady=5)

        # 注释快捷键
        frame_result.frame_2.sql_command_text_area.bind('<Command-/>', self.toggle_sql_comment)
        frame_result.frame_2.sql_command_text_area.bind('<Control-/>', self.toggle_sql_comment)
        return frame_result


    # 注释功能函数
    def toggle_sql_comment(self, event=None):

        text = event.widget

        try:
            start = text.index('sel.first')
            end = text.index('sel.last')
        except tk.TclError:                             # 没有选取文字，注释当前行
            start = text.index('insert linestart')
            end = text.index('insert lineend')

        start_line = int(start.split('.')[0])
        end_line = int(end.split('.')[0])

        for line_n in range(start_line, end_line+1):

            line_start = f'{line_n}.0'
            line_end = f'{line_n}.end'

            line_text = text.get(line_start, line_end)

            stripped = line_text.lstrip()
            indent_len = len(line_text) - len(stripped)

            if stripped.startswith('--'):

                new_line = line_text[:indent_len] + stripped[2:].lstrip()       # 取消注释

            else:

                new_line = line_text[:indent_len] + '-- ' + stripped            # 加上注释

            text.delete(line_start, line_end)
            text.insert(line_start,new_line)


    # 连接数据库按钮函数
    def create_select_database_sqlite_path(self, entry_file, text_area):

        fill_text = ''

        path = filedialog.asksaveasfilename(defaultextension='.sqlite',
                                            filetypes=[('SQLite Database Files', '*.sqlite'),
                                                       ('SQLite Database Files', '*.db'),
                                                       ('SQLite Database Files', '*.sqlite3'),
                                                       ('SQLite Database Files', '*.db3'),
                                                       ('All Files', '*.*')],
                                            confirmoverwrite=False)

        if path:
            fill_text += f'Selected: {path}\n'
            result_info = create_database_sqlite_fun.create_database_sqlite(path)
            if result_info[0]:
                fill_text += f'Database created/select successfully!\n'
            else:
                fill_text += 'Database creation/select failed!\n'
                fill_text += result_info[1]
        else:
            fill_text += f'File selection failed!\n'

        entry_file.config(state='normal')
        entry_file.delete(0, tk.END)
        entry_file.insert(0, path)
        entry_file.config(state='readonly')

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 导入xlsx/xls/csv/txt文件按钮
    def import_file_button(self, root, entry_file, text_area):

        fill_text = ''
        database_path = entry_file.get()

        result_df = gui_tk_import_xlsx_xls_csv_txt_py.gui_tk_import_xlsx_xls_csv_txt_frame(root)

        root.wait_window(result_df)

        df_import = gui_tk_import_xlsx_xls_csv_txt_py.result_df

        if df_import is not None:

            result_tables_name = get_all_tables_sqlite_fun.get_all_tables_sqlite(database_path)
            if result_tables_name:
                option_tables_name = result_tables_name[1]
            else:
                option_tables_name = []
            option_col = df_import.columns.tolist()

            result_sql_option = self.import_sql_option(root, option_tables_name, option_col)

            table_name = result_sql_option[0]
            if_exists = result_sql_option[1]
            index = result_sql_option[2]
            index_label = result_sql_option[3]

            if database_path and table_name:

                result_info = import_dataframe_sqlite_fun.import_dataframe_sqlite(database_path, df_import, table_name, if_exists, index, index_label)
                if result_info[0]:
                    fill_text += f'Database import successful!\n'
                else:
                    fill_text += 'Database import failed!\n'
                    fill_text += result_info[1]
            else:

                if not database_path:
                    fill_text += f'Please check that the database path is not empty!\n'
                if not table_name:
                    fill_text += f'Please check that the database table name is not empty!\n'

            gui_tk_area_text.text_area_fill(text_area, fill_text)

        else:

            fill_text += 'Failed to read file!\n'

            gui_tk_area_text.text_area_fill(text_area, fill_text)


    def import_sql_option(self, root, tables_name, option_col):

        table_name = tk.StringVar()
        if_exists = tk.StringVar()
        index = tk.StringVar()
        index_label = tk.StringVar()
        options_sql_if_exists = ['fail', 'replace', 'append']
        options_sql_index = [True, False]

        sub_win = tk.Toplevel(root)
        sub_win.title('Import Setting')
        sub_win.geometry('300x200+600+300')
        sub_win.resizable(False, False)

        # table name
        frame_1 = tk.Frame(sub_win)
        frame_1.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_1, text='table name', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=(15, 5))
        combobox_table_name = ttk.Combobox(frame_1, textvariable=table_name, values=tables_name, width=30)
        combobox_table_name.pack(side=tk.LEFT, padx=5, pady=5)
        if tables_name:
            combobox_table_name.current(0)

        # if_exists
        frame_2 = tk.Frame(sub_win)
        frame_2.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_2, text='if_exists', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        combobox_if_exists = ttk.Combobox(frame_2, textvariable=if_exists, values=options_sql_if_exists, width=30, state='readonly')
        combobox_if_exists.pack(side=tk.LEFT, padx=5, pady=5)
        combobox_if_exists.current(0)

        # index
        frame_3 = tk.Frame(sub_win)
        frame_3.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_3, text='index', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=5)
        combobox_index = ttk.Combobox(frame_3, textvariable=index, values=options_sql_index, width=30, state='readonly')
        combobox_index.pack(side=tk.LEFT, padx=5, pady=5)
        combobox_index.current(0)

        # index_label
        frame_4 = tk.Frame(sub_win)
        frame_4.pack(side=tk.TOP, fill=tk.BOTH)
        tk.Label(frame_4, text='index_label', width=10, anchor='w').pack(side=tk.LEFT, padx=5, pady=(5, 15))
        combobox_index_label = ttk.Combobox(frame_4, textvariable=index_label, values=option_col, width=30 , state='readonly')
        combobox_index_label.pack(side=tk.LEFT, padx=5, pady=5)
        if option_col:
            combobox_index_label.current(0)                                         # 默认选中第一个

        # 确认按钮函数
        def confirm():
            sub_win.destroy()
        # 确认按钮
        frame_5 = tk.Frame(sub_win)
        frame_5.pack(side=tk.TOP, fill=tk.BOTH)
        ttk.Button(frame_5, text='Confirm', command=confirm, width=15).pack(side=tk.TOP, padx=15, pady=5)

        sub_win.grab_set()
        root.wait_window(sub_win)

        return [table_name.get().strip(), if_exists.get(), index.get(), index_label.get()]


    # 查询所有工作表按钮函数
    def show_tables_name_button(self, entry_file, text_area):

        fill_text = ''

        database_path = entry_file.get()

        result_info = get_all_tables_sqlite_fun.get_all_tables_sqlite(database_path)

        if result_info[0]:

            fill_text += ', '.join(result_info[1])
            if fill_text:
                fill_text += '\n'
            else:
                fill_text += 'There is no table in the database.\n'

        else:

            fill_text += result_info[1]

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 检查表是否存在按钮函数
    def find_table_name_button(self, root, entry_file, text_area):

        fill_text = ''

        database_path = entry_file.get()

        table_name = self.enter_table(root)
        if table_name:
            result_info = table_exists_sqlite.table_exists(database_path, table_name)
            fill_text = result_info[1]
        else:
            fill_text += 'No table name entered.\n'

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 获取表信息按钮函数
    def show_table_info_button(self, root, entry_file, text_area):

        fill_text = ''

        database_path = entry_file.get()

        result_info = get_all_tables_sqlite_fun.get_all_tables_sqlite(database_path)

        if result_info[0]:
            tables_list = result_info[1]
            table_name = self.select_table(root, tables_list)
            result_text = get_table_info_sqlite_fun.get_table_info_sqlite(database_path, table_name)
            if result_text[0]:

                fill_text += f'Table {table_name} column Info:\n'
                fill_text += (f"{'CID':<4} {'NAME':<15} {'TYPE':<12} {'NOT NULL':<9} {'DEFAULT':<8} {'PK':<3}\n")
                fill_text += (f"{'-'*4} {'-'*15} {'-'*12} {'-'*9} {'-'*8} {'-'*3}\n")
                for cid, name, col_type, notnull, default, pk in result_text[1][0]:
                    fill_text += (f'{cid:<4} {name:<15} {col_type:<12} {notnull:<9} {str(default):<8} {pk:<3}\n')
                fill_text += f'\nNumber of Rows: {result_text[1][1]}\n'
            else:
                fill_text += result_text[1]
        else:
            fill_text += result_info[1]

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 获取所有列按钮函数
    def show_col_button(self, root, entry_file, text_area):

        fill_text = ''

        database_path = entry_file.get()

        result_info = get_all_tables_sqlite_fun.get_all_tables_sqlite(database_path)

        if result_info[0]:
            tables_list = result_info[1]
            table_name = self.select_table(root, tables_list)
            result_text = get_table_columns_sqlite.get_table_columns(database_path, table_name)
            if result_text[0]:
                fill_text += ', '.join(result_text[1])
                if fill_text:
                    fill_text += '\n'
                else:
                    fill_text += 'There is no column in the table.\n'
            else:
                fill_text += result_text[1]
        else:
            fill_text += result_info[1]

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 选择 table 子窗口
    def select_table(self, root, tables_list):

        sub_win = tk.Toplevel(root)
        sub_win.title('Select Table')
        sub_win.geometry('300x100+600+300')
        sub_win.resizable(False, False)
        table_select = tk.StringVar()
        combobox_table_select = ttk.Combobox(sub_win, textvariable=table_select, values=tables_list, width=50, state='readonly')
        combobox_table_select.pack(side=tk.TOP, padx=15, pady=(15, 5))
        if tables_list:
            combobox_table_select.current(0)                                                    # 默认选中第一个
        def confirm():
            sub_win.destroy()
        ttk.Button(sub_win, text='Confirm', command=confirm, width=15).pack(side=tk.TOP, padx=15, pady=(5, 15))
        sub_win.grab_set()
        root.wait_window(sub_win)
        return table_select.get()


    # 输入 table 子窗口
    def enter_table(self, root):

        table_name = tk.StringVar()
        sub_win = tk.Toplevel(root)
        sub_win.title('Enter Table Name')
        sub_win.geometry('300x100+600+300')
        sub_win.resizable(False, False)
        entry = tk.Entry(sub_win, textvariable=table_name, width=50)
        entry.pack(side=tk.TOP, padx=15, pady=(15, 5))
        entry.focus_set()                                                   # 自动获得焦点
        def confirm():
            sub_win.destroy()
        ttk.Button(sub_win, text='Confirm', command=confirm, width=15).pack(side=tk.TOP, padx=15, pady=(5, 15))
        sub_win.grab_set()
        root.wait_window(sub_win)
        return table_name.get().strip() or None


    # 备份数据库按钮函数
    def backup_file_button(self, entry_file, text_area):

        fill_text = ''

        database_path = entry_file.get()

        folder_path = os.path.dirname(database_path)
        filename = os.path.basename(database_path)
        name, ext = os.path.splitext(filename)
        target_path = os.path.join(folder_path, f'{name}_1{ext}')

        counter = 2
        while os.path.exists(target_path):
            new_filename = f'{name}_{counter}{ext}'
            target_path = os.path.join(folder_path, new_filename)
            counter += 1

        shutil.copy(database_path, target_path)

        fill_text = f'还原点建立成功，文件路径：{target_path}\n'

        gui_tk_area_text.text_area_fill(text_area, fill_text)

    # 查询并预览
    def review_button(self, entry_file, sql_command_text_area, text_area):

        fill_text = ''

        database_path = entry_file.get()

        sql_command = sql_command_text_area.get('1.0', 'end-1c')
        sql_clean = sql_command.strip()
        sql_type = sql_clean.lower().split()[0]

        if sql_type == 'select':
            result_info = execute_query_sqlite_fun.execute_query_sqlite(database_path, sql_clean)
            if result_info[0]:
                result_df = result_info[1]
                result_review = df_review_xlsx_fun.df_review_xlsx(result_df)
                subprocess.run(['open', result_review[2]])
                fill_text = f'\n查询指令：\n{sql_command}\n执行完毕！\n'
            else:            
                fill_text = f'\n查询指令：\n{sql_command}\n执行失败！\n错误信息：{str(result_info[1])}\n'
        else:
                fill_text = f'\n查询指令：\n{sql_command}\n，不是查询指令，请输入查询指令。\n'

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 查询并导出
    def export_button(self, entry_file, sql_command_text_area, text_area):

        fill_text = ''

        database_path = entry_file.get()

        sql_command = sql_command_text_area.get('1.0', 'end-1c')
        sql_clean = sql_command.strip()
        sql_type = sql_clean.lower().split()[0]

        target_path = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[('Excel Files', '*.xlsx')])

        if sql_type == 'select':
            result_info = execute_query_sqlite_fun.execute_query_sqlite(database_path, sql_clean)
            if result_info[0]:
                result_df = result_info[1]
                result_export = df_export_xlsx_fun.df_export_xlsx(result_df, target_path, index=False)
                if result_export[0]:
                    fill_text = f'\n查询指令：\n{sql_command}\n执行完毕！\n导出文件路径：{target_path}\n'
                    subprocess.run(['open', target_path])
            else:
                fill_text = f'\n查询指令：\n{sql_command}\n执行失败！\n错误信息：{str(result_info[1])}\n'
        else:
                fill_text = f'\n查询指令：\n{sql_command}\n，不是查询指令，请输入查询指令。\n'

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 执行SQL指令按钮函数
    def command_button(self, entry_file, sql_command_text_area, text_area):

        fill_text = ''

        database_path = entry_file.get()

        sql_command = sql_command_text_area.get('1.0', 'end-1c')
        sql_clean = sql_command.strip()
        sql_type = sql_clean.lower().split()[0]

        if sql_type != 'select':
            self.backup_file_button(entry_file, text_area)

        fill_text += command_sqlite_fun.command_sqlite(database_path, sql_type, sql_clean)

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # 保存查询
    def save_select_button(self, sql_command_text_area, text_area):

        fill_text = ''

        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt'),('All Files', '*.*')])
        if file_path:
            with open(file_path, 'w') as output_file:
                output_file.write(sql_command_text_area.get('1.0',tk.END+'-1c'))
            fill_text += f'Save path: {file_path}'

        gui_tk_area_text.text_area_fill(text_area, fill_text)


    # ScrolledText内容
    def clear_button(self, root, sql_command_text_area, text_area):

        result_info = self.select_clear(root)

        if result_info[0]:
            sql_command_text_area.delete('1.0', 'end')
        if result_info[1]:
            gui_tk_area_text.text_area_clear(text_area)


    # 选择 table 子窗口
    def select_clear(self, root):

        sub_win = tk.Toplevel(root)
        sub_win.title('Clear Text')
        sub_win.geometry('300x150+600+300')
        sub_win.resizable(False, False)
        sql_command_select = tk.IntVar(value=1)
        text_area_select = tk.IntVar(value=0)
        checkbutton_sql_command_select = tk.Checkbutton(sub_win, text='SQL Command Text Area', variable=sql_command_select)
        checkbutton_sql_command_select.pack(side=tk.TOP, padx=15, pady=(20, 5))
        checkbutton_text_area_select = tk.Checkbutton(sub_win, text='Operation Log', variable=text_area_select)
        checkbutton_text_area_select.pack(side=tk.TOP, padx=15, pady=(5, 10))
        def confirm():
            sub_win.destroy()
        ttk.Button(sub_win, text='Confirm', command=confirm, width=15).pack(side=tk.TOP, padx=15, pady=(5, 15))
        sub_win.grab_set()
        root.wait_window(sub_win)
        return [sql_command_select.get(), text_area_select.get()]


    # SQL指令帮助按钮函数
    def manual_button(self):

        sub_win = tk.Toplevel()
        sub_win.title('SQLite 指令说明')
        sub_win.geometry('780x600+100+100')

        text = ScrolledText(sub_win, wrap=tk.WORD, font=("Arial", 12))
        text.pack(expand=True, fill=tk.BOTH)

        params_text = """
    SQLite 指令说明

    """
        text.insert(tk.END, params_text)
        text.config(state="disabled")