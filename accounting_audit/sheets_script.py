# sheets_script.py

from gui_tk import gui_tk_root

title = '电子表格拼接'
geometry = '1280x720+50+50'
resizable_x = False
resizable_y = False
control_frame_n = 1
control_frame_config = [
                        {'name':              'sheets_script',
                         'widget_text':       [12, '添加', '删除', '导出'],
                         'function_name':     '',
                         'function_para':     ''},

                        {'text_area_hight':     16}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, resizable_x=resizable_x, resizable_y=resizable_y, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()