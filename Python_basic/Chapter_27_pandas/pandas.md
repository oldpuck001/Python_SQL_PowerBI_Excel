pandas.md

要使用Python處理電子表格，最常用的庫是pandas，並且結合openpyxl或xlrd使用。

pandas是用于数据分析和处理的Python库。
openpyxl是用于读写xlsx/xlsm/xltx/xltm文件的库，它也是pandas使用的默认处理Excel文件的引擎。

导入和导出DataFrame
数据格式/系统       导入：pandas（pd）函数      导出：DataFrame（df）方法
CSV文件            pd.read_csv               df.to_csv
JSON              pd.read_json              df.to_json
HTML              pd.read_html              df.to_html
剪贴板             pd.read_clipboard         df.to_clipboard
Excel文件          pd.read_excel             df.to_excel
SQL数据库          pd.read_sql               df.to_sql


部分read_excel参数

sheet_name
除了提供工作表名称，也可以提供工作表的索引（从0开始），比如 sheet_name=0如果将参数设置为sheet_name=None，则pandas会读取整个工作簿并以 {"sheetname":df} 的形式返回一个字典。要读取指定的多张工作表，可以传递一个工作表名称或索引的列表

skiprows
跳过指定数量的行

usecols
如果Excel文件包含列标题，就通过传递列标题列表选择指定列，比如 ["Store", "Employees"] 另外，也可以传递列的索引列表，比如 [1, 2] 或者Excel列名的字符串（不是列表）也可以包含列区域，比如 "B:D, G" 还可以传递一个函数：如果想只包含以Manager开始的列，则可以将参数设置为usecols=lambda x: x.startwith("Manager")

nrows
想要读取的行数

index_col
指定将作为索引的列，接受列名或列索引，比如index_col=0，如果提供了包含多列的列表，则会创建层次索引

header
如果设置为header=None，而未通过names参数提供列名，则会使用默认的整数列标题。如果提供的是索引的列表，则会创建层次列标题

names
提供列名称列表

na_values
在默认情况下，pandas会将这些值解释为NaN：空单元格、#NA、NA、null、#N/A、N/A、NaN、n/a、-NaN、1.#IND、nan、#N/A、N/A、-1.#QNAN、-nan、NULL、-1.#IND、<NA>和1.#QNAN。如果需要往这些值中添加一个或多个值，则可以通过na_values来提供

keep_default_na
如果希望忽略pandas默认解释为NaN的值，则可以将参数设置为keep_default_na=False

convert_float
在默认情况下，Excel会在内部将所有数字都以浮点型保存，pandas会将带有无意义的小数点的数字转换为整数。如果想改变这种行为，则可以将参数设置为convert_float=False（可能会获得少许性能提升）

converters
可以为各列提供一个函数来转换其中的值。如果要将某一列中的文本转换为大写，则可以将参数设置为：converters={"column_name": lambda x: x.upper()}