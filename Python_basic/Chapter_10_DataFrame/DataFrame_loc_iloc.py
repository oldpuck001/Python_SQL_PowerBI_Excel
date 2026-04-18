# DataFrame_loc_iloc.py

# df.loc
# df.iloc

import pandas as pd

columns = ['name', 'No.', 'country', 'score', 'job']

index=[101, 100, 102, 103, 104, 105, 106, 107, 108, 109]

data = [['Mike', 1, 'Thailand', 80, 'teacher'],
        ['Yang', 2, 'China', 77, 'student'],
        ['Tom', 3, 'England', 85, 'student'],
        ['Losa', 4, "Japan", 90, 'accounting'],
        ['Tim', 6, 'America', 87, 'student'],
        ['Zhang', 5, 'China', 73, 'student'],
        ['Jack', 9, 'India', 85, 'student'],
        ['Wang', 8, 'China', 89, 'student'],
        ['Chang', 10, "Thailand", 94, 'accounting'],
        ['Lucy', 7, "Japan", 91, 'employee']
        ]

df = pd.DataFrame(data, columns=columns, index=index)

# loc 通過標籤選取數據，支持切片語法，但是與Python其他地方不同，這裡的切片是閉區間，包含了首尾兩個標籤
# df.loc[row_selection, column_selection]
print('df.loc[row_selection, column_selection]')
print(df.loc[103, 'country'])           # 單個值
print(df.loc[:, 'country'])             # 單個列，返回一維的Series數據結構
print(df.loc[:, ['country']])           # 單個列，返回多維的DataFrame數據結構
print(df.loc[:, ['No.', 'country']])    # 多個列
print(df.loc[:, 'name':'country'])      # 列區間
print(df.loc[105, :])                   # 單個行，返回一維的Series數據結構
print(df.loc[[105], :])                 # 單個行，返回多維的DataFrame數據結構
print(df.loc[[102, 106, 108], :])       # 多個行
print(df.loc[103:107, :])               # 行區間

# 選擇列的更便捷寫法，這種簡便寫法不支持列區間
print(df['country'])            # 單個列，返回一維的Series數據結構
print(df[['country']])          # 單個列，返回多維的DataFrame數據結構
print(df[['name', 'country']])  # 多個列

# 使用多級索引（MultiIndex）選取數據
df_multi = df.reset_index().set_index(['job', 'country'])
print(df_multi.loc['student', :])
print(df_multi.loc[('student', 'China'), :])

# iloc 通过位置选取数，iloc 的切片區間與Python一樣，是半開半閉的
print('df.iloc[row_begin:row_end, column_bengin:column_end]')
print('df.iloc[[row_1, row_2], [column_1, column_2]]')
print(df.iloc[1, 2])            # 單個值
print(df.iloc[:, 2])            # 單個列，返回一維的Series數據結構
print(df.iloc[:, [2]])          # 單個列，返回多維的DataFrame數據結構
print(df.iloc[:, [2, 1]])       # 多個列
print(df.iloc[:, :3])           # 列區間
print(df.iloc[1, :])            # 單個行，返回一維的Series數據結構
print(df.iloc[[1], :])          # 單個行，返回多維的DataFrame數據結構
print(df.iloc[[3, 1], :])       # 多個行
print(df.iloc[1:5, :])          # 行區間

# 使用布爾索引選取數據
# 布爾索引（booleam indexing）借助只包含True或False的Series或DataFrame來選去一個DataFrame的子集
# DataFrame的布爾運算符：& | ~
# 如果篩選條件不只一條，一定要在每條布爾表達式之間加上圓括號
# 最常見的用例是是用來篩選DataFrame的行
print('使用布爾索引選取數據')
tf = (df['No.'] > 5) & (df['country'] == "Thailand")        # 这个Series中只有True和False
print(tf)
print(df.loc[tf, :])

# 對索引進行篩選
print('對索引進行篩選')
print(df.loc[df.index>105, :])

# 使用isin方法篩選，類似於in運算符的功能
print('使用isin方法篩選，類似於in運算符的功能')
print(df.loc[df['country'].isin(['Thailand', 'Japan']), :])

# 在不使用loc的情況下傳遞一整個布爾DataFrame作為參數，DataFrame只包含數字時排除異常值特別有用
# df[boolean_df]
print('df[boolean_df]')
numbers = pd.DataFrame(data={"col 1": [250.1, 99.4],
                             "col 2": [350.4, 129.7],
                             "col 3": [200.7, 100.6]})
print(numbers < 250)
print(numbers[numbers <250])