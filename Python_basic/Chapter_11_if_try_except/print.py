# print_function.py

import time

# 簡單的列印一個字串
print('Hello, world!')

# 列印多個數據，用逗號分隔
print('Hello,', 'world!', 2023)

# 列印多個數據，用指定的分隔符分隔
print('Hello,', 'world!', 2023, sep='---')

# 列印數據，並在結束時加上指定的結束符
print('Hello, world!', end = '###')

# 把數據輸出到指定的文件
with open('output.txt', 'w') as f:
    print('Hello, world!', file = f)

# flush=True 的作用
for i in range(10):
    print(i, flush=True)
    time.sleep(1)       # 暫停一秒