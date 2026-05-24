# fill_info_sheet.py

from gui_tk import gui_tk_root

title = '生成基本情况表'
geometry = '360x240+100+100'
resizable_x = False
resizable_y = False
control_frame_n = 1
control_frame_config = [
                        {'name':                'fill_info_sheet',
                         'widget_text':         ['读取企查查文件（Excel操作版）', '生成基本情况表'],
                         'function_name':       '',
                         'function_para':       ''},

                        {'text_area_hight':     20}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, resizable_x=resizable_x, resizable_y=resizable_y, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()