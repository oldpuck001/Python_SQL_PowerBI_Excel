# DataFrame_create.py

# pd.DataFrame
# df.info()，info 方可以得 DataFrame 的本，的是数据数和的数据型

import pandas as pd

# 创建一个空白的 DataFrame
empty_df = pd.DataFrame()
print('创建一个空白的 DataFrame')
print(empty_df)
print(empty_df.info())

# 创建带有列名的空白 DataFrame
columns = ['Column1', 'Column2', 'Column3']
empty_df_with_columns = pd.DataFrame(columns=columns)
print('创建带有列名的空白 DataFrame')
print(empty_df_with_columns)
print(empty_df_with_columns.info())

index = [1001, 1000, 1002, 1003]
columns_list = ['name', 'No.', 'country', 'score', 'job']
# 使用列表構造DataFrame
data_list = [['Mike', 1, 'Thailand', 80, 'teacher'],
             ['Yang', 2, 'China', 77, 'student'],
             ['Tom', 3, 'England', 85, 'student'],
             ['Losa', 4, 'Japan', 90, 'accounting']]
df_list = pd.DataFrame(data=data_list, columns=columns_list, index=index)
print('使用列表構造DataFrame')
print(df_list)
print(df_list.info())

# 使用字典構造DataFrame
data_dict = {'name': ['Mike', 'Yang', 'Tom', 'Losa'],
             'No.': [1, 2, 3, 4],
             'country': ['Thailand', 'China', 'England', 'Japan'],
             'score': [80, 77, 85, 90],
             'job': ['teacher', 'student', 'student', 'accounting']
            }
df_dict = pd.DataFrame(data=data_dict, index=index)
print('使用字典構造DataFrame')
print(df_dict)
print(df_dict.info())