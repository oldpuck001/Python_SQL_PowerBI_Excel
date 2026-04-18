# DataFrame_value.py

# 設置值
# df.replace
# 添加新列

import pandas as pd

columns = ['name', 'No.', 'country', 'score', 'job']

index = [101, 100, 102, 103, 104, 105, 106, 107, 108, 109]

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

# 通過標籤設置值
print('通過標籤設置值')
df.loc[103, 'name'] = 'LOSA'
print(df)
df.loc[[105, 106], 'name'] = ['ZHANG', 'JACK']
print(df)

# 通過位置設置值
print('通過位置設置值')
df.iloc[4, 0] = 'TIM'
print(df)

# 通過布爾索引設置數據
print('通過布爾索引設置數據')
tf = (df['No.'] < 3) | (df['job'] == 'student')
df.loc[tf, 'name'] = 'xxx'
print(df)

numbers = pd.DataFrame(data={'col 1': [250.1, 99.4],
                             'col 2': [350.4, 129.7],
                             'col 3': [200.7, 100.6]})
numbers[numbers < 200] = 0
print(numbers)

# replace方法將DataFrame中的某個值，替換為另一個值
print('replace方法將DataFrame中的某個值，替換為另一個值')
df_replace_1 = df.replace('America', 'USA')
print(df_replace_1)

# replace方法只在某一列进行替换的语句
print('eplace方法只在某一列进行替换的语句')
df_replace_2 = df.replace({'job': {'employee': 'worker'}})
print(df_replace_2)

# 添加新列
print('添加新列')
df.loc[:, 'age'] = 0
df.loc[:, 'ID'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(df)

# 添加新列的同时进行运算
print('添加新列的同时进行运算')
df.loc[:, 'ID'] = 10 + df['ID']
print(df)