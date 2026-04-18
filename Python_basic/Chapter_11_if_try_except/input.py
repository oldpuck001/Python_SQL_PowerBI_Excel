# input_function.py

# input函數的基本用法
user_input = input('請輸入文字：')
print('您輸入了：', user_input)

# 將用戶輸入的字符串轉換為整數，可以使用int函數
user_input = int(input('請輸入一個整數：'))
print('您輸入的整數是：', user_input)

# 將用戶輸入的字符串轉換為浮點數，可以使用float函數
user_input = float(input('請輸入一個浮點數：'))
print('您輸入的浮點數是：', user_input)

# 如果用戶輸入的不是一個有效的整數或浮點數字符串，int或float函數會引發ValueError,可使用try和except語句來處理這種錯誤
try:
    user_input = int(input('請輸入一個整數：'))
    print('您輸入的整數是：', user_input)
except ValueError:
    print('您輸入的不是一個有效的整數！')