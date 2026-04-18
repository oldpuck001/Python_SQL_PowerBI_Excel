# class_init.py

# 構造函數__init__
# 在Python中，創建構造函數很容易，只需將方法init的名稱從普通的init改為前後加了雙下劃線的__init__即可。

class FooBar_1:

    def __init__(self):

        self.somevar = 42


f = FooBar_1()
print(f.somevar)


# 給構造函數添加參數的結果

class FooBar_2:

    def __init__(self, somvar):

        self.somevar = somvar

g = FooBar_2('This is a constructor argument')
print(g.somevar)