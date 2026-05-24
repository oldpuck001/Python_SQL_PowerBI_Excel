# list_basic.py

None_list = [None] * 3
a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
b_list = [16, 17, 18, 19, 20]
c_list = ['a', 'b', 'c', 'd']

# 包含None的列表
print('包含None的列表')
print(None_list)

# 列表的切片
print('列表的切片')
print(a_list)
print(a_list[4:10])
print(a_list[4:10][2])

# 切片的簡寫：如果切片結束於序列末尾，可以省略第二個索引。
print('切片的簡寫')
print(a_list[-3:])
print(a_list[:3])
print(a_list[11:-4])
print(a_list[:])              # 切片整個序列的縮寫
print(a_list[-3:])            # 索引也可以使用負數。使用負數時，如果要包含最後一個元素，即-1索引位置的元素
print(a_list[3:10:3])         # 切片可以有步長
print(a_list[::-1])           # 有步長時，可以照常用簡寫，步長可以為正數或負數，不能為0。
print(a_list[8:3:-1])         # 步長為負數時，第一個索引必須比第二個索引大。

# 列表相加：+ 用加法運算符相加，不能拼接不同類型的序列。
print('列表相加')
print(a_list + b_list + c_list)

# 列表的乘法：* 將序列與數x相乘時，將重複這個序列x次來創建一個新序列。
print('列表的乘法')
print(b_list * 2)

# 列表的成員資格檢查：in 要檢查特定的值是否包含在序列中，可以使用運算符in，包含返回True，不包含返回False。
print('列表的成員資格檢查')
if 'b' in c_list:
    print('b is in d_list.')

# 修改列表（給元素賦值）：不能給不存在的元素賦值。
print('修改列表（給元素賦值）')
b_list[2] = 100
print(b_list) 

# 刪除列表元素：del 列表的長度會相應減少。
print('刪除列表元素')
del b_list[2]
print(b_list) 

# 給列表切片賦值：使用切片賦值，即可將切片替換為長度與其不同的序列,也可在不替換原有元素的情況下插入新元素。 
print('給列表切片賦值')
c_list[2:] = list('ython')        # “替換”了一個空切片，相當於插入了一個序列。
print(c_list)
b_list[1:3] = []                  # 與del b_list[1:2]等效；可以執行步長不為1（乃至為負）的切片賦值。
print(b_list)
a_list[2:7:2]=[100, 100, 100]     # 與del b_list[1:2]等效；可以執行步長不為1（乃至為負）的切片賦值。
print(a_list)
b_list[1:1] = [17, 18, 19]        # 使用切片賦值插入数据。
print(b_list)