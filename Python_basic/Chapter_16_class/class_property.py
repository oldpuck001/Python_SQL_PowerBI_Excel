# class_property.py

# 在Python中，創建特性的機制：函數property

# property(fget, fset, fdel, doc)

# 返回一個特性,所有參數都是可選的

class Rectangle:

    def __init__(self):

        self.width = 0
        self.height = 0

    def set_size(self, size):

        self.width, self.height = size

    def get_size(self):

        return self.width, self.height
    
    size = property(get_size, set_size)

r = Rectangle()

r.width = 10
r.height = 5
print(r.size)

r.size = 150, 100
print(r.width)


# 調用函數property時，可不指定參數、指定一個參數、指定兩個參數、指定三個參數或指定四個參數。

# 如果沒有指定任何參數，創建的特性將既不可讀也不可寫。
# 如果指定一個參數（獲取方法），創建的特性將是只讀的。
# 如果指定兩個參數，創建的特性將是可讀可寫的。
# 第三個參數是可選的，指定用於刪除屬性的方法（這個方法不接受任何參數）。
# 第四個參數是可選的，指定一個文檔字符串。

# 這些參數分別名為fget、fset、fdel和doc。如果要創建一個只可寫且帶文檔字符串的特性，可使用它們作為關鍵字參數來實現。

# 對於新式類，應使用特性而不是存取方法。

# 函數property的工作原理：
# property其實並不是函數，而是一個類。
# 它的實例包含一些魔法方法，而所有的魔法都是由這些方法完成的。
# 這些魔法方法為__get__、__set__、__delete__，它們一道定義了所謂的描述符協議。
# 只要對象實現了這些方法中的任何一個，它就是一個描述符。描述符的獨特之處在於其訪問方式。
# 例如，讀取屬性（具體來說，是在實例中訪問類中定義的屬性）時，如果它關聯的是一個實現了__get__的對象，
# 將不會返回這個對象，而是調用方法__get__並將其結果返回。
# 實際上，這是隱藏在特性、關聯的方法、靜態方法和類方法以及super後面的機制。
# 有關描述符的詳細信息，請參閱Descriptor HowTo Guide（http://docs.python.org/3/howto/descriptor.html）。