# account_data_clean.py

from gui_tk import gui_tk_root

title = '科目余额表、序时账数据清洗'
geometry = '480x240+100+100'
resizable_x = False
resizable_y = False
control_frame_n = 1
control_frame_config = [
                        {'name':                'account_data_clean',
                         'widget_text':         ['导入科目余额表', '导入序时账', '输出数据文件'],
                         'function_name':       '',
                         'function_para':       ''},

                        {'text_area_hight':     20}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, resizable_x=resizable_x, resizable_y=resizable_y, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()