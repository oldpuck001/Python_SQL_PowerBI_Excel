# list_comprehensions.py

# 列表推導
# 示例1:建立列表
i_list = [x * x for x in range(10)]
print(i_list)

# 示例2:在列表推導中添加一條if語句。
# 如果只想打印能被3整除的平方值，可使用求模運算符：如果y能被3整除，y % 3將返回0，僅當x能被3整除時，x*x才能被3整除。
j_list = [x * x for x in range(10) if x % 3 == 0]
print(j_list)

# 示例3:添加更多的for部分。
k_list = [(x, y) for x in range(3) for y in range(3)]
print(k_list)

# 示例4:使用多個for部分時，也可添加if子句。
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print([b + '+' + g for b in boys for g in girls if b[0] == g[0]])

# 示例4:示例4效率更好的解法，示例4需要檢查每種可能的配對。（Alex Martelli推薦的解決方案）
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print([b + '+' + g for b in boys for g in letterGirls[b[0]]])
# 這個程序創建一個名為letterGirls的字典，其中每項的鍵都是一個字母，而值為以這個字母打頭的女孩名字組成的列表。
# 創建這個字典後，列表推導遍歷所有的男孩，並查找名字首字母與當前男孩相同的所有女孩。
# 這樣，這個列表推導就無需嘗試所有的男孩和女孩組合併檢查他們的名字首字母是否相同了。
# 字典方法setdefault：訪問不存在的鍵時添加鍵。