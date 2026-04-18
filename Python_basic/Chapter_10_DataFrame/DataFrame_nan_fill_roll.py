# DataFrame_nan_fill_roll.py

# df.dropna
# df.isna
# df.fillna
# df.ffill
# df.rolling

import pandas as pd

columns = ['name', 'No.', 'country', 'score', 'job']

index=[101, 100, 102, 103, 104, 105, 106, 107, 108, 109]

data = [['Mike', 1, 'Thailand', 80, 'teacher'],
        ['Yang', 2, 'China', 77, 'student'],
        ['Tom', 3, 'England', 85, 'student'],
        ['Losa', 4, "Japan", 90, 'accounting'],
        ['Tim', 6, None, 87, 'student'],
        ['Zhang', 5, 'China', 73, 'student'],
        ['Jack', 9, 'India', None, 'student'],
        ['Wang', 8, 'China', 89, 'student'],
        ['Chang', 10, "Thailand", 94, 'accounting'],
        [None, None, None, None, None]
        ]

df = pd.DataFrame(data, columns=columns, index=index)

# 浮点数标准中的缺失数据：NaN（Not-a-Number 非数字）
# 时间戳中的缺失数据：pd.NaT
# 文本中的缺失数据：None

# 移除所有包含缺失数据的行
print('移除所有包含缺失数据的行')
df_dropna_1 = df.dropna()
print(df_dropna_1)

# 只移除所有值都缺失了的行，使用how参数
print('只移除所有值都缺失了的行，使用how参数')
df_dropna_2 = df.dropna(how="all")
print(df_dropna_2)

# 要獲取一个反映对应位置上是否是NaN的布尔DataFrame或Series，可以使用isna方法
print('要獲取一个反映对应位置上是否是NaN的布尔DataFrame或Series，可以使用isna方法')
df_isna = df.isna()
print(df_isna)

# 使用fillna来填补缺失的值
# 例如，将数据点数量列中的NaN替换为平均分（mean描述性统计量）
print('使用fillna来填补缺失的值')
df_fillna = df.fillna({'score': df['score'].mean()})
print(df_fillna)

# ffill向前填充
print('ffill向前填充')
df_ffill_1 = df.ffill()
print(df_ffill_1)
df_ffill_2 = df.copy()
df_ffill_2['country'] = df_ffill_2['country'].ffill()
print(df_ffill_2)

# rolling方法会接受观测数量作为参数。可以在rolling后面链式调用所需的统计量方法
# 对于移动平均值来说就是在rolling后面调用mean
print('rolling方法会接受观测数量作为参数。')
df_ffill_1.loc[:, '3row average'] = df_ffill_1['score'].rolling(3).mean()
print(df_ffill_1)