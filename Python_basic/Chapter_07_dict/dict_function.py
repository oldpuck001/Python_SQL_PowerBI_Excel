# dict_function.py

phonebook = {'Zhao': '1391231234', 'Li':'1300001234', 'Wang':'1333214321'}

# 字典函數：

items = [('name', 'Liu'), ('age', 40)]
a_dict = dict(items)                        # dict從键-值对、映射或關鍵字參數創建字典
print(a_dict)
print(a_dict['name'])

b_dict = dict(name = 'Zhou', age = 30)     # 也可使用一個映射實參來調用它，這將創建一個字典，其中包含指定映射中的所有項。
print(b_dict)

c_dict = phonebook.copy()                  # 從映射創建字典時，如果該映射也是字典，可不使用函數dict，而是使用字典方法copy。
print(phonebook)
print(c_dict)
c_dict['Zheng'] = '18612312343'
print(phonebook)
print(c_dict)
# 返回一個新字典，其包含的鍵值對與原來的字典相同（這個方法執行的是淺複製，因為值本身是原件，而非副本）.
# 當替換副本中的值時，原件不受影響。
# 如果修改副本中的值（就地修改而不是替換），原件也將發生變化，因為原件指向的也是被修改的值。
# 淺複製替換附件不影響原件，修改副本影響原件。

d_dict = dict.fromkeys(['name','age'])      # fromkeys方法創建一個新字典，其中包含指定的鍵，且每個鍵對應的值都是None。如果不想使用默認值None，可提供特定的值。
print(d_dict)
e_dict = dict.fromkeys(['name','age'],'(unknown)')
print(e_dict)

print(len(phonebook))                       # len函数返回字典d包含的項（鍵值對）數。

phonebook['Qian'] = '1830004321'            # 即便是字典中原本沒有的鍵，也可以給它賦值，這將在字典中創建一個新項。
print(phonebook['Qian'])

d = 'Qian'
del phonebook[d]                            # 刪除鍵為d的項。
print(phonebook)

if 'Wang' in phonebook:                    # 檢查字典phonebook是否包含鍵為'Cecil'的項。相比於檢查列表是否包含指定的值，檢查字典是否包含指定的鍵的效率更高。數據結構越大，效率差距就越大。
    print('WAng is in phonebook.')