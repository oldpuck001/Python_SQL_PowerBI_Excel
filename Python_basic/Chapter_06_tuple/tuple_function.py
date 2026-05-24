# tuple_function.py

a_tuple = (1, 2, 3)

#元組函數：
print('元組函數')

# tuple函數將序列轉換為元組（創建元組），tuple可將任何序列（而不僅僅是字符串）作為tuple的參數。tuple實際不是函數，是一個類。
b_tuple = tuple([1, 2, 3])
print(b_tuple)
c_tuple = tuple('abc')
print(c_tuple)
d_list = tuple((1, 2, 3))
print(d_list)

print(len(a_tuple))         # len函數返回元組包含的元素個數。

print(min(a_tuple))         # min函數返回元組中最小的元素。

print(max(a_tuple))         # max函數返回元組中最大的元素。