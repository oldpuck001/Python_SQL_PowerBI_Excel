# str_example.py

a_str = '$$$ Get rich now!!! $$$'
b_str = 'abcdefghijk'
d_str = '    abcd  '
e_str = '*** ABCDefghijk!!! **'
h_str = '1+2+3+4+5'
i_str = '/usr/bin/env'
j_str = 'Using the default'

# 字符串方法：

# find方法在字符串中查找子串，可以用in方法檢查也可使用find來執行。如果找到，就返回子串的第一個字符的索引，否則返回-1。
# 還可指定搜索的起點和終點（它們都是可選的）。請注意，起點和終點值（第二個和第三個參數）指定的搜索範圍包含起點，但不包含終點。
print('find方法')
print(a_str)
print(a_str.find('$$$'))
print(a_str.find('$$$', 1))         # 只指定了起点
print(a_str.find('!!!'))
print(a_str.find('!!!', 0, 16))     # 同时指定了起点和终点

# replace方法將指定子串替換為另一個並返回，並返回替換後的結果。因為字符串是不可變的，所以所有的元素賦值和切片賦值都是非法的。
c_str = b_str.replace('bc', 'xyz')
print(c_str)

# strip方法將字符串開頭和末尾的指定字符串刪除，並返回刪除後的結果，默認情況下刪除的是開頭和末尾的空白。
# 這個方法只刪除開頭或末尾的指定字符，因此中間的指定字符不會被刪除。
print('strip方法')
f_str = d_str.strip('')
print(f_str)
g_str = e_str.strip(' *!')
print(g_str)

# split方法用於將字符串拆分為序列。注意，如果没有指定分隔符，将默认在单个或多个连续的空白字符（空格、制表符、换行符等）处进行拆分。
print('split方法')
k_str = h_str.split('+')
print(k_str)
l_str = i_str.split('/')
print(l_str)
m_str = j_str.split()
print(m_str)

# join方法通過使用不同的分隔符，將序列的元素合併為一個字符串。所有合併序列的元素必須都是字符串。
print('join方法')
seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))
dirs = ('', 'usr', 'bin', 'env')
print('/'.join(dirs))

# lower方法返回字符串的小寫版本。
print('lower方法')
n_str = a_str.lower()
print(n_str)