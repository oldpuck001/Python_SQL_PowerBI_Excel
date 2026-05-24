# DataFrame_column_row.py

# df.shape
# df.columns
# df.columns.name
# df.rename
# df.drop
# df.sort_values
# df.transpose

# 調用 DataFrame 的方法時，返回的是副本，所以原來的 DataFrame 沒有任何變化.
# 可以使用 df = df.reset_index() 的方法將返回值賦給原來的變量。

import pandas as pd

index = [1001, 1000, 1002, 1003]

data = {'name': ['Mike', 'Yang', 'Tom', 'Losa'],
        'No.': [1, 2, 3, 4],
        'country': ['Thailand', 'China', 'England', 'Japan'],
        'score': [80, 77, 85, 90],
        'job': ['teacher', 'student', 'student', 'accounting']
       }

df = pd.DataFrame(data=data, index=index)
print(df)

# shape方法獲取行與列的數量，返回 (行數, 列數) 的元組
print('獲取行與列的數量')
print(df.shape)

# 獲取列的信息，構造DataFrame數據結構時，如過沒有提供列明，將會從0開始的數字為列編號
print('獲取列的信息')
print(df.columns)

# 給索引列命名
print('給索引列命名')
df.columns.name = 'properties'
print(df)

# rename給列重命名
print('rename給列重命名')
df_rename = df.rename(columns={'name': 'First Name', 'No.': 'num'})
print(df_rename)

# drop刪除列與刪除行
print('drop刪除列與刪除行')
df_drop = df.drop(columns=["name", "country"], index=[1000, 1003])
print(df_drop)

# 按一列排序
print('sort_values按一列排序')
df_sort_values_one = df.sort_values('score')
print(df_sort_values_one)

# 按多列排序
print('sort_values按多列排序')
df_sort_values_more = df.sort_values(['job', 'score'])
print(df_sort_values_more)

# transpose 方法將 DataFrame 數據結構轉置
# df.transpose() 的縮寫
print('transpose 方法將 DataFrame 數據結構轉置')
df_transpose = df.T
print(df_transpose)