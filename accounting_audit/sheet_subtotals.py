# sheet_subtotals.py

from gui_tk import gui_tk_root

title = '分类汇总表格'
geometry = '720x480+50+50'
resizable_x = False
resizable_y = False
control_frame_n = 1
control_frame_config = [
                        {'name':                'sheet_subtotals',
                         'widget_text':         ['File Path', '选择工作表', '选择行目录', '选择列标题', '选择数值列', '导入', '生成'],
                         'function_name':       '',
                         'function_para':       ''},

                        {'text_area_hight':     21}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, resizable_x=resizable_x, resizable_y=resizable_y, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()