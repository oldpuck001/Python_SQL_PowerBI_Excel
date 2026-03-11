# in_out_value_check.py

from Accounting_Audit.gui_tk import gui_tk_root

title = 'In/Out value check'
geometry = '1280x720+50+50'
control_frame_n = 1
control_frame_config = [
                        {'name':                'in_out_value_check',
                         'widget_text':         ['Import Sheet 1', 'Review Sheet 1', 'Sheet 1 Label', 'Import Sheet 2', 'Review Sheet 2', 'Sheet 2 Label', 'Comparison Data'],
                         'function_name':       '',
                         'function_para':       ''},

                        {'text_area_hight':     25}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()