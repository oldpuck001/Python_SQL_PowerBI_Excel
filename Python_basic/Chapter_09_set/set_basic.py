# set_basic.py

a_set = {0, 1, 2, 3, 0, 1, 2, 3, 4, 5}
b_set = set(range(10))
c_set = set()
d_set = {None, }

# 集合
print('集合')
print(a_set)
print(b_set)
print(c_set)
print(type(c_set))
print(d_set)
print(type(d_set))

# 使用集合對列表或者元组去重
e_set = set(["USD", "USD", "SGD", "EUR", "USD", "EUR"])
print(e_set)

# 集合的運算符：

# 並集
print('並集')
f_set = a_set | b_set
print(f_set)

# 交集
print('交集')
g_set = a_set & b_set                        
print(g_set)

# a和b的對稱差集
print('對稱差集')
h_set = a_set ^ b_set
print(h_set)

# 集合的減法
print('集合的減法')
i_set = a_set - b_set
print(i_set)
j_set = b_set - a_set
print(j_set)

# <=
print('集合的<=')
print(a_set <= b_set)

# >=
print('集合的<=')
print(b_set >= a_set)