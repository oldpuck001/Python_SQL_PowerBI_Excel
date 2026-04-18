# for.py

a_list = ['a', 'b', 'c', 'd']

for p in a_list:
    if p == 'b':
        continue
    if p == 'c':
        break
    print(p)

for p in a_list:
    if p == 'b':
        continue
    if p == 'y':
        break
    print(p)
else:
    print('no break')

# for循環與range範圍函數結合使用:
# range(start, stop, step)
# 創建一個由整數組成的列表
# 範圍類似於切片，包含起始位置（這里為0），但不包含結束位置（這里為10）。
# range傳遞了第三個參數——步長，即序列中相鄰數的差。通過將步長設置為負數，可讓range向下迭代，還可讓它跳過一些數。

for number in range(0, 10, 2):
    print(number)

# 迭代時獲取索引：
# 函數enumerate(seq)
# 生成可迭代的索引-值對。
# 在有些情況下，需要在迭代對象序列的同時獲取當前對象的索引。

for index, string in enumerate(a_list):
    if 'b' in string:
        a_list[index] = '[censored]'

print(a_list)

# 使用字典的items方法迭代字典時獲取鍵值對：

a_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in a_dict.items():
    print(key, 'corresponds to', value)


# 並行迭代（zip函數）：
# zip(seq1, seq2, …)
# 創建一個適合用於並行迭代的新序列。
# 當序列的長度不同時，函數zip將在最短的序列用完後停止“縫合”。

str_list = ['a', 'b', 'c', 'd']
value_list = [1, 2, 3, 4]

for str_str, value_valur in zip(str_list, value_list):
    print(str_str, value_valur)