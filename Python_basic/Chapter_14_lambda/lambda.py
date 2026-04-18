# lambda.py

# 使用lambda作為map的參數
# map函數用於將一個函數應用到一個可迭代對象中的每一個元素上，並返回一個map對象。可迭代對象，例如是列表、元組等。map對象一個迭代器。
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)


# 使用lambda定義排序的key
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key = lambda pair: pair[1])
print(pairs)