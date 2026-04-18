# DataFrame_concat_join_merge.py

# pd.concat
# df.join
# df.merge

import pandas as pd

columns = ['name', 'No.', 'country', 'score']

index = [101, 100, 102, 103, 104]

data_1 = [['Mike', 1, 'Thailand', 80],
          ['Yang', 2, 'China', 77],
          ['Tom', 3, 'England'],
          ['Losa', 4, "Japan", 90],
          ['Zhang', 5, 'China', 73]]

data_2 = [['Tim', 6, 'America', 87],
          ['Lucy', 7, 'Japan', 91],
          ['Jack', 9, 'India', 85],
          ['Wang', 8, 'China', 89],
          ['Chang', 10, "Thailand", 94]]

df_1 = pd.DataFrame(data_1, columns=columns, index=index)
df_2 = pd.DataFrame(data_2, columns=columns, index=index)
print ('df_1')
print(df_1)
print('df_2')
print(df_2)

# concat 函数连接多个DataFrame，concat函数的优势是可以接受多个DataFrame连接在一起
# 在默认情况下，concat会将DataFrame按行粘合在一起，同时会将各列自动对齐
print('concat')
# axis=0 时，即使索引（index）重复，也会连接成新的行
print(pd.concat([df_1, df_2], axis=0))
# axis=1 时，如果索引（index）重复，会增加新的行
print(pd.concat([df_1, df_2], axis=1))


# join 函数，依靠索引连接两个DataFrame
# join 函數在连接两个DataFrame时，这两个DataFrame的列会连接在一起，而行的行为会借助集合论的原理来确定
'''
df1
    A   B
0   1   2
1   3   4
2   5   6

df2
    C   D
1  10  20
3  30  40

连接的类型
内连接
    A   B   C   D
1   3   4  10  20

左连接
    A   B   C   D
0   1   2  NA  NA
1   3   4  10  20
2   5   6  NA  NA

右连接
    A   B   C   D
1   3   4  10  20
3  NA  NA  30  40

外连接
    A   B   C   D
0   1   2  NA  NA
1   3   4  10  20
2   5   6  NA  NA
3  NA  NA  30  40

类型     描述
inner   只保留索引为两个DataFrame共有的行
left    左端DataFrame的所有行，用右端DataFrame中的行去匹配
right   右端DataFrame的所有行，用左端DataFrame中的行去匹配
outer   两个DataFrame行索引的并集
'''
df_3 = pd.DataFrame(data=[[1, 2], [3, 4], [5, 6]], columns=['A', 'B'])
df_4 = pd.DataFrame(data=[[10, 20], [30, 40]], columns=['C', 'D'], index=[1, 3])
print('df_3')
print(df_3)
print('df_4')
print(df_4)
print('join')
print(df_3.join(df_4, how='inner'))
print(df_3.join(df_4, how='left'))
print(df_3.join(df_4, how='right'))
print(df_3.join(df_4, how='outer'))

# merge 函数，通过on参数提供的一列或多列作为连接条件（join condition），这些列必须是两个DataFrame所共有的，它们会被用来和行进行匹配
# 在df_3、df_4中添加一个"category"列
df_3['category'] = ['a', 'b', 'c']
df_4['category'] = ['c', 'b']
print('新df_3')
print(df_3)
print('新df_4')
print(df_4)
print('merge')
print(df_3.merge(df_4, how='inner', on=['category']))
print(df_3.merge(df_4, how='left', on=['category']))