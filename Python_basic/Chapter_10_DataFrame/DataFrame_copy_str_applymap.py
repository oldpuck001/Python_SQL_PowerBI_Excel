# DataFrame_str.py

# df.copy()
# df['name'].str.strip()
# df['name'].str.startswith('J')
# df.applymap

import pandas as pd

columns = ['name', 'No.', 'country', 'score', 'job']

index=[101, 100, 102, 103, 104, 105, 106, 107, 108, 109]

data = [['  Mike', 1, 'Thailand', 8000, 'teacher'],
        ['Yang  ', 2, 'China', 7787, 'student'],
        [' Tom  ', 3, 'England', 8545, 'student'],
        ['  Losa ', 4, 'Japan', 9045.76, 'accounting'],
        [' Tim  ', 6, 'America', 1.87, 'student'],
        ['Zhang ', 5, 'China', 73.4, 'student'],
        [' Jack  ', 9, 'India', 850.89, 'student'],
        ['Wang  ', 8, 'China', 24899.3, 'student'],
        [' Chang', 10, 'Thailand', 940.04, 'accounting'],
        ['   Lucy ', 7, 'Japan', 91, 'employee']
        ]

df = pd.DataFrame(data, columns=columns, index=index)

# 要在含有文本字符串的列上执行相关操作，需要使用str属性，str属性可以访问Python的字符串方法
df_cleaned = df.copy()
df_cleaned['name'] = df_cleaned['name'].str.strip()
print(df_cleaned)

# 找出以J开头的名字
print(df_cleaned['name'].str.startswith('J'))

# applymap 调用自定义函数
def format_string(x):
    if isinstance(x, (int, float)):
        return f'{x:,.2f}'
    else:
        return x
print(df.applymap(format_string))

# 方法             適用對象                  說明
# map()            Series                  適合對單欄的元素逐一處理
# apply()          Series或DataFrame       針對整列或整欄處理（支援lambda或自定函數）
# applymap()       DataFrame               對DataFrame中每個元素應用函數

# 使用lambda表達式的版本
print(df.applymap(lambda x: f'{x:,.2f}' if isinstance(x, (int, float)) else x))