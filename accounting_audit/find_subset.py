# find_subset.py

from gui_tk import gui_tk_root

title = '凑数工具'
geometry = '720x480+50+50'
resizable_x = False
resizable_y = False
control_frame_n = 1
control_frame_config = [
                        {'name':                'find_subset',
                         'widget_text':         ['File Path', '目标值', '选择工作表', '选择项目列', '选择数值列', '选择文件', '导入数据', '数据预览', '开始凑数'],
                         'function_name':       '',
                         'function_para':       ''},

                        {'text_area_hight':     21}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, resizable_x=resizable_x, resizable_y=resizable_y, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()