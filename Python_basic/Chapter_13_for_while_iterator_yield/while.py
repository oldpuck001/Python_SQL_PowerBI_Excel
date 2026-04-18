# while.py

x = 94
while x <= 100:
    x += 1
    if x == 97:
        continue
    if x == 99:
        break
    print(x)

y = 94
while y <= 100:
    y += 1
    if y == 97:
        continue
    if y == 120:
        break
    print(y)
else:
    print('no break')

name = ''
# 可改為while not name or name.isspace()或while not name.strip()
while not name:
    name = input('Please enter your name: ')

print('Hello,{}!'.format(name))


# while True/break成例：輸入單詞時執行某種操作，沒有提供單詞時結束循環
while True:
    word = input('Please enter a word:')
    if not word: break
    #使用这个单词做些事情：
    print('The word was', word)