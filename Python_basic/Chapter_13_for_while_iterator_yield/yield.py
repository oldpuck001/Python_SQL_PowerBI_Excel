# yield.py

# 生成器是包含yield語句的函數。
# 生成器與普通函數的差別在於，生成器不是使用return返回一個值，而是生成多個值，每次使用yield生成一個值後，函數都將停止執行，
# 等被重新喚醒後，函數將從停止的地方開始繼續執行。


# 生成器示例

nested = [[1, 2], [3, 4], [5]]

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element

for num in flatten(nested):
      print(num)

print(list(flatten(nested)))


# 生成器推導（也叫生成器表達式）示例：不同於列表推導，這裡使用的是圓括號
# 工作原理與列表推導相同，但不是創建一個列表（即不立刻執行循環），而是返回一個生成器，讓你能夠逐步執行計算。
g = ((i + 2) ** 2 for i in range(2,27))
print(next(g))


# 遞歸式生成器
# 如果要處理任意層嵌套的列表，可能使用列表來表示樹結構（也可以使用特定的樹類，但策略是相同的）
# 對於每層嵌套，都需要一個for循環，但由於不知道有多少層嵌套，可以使用遞歸的方法，使其更加靈活
# 在函數flatten_recursion中，不應該對類似於字符串的對象進行迭代，對這樣的對象進行迭代會導致無窮遞歸
# 因為字符串的第一個元素是一個長度為1的字符串，而長度為1的字符串的第一個元素是字符串本身

def flatten_recursion(nested):
    try:
        for sublist in nested:
            for element in flatten_recursion(sublist):
                yield element
    except TypeError:
        yield nested

print(list(flatten_recursion([[[1],2],3,4,[5,[6,7]],8])))


# 通用生成器是一個既包含yield又包含return的函數
# 生成器中的 yield 和 return
# yield
# 用於暫停函數執行並向調用者返回一個值
# 函數可以繼續從暫停的位置執行，直到下一次遇到yield
# return
# 用於終止生成器，並可以選擇性地返回一個值
# 如果在生成器中使用了return並返回了一個值，這個值將作為StopIteration異常的參數被捕獲

def example_generator():
    yield 1
    yield 2
    return 'Generator completed'
    yield 3                         # 不會執行到這裡

gen = example_generator()

try:
    print(next(gen))                # 1
    print(next(gen))                # 2
    print(next(gen))                # 引發 StopIteration 並攜帶 "Generator completed"
except StopIteration as e:
    print(f"Generator stopped with return value: {e.value}")