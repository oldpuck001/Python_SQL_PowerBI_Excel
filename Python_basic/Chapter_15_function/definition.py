# definitio0n.py

# 下面的函數返回一個由斐波那契數組成的列表（一種數列，其中每個數都是前兩個數的和）。

def fibs(num = 10):

    result = [0, 1]
    
    for i in range(num-2):
        result.append(result[-2]+result[-1])

    return result

print(fibs())
print(fibs(30))


str_one = 'Hi,'
str_two = 'my world!'

def print_str(str_1 = 'Hello,', str_2 = 'world!'):
    print(str_1, str_2)

print_str()
print_str(str_2 = str_two)
print_str(str_one, str_two)


def print_params(x, y, z = 3, *pospar, **keypar):
   print(x, y, z)
   print(pospar)
   print(keypar)

print_params(1, 2, 3, 4, 5, 6, 7, foo = 1, bar = 2)
print_params(1, 2)