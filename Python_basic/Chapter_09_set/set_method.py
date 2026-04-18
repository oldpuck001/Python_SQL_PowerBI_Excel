# set_method.py

a_set = {0,1,2,3,0,1,2,3,4,5}
b_set = set(range(10))

# 集合方法
# 並集
print('union方法（並集）')
c_set = a_set.union(b_set)
print(c_set)

# 交集
print('intersection方法（交集）')
d_set = a_set.intersection(b_set)
print(d_set)

# symmetric_difference方法，取兩個集合的對稱差集，返回一個新的集合，其中包含所有在集合a或集合b中出現，但不同時出現在兩個集合中的元素。
print('symmetric_difference方法（對稱差集）')
e_set = a_set.symmetric_difference(b_set)
print(e_set)

# difference方法，返回集合a中有而集合b中没有的元素组成的新集合
print('difference方法')
f_set = b_set.difference(a_set)
print(f_set)

# issubset方法，接受一個集合作為參數，並返回一個布爾值表示當前集合是否是該參數集合的子集，子集的相對概念是超集。
print('issubset方法')
print(a_set.issubset(b_set))

# add方法，將1個元素添加到集合中
print('add方法')
a_set.add(100)
print(a_set)

# remove方法，從集合中移除指定元素，如果元素不存在，則引發KeyError異常
print('remove方法')
a_set.remove(100)
print(a_set)

# copy方法，用於返回一個集合（set）的複製。這個方法將返回一個包含原始集合中所有元素的新集合，對這個新集合的任何更改都不會影響原始集合。
print('copy方法')
g_set = a_set.copy()
print(g_set)