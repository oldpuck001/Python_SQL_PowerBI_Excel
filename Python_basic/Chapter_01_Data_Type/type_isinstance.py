# type_isinstance.py

import pandas as pd

def data_type_isinstance_true_no(data):

    return(isinstance(data, (str, int, float)))

def data_type_isinstance(data):

    if isinstance(data, str):
        data_type = 'str'
    elif isinstance(data, int):
        data_type = 'int'
    elif isinstance(data, float):
        data_type = 'float'
    elif isinstance(data, list):
        data_type = 'list'
    elif isinstance(data, tuple):
        data_type = 'tuple'
    elif isinstance(data, dict):
        data_type = 'dict'
    elif isinstance(data, set):
        data_type = 'set'
    elif isinstance(data, pd.DataFrame):
        data_type = 'DataFrame'
    else:
        data_type = f'other: {type(data)}'

    return data_type

class MyClass:
    pass


df = pd.DataFrame()
data = ['3', 3, 3.14, [1,2,3], (1,2,3), {'a':1,'b':2,'c':3}, {1,2,3}, df]

for n in data:
    print(n)
    print(data_type_isinstance_true_no(n))
    print(data_type_isinstance(n))


# 檢查是否是某個類的實例
obj = MyClass()
print(f'obj: {isinstance(obj, MyClass)}')