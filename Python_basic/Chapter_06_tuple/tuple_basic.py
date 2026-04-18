# tuple_basic.py

a_tuple = (1, 2, 3)
b_tuple = ('a', 'b', 'c', 'd')
c_tuple = ()
d_tuple = (42,) 

# 元組
print('元組')
print(a_tuple)
print(b_tuple)
print(c_tuple)
print(d_tuple)

# 元組的切片(slicing),第一個索引是包含的第一個元素的編號，第二個索引是切片後餘下的第一個元素的編號。
# 元组的切片也是元组，就像列表的切片也是列表一样。
# 元组的索引(indexing),第一個元素的索引是0；最後一個元素的索引是 -1
print('元組切片')
print(b_tuple[1])
print(b_tuple[1: 2])

# 元組相加+，用加法運算符相加。
print('元組相加')
e_tuple = a_tuple + b_tuple
print(e_tuple)

# 元組的乘法*，將元組與數x相乘時，將重複這個元組x次來創建一個新元組。
print('元組的乘法')
f_tuple = b_tuple * 3
print(f_tuple)
g_tuple = (42,) * 5
print(g_tuple)
h_tuple = (None,) * 3
print(h_tuple)

# 元組的成員資格檢查：in 要檢查特定的值是否包含在元組中，可以使用運算符in，包含返回True，不包含返回False。
print('元組的成員資格檢查')
if 'b' in b_tuple:
    print('b is in b_tuple')