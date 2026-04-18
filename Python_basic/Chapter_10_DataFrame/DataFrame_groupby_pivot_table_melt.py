# DataFrame_groupby_pivot_table_melt.py

# df.groupby(['job']).mean()
# df.groupby(['job']).agg()
# pd.pivot_table
# pd.melt

import pandas as pd

numbers = pd.DataFrame(data={'col 1': [250.1, 99.4],
                             'col 2': [350.4, 129.7],
                             'col 3': [200.7, 100.6]})

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

# groupby方法
print('groupby方法分組數據')

# groupby方法分組數據，使用一個列的值分組數據
print(df.loc[:, ['No.', 'score', 'job']].groupby(['job']).mean())

# groupby 方法分組數據，使用多個列的值分組數據
print(df.loc[:, ['No.', 'country', 'score', 'job']].groupby(['job', 'country']).mean())

# groupby 方法分組數據，結合agg方法使用自定義函數
print(df.loc[:, ['No.', 'score', 'job']].groupby(['job']).agg(lambda x: x.max() - x.min()))


# pivot_table函数的功能類似於Excel的数据透视表
# 第一个参数是DataFrame數據，index和columns分别指定了哪一列会成为数据透视表的行标签和列标签
# values会通过aggfunc（以字符串或者NumPy ufunc的形式提供）被聚合到结果DataFrame中的数据部分
# 最后，margins对应的是Excel中的Grand Total，如果省略margins和margins_name，则结果中不会出现Total列
print('pivot_table方法（類似於Excel的数据透视表）')
df_pivot = pd.pivot_table(df, index='job', columns='country', values='score', aggfunc='sum', margins=True, margins_name='Total')
print(df_pivot)


# melt函數
print('melt函數')
# melt函數将列标题转换成列的值，如果想将数据处理成数据库要求的格式，可以使用melt
# pd.melt(frame, id_vars=None, value_vars=None, var_name=None, value_name='value')
# frame         DataFrame本身
# id_vars       要保留的識別變數（識別列），這些欄位不會展開，並會在長格式中重複出現
# value_vars    需要被展開的欄位名稱，如果未指定，則會展開除了id_vars之外的所有欄位
# var_name      在長格式中代表展開的欄位名稱（變數名列）的名稱，默認為 variable
# value_name    展開後數值所在欄位的名稱，默認為value
df_melt_1 = pd.melt(df, id_vars=['country'], value_vars=['No.', 'score'], var_name='variable', value_name='new_score')
print(df_melt_1)

# 可以把melt看作是pivot_table的反函数
df_melt_2 = pd.melt(df_pivot.iloc[:-1,:-1].reset_index(), id_vars='job', value_vars=['China', 'Thailand'], value_name='score')
print(df_melt_2)