# DataFrame_to_list.py

import pandas as pd

# 假設您有以下DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}

df = pd.DataFrame(data)

# 将某列的数据复制到列表中
column_list = df['A'].tolist()
print(column_list)

# 将某行的数据复制到列表中
row_list = df.iloc[1].tolist()
print(row_list)

# 將使用iloc選擇的數據轉換為列表形式
selected_data = df.iloc[1:2, 0:1]
data_list = selected_data.values.tolist()
print(data_list)

# 将整个DataFrame的数据复制到列表中
# 如果只想簡單地將整個DataFrame轉換為一個二維列表，df.values.tolist()是更好的選擇，如果需要對每一行進行特定的處理，那麼使用列表推導式可能會更合適
# 方式一
list_of_rows_1 = df.values.tolist()
print(list_of_rows_1)
# 方式二，轉換為一個列表的列表，每個內部列表都是一行
list_of_rows_2 = [row.tolist() for _, row in df.iterrows()]
print(list_of_rows_2)

# df.iterrows()：pandas的DataFrame方法，用于迭代DataFrame的行。它返回一个迭代器，生成索引和对应的行数据（作为pandas的Series对象）
# for _, row in df.iterrows()： 遍历iterrows() 返回的每一行。在这里，_ 表示我们不关心行的索引值。如果需要行的索引，可以替换 _ 为一个变量名
# row.tolist()：将pandas的Series对象转换为Python的列表
# [...]：这是一个列表推导式，它为DataFrame中的每一行生成一个列表，并将所有这些列表组合成一个大列表