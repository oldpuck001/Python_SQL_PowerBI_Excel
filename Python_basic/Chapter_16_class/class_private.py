# class_private.py

# 將屬性設為私有：

# 默認情況下，可從外部訪問對象的屬性。私有屬性不能從對像外部訪問，而只能通過對象的方法來訪問。

# Python沒有為私有屬性提供直接的支持，而是要求程序員知道在什麼情況下從外部修改屬性是安全的。

# 要讓方法或屬性成為私有的（不能從外部訪問），只需讓其名稱以兩個下劃線打頭，就可獲得類似於私有屬性的效果。

class Secretive:

    def __inaccessible(self):
        print("Bet you can't see me ...")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()


s = Secretive()

s.accessible()

# 在類定義中，對所有以兩個下劃線打頭的名稱都進行轉換，即在開頭加上一個下劃線和類名。

print(Secretive._Secretive__inaccessible)

s._Secretive__inaccessible()

s.__inaccessible()

# 無法禁止別人訪問對象的私有方法和屬性，但這種名稱修改方式發出了強烈的信號，讓他們不要這樣做。

# 如果不希望名稱被修改，又想發出不要從外部修改屬性或方法的信號，可用一個下劃線打頭。
# 這只是一種約定，但也有些作用。例如，from module import *不會導入以一個下劃線打頭的名稱。

# 對於成員變量（屬性），有些語言支持多種私有程度。例如，Java支持4種不同的私有程度。 
# Python沒有提供這樣的支持，不過從某種程度上說，以一個和兩個下劃線打頭相當於兩種不同的私有程度。