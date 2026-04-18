# class_class.py

# Person是類的名稱
# class語句創建獨立的命名空間，用於在其中定義函數
# self指向對象本身,如果沒有self，所有的方法都無法訪問對象本身——要操作的屬性所屬的對象
# 與自定義函數時一樣，也可以從外部訪問這些屬性
# 如果foo是一個Person實例，可將foo.greet()視為Person.greet(foo)的簡寫，但後者的多態性更低

class Person:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print(f'Hello, world! I’m {self.name}.')


foo = Person()
bar = Person()
foo.set_name('Luke Skywalker')
bar.set_name('Anakin Skywalker')

foo.greet()
bar.greet()

print(foo.name)

bar.name = 'Yoda'
bar.greet()