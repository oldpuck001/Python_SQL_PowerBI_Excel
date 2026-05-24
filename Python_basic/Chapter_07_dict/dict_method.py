# dict_method.py

phonebook = {'Zhao': '1391231234', 'Li':'1300001234', 'Wang':'1333214321'}

# 如果字典包含指定的鍵，get的作用將與普通字典查找相同;訪問不存在的鍵時，默認返回None，可以设置返回指定值。
# 访问不存在的键时，使用get方法、if语句、try/except语句的对比，请参考码农高天的视频：
# b站：https://www.bilibili.com/video/BV1MM411w7Te/?spm_id_from=333.337.search-card.all.click
# YouTube：https://www.youtube.com/watch?v=NjeiQY9aNW4&list=PLmDfTmp9rjCmZKR7NaS2GHwZlMW0VFt4C&index=5
print('get方法')
print(phonebook.get('Li'))
print(phonebook.get('liang', 'N/A'))

# 如果指定的鍵存在，就返回其值，並保持字典不變。指定的鍵不存在時，setdefault返回指定的值並相應地更新字典。值的默認為None，可以设置指定值。
print('setdefault方法')
phonebook.setdefault('Chen')
print(phonebook)
phonebook.setdefault('Yan', 'N/A')
print(phonebook)

# update方法使用一個字典中的項來更新另一個字典。對於通過參數提供的字典，將其項添加到當前字典中。
# 如果當前字典包含鍵相同的項，就替換它。可像調用函數dict（類型構造函數）那樣調用方法update。
# 這意味著調用update時，可向它提供一個映射、一個由鍵值對組成的序列（或其他可迭代對象）或關鍵字參數。
print('updata方法')
x = {'Li': '13000000000', 'Liu': '1319879876'}
phonebook.update(x)
print(phonebook)

# pop方法用於獲取與指定鍵相關聯的值，並將該鍵值對從字典中刪除。
print('pop方法')
phonebook.pop('Liu')
print(phonebook)

# popitem方法隨機彈出一個字典項並刪除。如果要以高效地方式逐個刪除並處理所有字典項，這可能很有用，因為這樣無需先獲取鍵列表。
print('popitem方法')
phonebook.popitem()
print(phonebook)
key, value = phonebook.popitem()
print(key)
print(value)

# items方法返回一個包含所有字典項的列表（返回值屬於一種名為字典視圖的特殊類型。
# 字典視圖可用於迭代，還可確定其長度以及對其執行成員資格檢查。
# 視圖的一個優點是不復制，它們始終是底層字典的反映，即便修改了底層字典亦如此。），其中每個元素都為(key, value)的形式。
# 字典項在列表中的排列順序不確定。
print('items方法')
dict_items = phonebook.items()
print(dict_items)

# keys方法返回一個字典視圖，其中包含指定字典中的鍵。
print('keys方法')
dict_keys = phonebook.keys()
print(dict_keys)

# values方法返回由字典的值組成的字典視圖。不同於方法keys，方法values返回的視圖可能包含重複的值。
print('values方法')
dict_values = phonebook.values()
print(dict_values)

# clear方法刪除所有的字典項，這種操作是就地執行的（就像list、sort一樣），因此什麼都不返回（或者說返回None）。
print('clear方法')
phonebook.clear()
print(phonebook)