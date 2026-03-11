# sql_sqlite.py

from Accounting_Audit.gui_tk import gui_tk_root

title = 'SQLite Database'
geometry = '1280x720+50+50'
resizable_x = False
resizable_y = False

control_frame_n = 1
control_frame_config = [
                        {'name':                 'SQLite Database',
                         'widget_text':          [['SQLite File Path', '创建/选择SQLite数据库'],
                                                  ['SQL Command'],
                                                  ['Import xlsx/xls/csv/txt', 'Show Tables', 'Check Table', 'Show Table Info', 'Show Columns', 'Backup'],
                                                  ['Select Review', 'Select Export', 'SQL Command', 'Save Select', 'Clear', 'Help Text'],
                                                 ],
                         'function_name':        '',
                         'function_para':        ''},

                        {'text_area_hight':     19}
                       ]

app = gui_tk_root.App(title=title, geometry=geometry, resizable_x = resizable_x, resizable_y = resizable_x,
                      control_frame_n=control_frame_n, control_frame_config=control_frame_config)
app.root.mainloop()