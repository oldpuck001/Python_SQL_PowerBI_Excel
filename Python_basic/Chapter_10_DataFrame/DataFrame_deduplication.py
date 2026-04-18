# DataFrame_deduplication.py

# df.drop_duplicates
# df['country'].is_unique
# df.index.is_unique

import pandas as pd

columns = ['name', 'No.', 'country', 'score', 'job']

index=[101, 100, 102, 103, 104, 105, 106, 107, 108, 109]

data = [['Mike', 1, 'Thailand', 80, 'teacher'],
        ['Yang', 2, 'China', 77, 'student'],
        ['Tom', 3, 'England', 85, 'student'],
        ['Losa', 4, 'Japan', 90, 'accounting'],
        ['Tim', 6, 'America', 87, 'student'],
        ['Zhang', 5, 'China', 73, 'student'],
        ['Jack', 9, 'India', 85, 'student'],
        ['Wang', 8, 'China', 89, 'student'],
        ['Chang', 10, 'Thailand', 94, 'accounting'],
        ['Lucy', 7, 'Japan', 91, 'employee']
        ]

df = pd.DataFrame(data, columns=columns, index=index)
print(df)

# drop_duplicates方法清理重複的行，默認情況下，第一次出現的數據會得以保留
print('drop_duplicates方法清理重複的行，默認情況下，第一次出現的數據會得以保留')
df_drop_duplicates = df.drop_duplicates(['country', 'job'])
print(df_drop_duplicates)

# is_unique方法確認某一列是否包含重複數據
print('is_unique方法確認某一列是否包含重複數據')
print(df['country'].is_unique)
print(df['name'].is_unique)

# unique方法可以獲得去重後的值
print('unique方法可以獲得去重後的值')
print(df['country'].unique())

# 如果想對索引進行此類操作，可以將df['country']換成df.index
print('如果想對索引進行此類操作，可以將df[\'country\']換成df.index')

# duplicated方法找出哪些行是重複的，返回值是一個布爾Series
print('duplicated方法找出哪些行是重複的，返回值是一個布爾Series')
# 默認情況下，keep=first，只有重複的行會被標記為True，即第一次出現時不會被標記為True
print(df['country'].duplicated())
print(df.loc[df['country'].duplicated(), :])
# 將參數設置為keep=False時，會標記所有重複的行，包括第一次出現時
print(df['country'].duplicated(keep=False))
print(df.loc[df['country'].duplicated(keep=False), :])