# DataFrame_index.py

# df.index
# df.index.name
# df.reset_index
# df.set_index
# df.reindex
# df.sort_index

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

# index是DataFrame數據結構的索引，和数据库的不同，DataFrame 的索引可以重复
print('索引')
print(df.index)

# 給索引命名
print('給索引命名索引')
df.index.name = 'user_id'
print(df)

# reset_index，可以將索引變成普通的列
print('reset_index，可以將索引變成普通的列')
df_reset_index = df.reset_index()
print(df_reset_index)

# set_index，可以將一個普通列設置成一個新的索引，索引可以是多級的
print('set_index，可以將一個普通列設置成一個新的索引，索引可以是多級的')
df_set_index_1 = df.reset_index().set_index('name')
print(df_set_index_1)
df_set_index_2 = df.reset_index().set_index(['job', 'country'])
print(df_set_index_2)
df_set_index_3 = df_set_index_2.reset_index(level=0)
print(df_set_index_3)

# 使用鏈式方法調用（method chaining），執行順序從左到右，省去了寫中間值
print('使用鏈式方法調用（method chaining），執行順序從左到右，省去了寫中間值')
df_method_chaining = df.reset_index().set_index('No.')
print(df_method_chaining)

# reindex 更新索引，這個方法會匹配所有新索引的行，無法匹配的行的索引會變為空值NaN
print('reindex 更新索引，這個方法會匹配所有新索引的行，無法匹配的行的索引會變為空值NaN')
new_index = [999, 1000, 1001, 1004]
df_new_index = df.reindex(new_index)
print(df_new_index)

# sort_index 按索引排序
print('sort_index 按索引排序')
df_sort_index = df.sort_index()
print(df_sort_index)