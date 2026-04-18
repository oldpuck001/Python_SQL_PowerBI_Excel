# definition_closure.py

# Python函數可以嵌套，即可將一個函數放在另一個函數內。嵌套通常用處不大，但有一個很突出的用途：使用一個函數來創建另一個函數。

def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor

# 在這裡，一個函數位於另一個函數中，且外面的函數返回裡面的函數。也就是返回一個函數，而不是調用它。
# 重要的是，返回的函數能夠訪問其定義所在的作用域。換而言之，它攜帶著自己所在的環境和相關的局部變量.

# 每當外部函數被調用時，都將重新定義內部的函數，而變量factor的值也可能不同。
# 由於Python的嵌套作用域，可在內部函數中訪問這個來自外部局部作用域（multiplier）的變量.
# 像multiplyByFactor這樣存儲其所在作用域的函數稱為閉包。
# 通常，不能給外部作用域內的變量賦值，但如果一定要這樣做，可使用關鍵字nonlocal。這個關鍵字的用法與global很像。

double = multiplier(2)

print(double(5))


triple = multiplier(3)

print(triple(3))


print(multiplier(5)(4))