# try_except.py

x = 5
y = 'aaa'

# 如果要使用一個except子句捕獲多種異常，可在一個元組中指定這些異常.
# 如果有多個except代碼塊，異常類型的順序非常重要，Python會從上到下依次檢查每個except代碼塊的異常類型，直到找到第一個匹配的異常類型為止。
# 要在except子句中訪問異常對象本身，可使用兩個而不是一個參數。在大多數情況下，可以使用except Exception as e並對異常對象進行檢查。
# 如果想要使用一段代碼捕獲所有的異常，只需在except語句中不指定任何異常類即可。即：except: 
# 像這樣捕獲所有的異常很危險，因為這不僅會隱藏你有心理準備的錯誤，還會隱藏你沒有考慮過的錯誤。

try:
    print(x / y)                     # 可能出現異常的代碼

except AttributeError as e:          # 引用属性或给它赋值失败时引发
    print('Exception: AttributeError')
    print(e)

except OSError as e:                 # 操作系统不能执行指定的任务(如打开文件)时引发，有多个子类
    print('Exception: OSError')
    print(e)

except IndexError as e:              # 使用序列中不存在的索引时引发，为LookupError的子类
    print('Exception: IndexError')
    print(e)

except KeyError as e:                # 使用映射中不存在的键时引发，为LookupError的子类
    print('Exception: KeyError')
    print(e)

except NameError as e:               # 找不到名称（变量）时引发
    print('Exception: NameError')
    print(e)

except SyntaxError as e:             # 代码不正确时引发
    print('Exception: SyntaxError')
    print(e)

except TypeError as e:               # 将内置操作或函数用于类型不正确的对象时引发
    print('Exception: TypeError')
    print(e)

except ValueError as e:              # 将内置操作或函数用于这样的对象时引发：其类型正确但包含的值不合适
    print('Exception: ValueError')
    print(e)

except ZeroDivisionError as e:       # 在除法或求模运算的第二个参数为零时引发
    print('Exception: ZeroDivisionError')
    print(e)

except:                              # 異常處理代碼3（捕捉所有異常）
    print('Other Exception')

else:                                # 當沒有異常發生時執行的代碼
    print('No Exception')

finally:                             # 無論有沒有異常發生都會執行的代碼
    print('Over!')

# 使用else结合while循环（重复获取输入值，直至参数符合要求）
while True:
    try:
        x = int(input('Enter the first number:'))
        y = int(input('Enter the second number:'))
        value = x / y
        print('x / y is', value)
    except Exception as e:
        print('Invalid input:', e)
        print('Please try again')
    else:
        break