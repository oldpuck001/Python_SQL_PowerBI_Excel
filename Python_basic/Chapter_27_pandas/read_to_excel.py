# read_to_excel_py.py

import os
import pandas as pd

# read_excel

file_path_1 = 'a.xlsx'
file_path_2 = 'stores.xlsx'
# 也可以是URL地址

# 获取扩展名
file_extension = os.path.splitext(file_path_1)[1].lower()

# sheet_name 工作表名称
sheet_name = 'a'

# skiprows 从第几行开始读取数据，第一行是0
skiprows = 0

# usecols 设置读取的列区间，首尾都包含
usecols = 'B:F'

# engine 设置使用的引擎

# 使用pd.read_excel讀取表格文件
if file_extension == '.xlsx':
    df_1 = pd.read_excel(file_path_1, engine='openpyxl')
    df_2 = pd.read_excel(file_path_1, sheet_name=sheet_name, skiprows=skiprows, usecols=usecols, engine='openpyxl')
elif file_extension == '.xls':
    df_1 = pd.read_excel(file_path_1, engine='xlrd')
    df_2 = pd.read_excel(file_path_1, sheet_name=sheet_name, skiprows=skiprows, usecols=usecols, engine='xlrd')

print(df_1)
print(df_2)

# pd.read_excel() 函数的 sheet_name 参数可以接受几种不同的值：
# 默认值：如果不指定sheet_name，默认读取文件中的第一个工作表
# 指定工作表名称：通过工作表的名称来指定读取哪个工作表。例如：sheet_name='工作表1'
# 指定工作表索引：工作表在Excel文件中是按顺序排列的，您可以通过索引（从0开始计数）来指定要读取的工作表。例如：sheet_name=2 读取第三个工作表等
# 读取多个工作表：如果想一次性读取多个工作表，可以将工作表的名称或索引放在一个列表中作为sheet_name的值。
# 例如：sheet_name=['工作表1', '工作表2'] 这将返回一个字典，其中每个键是工作表的名称，每个值是对应的DataFrame
# 读取所有工作表：通过将 sheet_name=None 传递给 pd.read_excel() 函数，可以读取Excel文件中的所有工作表
# 这同样会返回一个字典，其中包含文件中每个工作表的DataFrame

# 导入时通过自定义函数或lambda函数修改数据
def fix_missing(x):
    return False if x in ['', 'MISSING'] else x

df_3 = pd.read_excel(file_path_2, sheet_name='Sheet1', skiprows=1, usecols='B:F',converters={'Flagship': fix_missing})

print(df_3)
print(df_3.info())

# 使用工作表名称列表或列表的切片導入多個工作表，返回的是以DataFrame为值、工作表名称为键的一个字典
# usecols也可以接受列名的列表
sheets_1 = pd.read_excel(file_path_2, sheet_name=['Sheet1', 'Sheet2'], skiprows=1, usecols=['Store', 'Employees'])
print(sheets_1['Sheet1'])
print(sheets_1['Sheet2'])

# 導入所有工作表
sheets_2 = pd.read_excel(file_path_2, sheet_name=None, skiprows=1, usecols=['Store', 'Employees'])
print(sheets_2['Sheet1'])
print(sheets_2['Sheet2'])
print(sheets_2['Sheet3'])

# 如果源文件没有列标题，则可设置参数 header=None 并通过 names 参数提供对应的列名
# 如果工作表中包含了表头（即每一列的名称），pd.read_excel()默认会把第一行作为表头（列名）。
# 如果数据从文件的第一行就开始，而没有列名，您可以通过设置 header=None 来告诉pandas不要将第一行作为表头
df_4 = pd.read_excel(file_path_2, sheet_name=0, skiprows=2, skipfooter=3, usecols='B:C,F', header=None, names=['Branch', 'Employee_Count', 'Is_Flagship'])
print(df_4)

# 只将含有 MISSING 的单元格解释为 NaN，除此之外的情况什么都不做
df_5 = pd.read_excel(file_path_2, sheet_name='Sheet1', skiprows=1, usecols='B,C,F', skipfooter=2, na_values="MISSING", keep_default_na=False)
print(df_5)

# 通过 ExcelFile 访问所有工作表的名称
sheets_3 = pd.ExcelFile(file_path_2)
print(sheets_3.sheet_names)


# to_excel

file_path_3 = 'b.xlsx'
file_path_4 = 'c.xlsx'

data=[['2020-01-01 10:13:00', 2.222, 1, True],
      ['2020-01-02 00:00:00', '', 2, False],
      ['2020-01-02 00:00:00', '', 3, True]]

df = pd.DataFrame(data=data, columns=['Dates', 'Floats', 'Integers', 'Booleans'])
df.index.name="index"

# engine（引擎）默認使用XlsxWriter来写文件
df.to_excel(file_path_3, sheet_name="Output", startrow=1, startcol=1, index=True, header=True, engine='openpyxl')

# 在Pandas中，當使用to_excel方法將DataFrame寫入Excel文件時，index參數決定了是否將DataFrame的索引(index)也寫入Excel。
# index = True（這是默認值）: DataFrame的索引將被一同寫入Excel。這意味著當打開生成的Excel文件時，除了數據列之外，您還會看到一個額外的列，該列表示DataFrame的索引
# index = False: DataFrame的索引不會被寫入Excel。只有數據列本身會被寫入


# to_excel結合ExcelWriter類與With上下文管理器，可以向一個工作表中寫入多個DataFrame，或者向一個工作簿文件中寫入多個工作表
with pd.ExcelWriter(file_path_4) as writer:
    df.to_excel(writer, sheet_name="Sheet1", startrow=1, startcol=1)
    df.to_excel(writer, sheet_name="Sheet1", startrow=10, startcol=1)
    df.to_excel(writer, sheet_name="Sheet2")