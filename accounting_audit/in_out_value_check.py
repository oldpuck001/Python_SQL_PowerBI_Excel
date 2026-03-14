# in_out_value_check.py

from gui_tk import gui_tk_root

title = 'In/Out value check'
geometry = '1280x720+50+50'
resizable_x = False
resizable_y = False
control_frame_n = 1
control_frame_config = [
                        {'name':                'in_out_value_check',
                         'widget_text':         [['正向', '反向'], ['双列模式', '+/-单列模式', '标识列单列模式'],
                                                 'File 1 Path', 'Sheet 1 Name', 'Sheet 1 Time Series', 'Sheet 1 Item', 'Sheet 1 In/Out Mode',
                                                 'Sheet 1 In Col', 'Sheet 1 Out Col', 'Reserved', 'Reserved',
                                                 'Sheet 1 In/Out Col', 'Sheet 1 In Label', 'Sheet 1 Out Label', 'Sheet 1 In/Out Value',
                                                 'File 2 Path', 'Sheet 2 Name', 'Sheet 2 Time Series', 'Sheet 2 Item', 'Sheet 2 In/Out Mode',
                                                 'Sheet 2 In Col', 'Sheet 2 Out Col', 'Reserved', 'Reserved',
                                                 'Sheet 2 In/Out Col', 'Sheet 2 In Label', 'Sheet 2 Out Label', 'Sheet 2 In/Out Value',
                                                 'Import Sheet 1', 'Review Sheet 1', 'Sheet 1 Label', 'Import Sheet 2', 'Review Sheet 2', 'Sheet 2 Label', 'Comparison Data'],
                         'function_name':       '',
                         'function_para':       ''},

                        {'text_area_hight':     25}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, resizable_x=resizable_x, resizable_y=resizable_y, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()