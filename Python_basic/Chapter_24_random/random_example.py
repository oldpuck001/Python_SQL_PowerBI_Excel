# random.py

import random

seq_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

# random() 返回一個0～1（含）的隨機實數（偽隨機數），除非這正是你需要的，否則可能應使用其他提供了額外功能的函數。
print('返回一個0～1（含）的隨機實數（偽隨機數）：')
print(random.random())


# uniform(a,b) 返回一個a～b（含）的隨機（均勻分佈的）實數
# 編寫與統計相關的程序時，可使用其他類似於uniform的函數，它們返回按各種分佈隨機採集的數字，如貝塔分佈、指數分佈、高斯分佈等。
print('返回一個a～b（含）的隨機（均勻分佈的）實數：')
print(random.uniform(0, 10))


# randrange([start],stop,[step]) 從range(start, stop, step)中隨機地選擇一個數，生成隨機整數的標準函數。
print('從range(start, stop, step)中隨機地選擇一個數，生成隨機整數的標準函數：')
print(random.randrange(10) + 1)
print(random.randrange(1, 20, 2))


# choice(seq) 從序列seq中隨機地選擇一個元素
print('從序列seq中隨機地選擇一個元素：')
print(random.choice(seq_list))


# shuffle(seq[,random]) 隨機地打亂一個可變序列中的元素，並確保每種可能的排列順序出現的概率相同。
print('隨機地打亂一個可變序列中的元素，並確保每種可能的排列順序出現的概率相同：')
random.shuffle(seq_list)
print(seq_list)
# 默認情況下，使用內建的random模組中的隨機數生成器,如果提供了random參數，將使用用戶提供的隨機數生成器，而不是默認的。


# sample(seq, n) 從序列seq中隨機地選擇n個值不同的元素
print('從序列seq中隨機地選擇n個值不同的元素：')
print(random.sample(seq_list, 4))


#函數random.sample從給定序列中隨機（均勻）地選擇指定數量的元素，並確保所選擇元素的值各不相同。
print('從給定序列中隨機（均勻）地選擇指定數量的元素，並確保所選擇元素的值各不相同：')
print(random.sample(seq_list, 6))