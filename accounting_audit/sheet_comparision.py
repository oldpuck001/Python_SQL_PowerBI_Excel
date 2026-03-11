# sheet_comparision.py

from gui_tk import gui_tk_root

title = '电子表格对比'
geometry = '720x480+50+50'
resizable_x = False
resizable_y = False
control_frame_n = 1
control_frame_config = [
                        {'name':                'sheet_comparision',
                         'widget_text':         ['File Path 1', '选择工作表', 'File Path 2', '选择工作表', '选择文件 1', '选择文件 2', '开始对比'],
                         'function_name':       '',
                         'function_para':       ''},

                        {'text_area_hight':     18}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, resizable_x=resizable_x, resizable_y=resizable_y, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()