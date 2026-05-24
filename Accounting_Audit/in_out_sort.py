# in_out_sort.py

from gui_tk import gui_tk_root

title = 'In/Out Value Sort'
geometry = '1280x720+50+50'
resizable_x = False
resizable_y = False
control_frame_n = 1
control_frame_config = [
                        {'name':                'in_out_sort',
                         'widget_text':         ['File Path', '选择工作表', '选择In/Out标识列', '选择In标识', '选择Out标识', '选择2级分类列',
                                                 '选择3级分类列', '选择数值列', 'In优先项目', 'Out优先项目', 'Import', 'Export'],
                         'function_name':       '',
                         'function_para':       ''},

                        {'text_area_hight':     21}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, resizable_x=resizable_x, resizable_y=resizable_y, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()