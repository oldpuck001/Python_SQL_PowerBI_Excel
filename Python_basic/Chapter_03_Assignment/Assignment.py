# Assignment.py

# 序列解包（可迭代對象解包）:
x, y, z = 1, 2, 3
print(x, y, z)

x, y = y, x
print(x, y, z)

values = 1, 2, 3
print(values)

x, y, z = values
print(x)

scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print(key)
print(value)

#  使用星號運算符（*）來收集多餘的值，這樣無需確保值和變量的個數相同，還可將帶星號的變量放在其他位置。
#  賦值語句的右邊可以是任何類型的序列，但帶星號的變量最終包含的總是一個列表。在變量和值的個數相同時亦如此。
a, b, *rest = [1, 2, 3, 4]
print(rest)

name = 'Albus Percival Wulfric Brian Dumbledore'
first, *middle, last = name.split()
print(middle)

a, *b, c = 'abc'
print(a, b, c)

fnord = 'foo'
fnord += 'bar'
fnord *= 2
print(fnord)