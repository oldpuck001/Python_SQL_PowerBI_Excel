# create_project_floder.py

from gui_tk import gui_tk_root

title = '创建项目文件夹'
geometry = '640x480+100+100'
resizable_x = False
resizable_y = False
control_frame_n = 1
control_frame_config = [
                        {'name':                'create_project_floder',
                         'widget_text':         ['Folder Structure', 'Create Project Floder'],
                         'function_name':       '',
                         'function_para':       ''},

                        {'text_area_hight':     11}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, resizable_x=resizable_x, resizable_y=resizable_y, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()