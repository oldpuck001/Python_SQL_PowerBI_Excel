# DataFrame_operation.py

import pandas as pd

numbers_1 = pd.DataFrame(data={'col 1': [250.1, 99.4],
                               'col 2': [350.4, 129.7],
                               'col 3': [200.7, 100.6]})

numbers_2 = pd.DataFrame(data=[[100, 200],[300, 400]], index=[1, 2], columns=['col 1', 'col 4'])

print(numbers_1)
print(numbers_2)

# 算术运算符与DataFrame方法的对应关系
# 运算符    方法
# *        mul
# +        add
# -        sub
# /        div
# **       pow

# 为DataFrame中的每一个值加上一个数
print(numbers_1 + 100)

# 使用 + 號求兩個DataFrame的和，結果它們都有的字段會被相加，其他的部分會顯示為NaN
print(numbers_1 + numbers_2)

# 使用 add 方法，並將fill_value参数设置为0，会得出类似Excel的效果
print(numbers_1.add(numbers_2, fill_value=0))

# 當算式的操作數是一個DataFrame和一個Series時，默認情況下Series會按索引（行）對每列對應的值進行運算
numbers_3 = pd.Series(data={'col 1':100, 'col 2': 100, 'col 3': 100})
print(numbers_1 + numbers_3)

numbers_4 = pd.Series(data=[1000, 1000])
print(numbers_4)
print(numbers_1.add(numbers_4, axis=0))