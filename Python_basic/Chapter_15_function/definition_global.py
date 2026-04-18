# definition_global.py

# global：可以使用函數globals來訪問全局變量。
# 在函數內部給變量賦值時，該變量默認為局部變量，除非你明確地告訴Python它是全局變量。

x = 1

def change_global():
    global x
    x = x + 1

change_global()

print(x)