# sheet_regex.py

from gui_tk import gui_tk_root

title = '使用正则表达式筛选'
geometry = '1280x720+50+50'
resizable_x = False
resizable_y = False
control_frame_n = 1
control_frame_config = [
                        {'name':                'sheet_regex',
                         'widget_text':         ['File Path', '选择工作表', '选择筛选列', '选择标识符', '正则表达式（Python环境）', '正则表达式指令区',
                                                 '选择文件', '导入数据', '预览数据', '添加regex', '[]', 'AND', 'OR', '执行筛选', '导出文件'],
                         'function_name':       '',
                         'function_para':       ''},

                        {'text_area_hight':     21}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, resizable_x=resizable_x, resizable_y=resizable_y, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()