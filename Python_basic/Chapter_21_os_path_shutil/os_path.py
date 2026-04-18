# os_path.py

import os

targetPath_1 = '/Users/lei/Downloads/自动改名程序'
targetPath_2 = '/Users/lei/Downloads/del'
targetPath_3 = '/Users/lei/Downloads/'
targetPath_5 = '/Users/lei/Downloads/a.txt'
targetPath_6 = '/Users/lei/Downloads/c.txt'
targetPath_7 = '/Users/lei/Downloads/d.txt'

# os.walk()會從指定的根目錄開始，逐層地走訪子目錄，並在每一層產出一個三元組 (dirpath, dirnames, filenames)
for root, dirs, files in os.walk(targetPath_3):
    print(root, dirs, files)


# 检查路径是否存在
if os.path.exists(targetPath_1):
    print(f"目标路径'{targetPath_1}'已存在。")
else:
    # 安全地创建目录，即使目录已存在
    os.makedirs(targetPath_1, exist_ok=True)


# 检查路径是否是目錄
if os.path.isdir(targetPath_2):
    print(f"目标路径'{targetPath_2}'是文件夾。")


# 指定目錄中的所有文件和目錄名的列表
sorted_list = sorted(os.listdir(targetPath_3))
print(sorted_list)


# os.path.basename()取得路徑中的文件名（或最後一層目錄名稱）
print(os.path.basename(targetPath_2))
print(os.path.basename(targetPath_3))
print(os.path.basename(targetPath_5))


# 合并路径
targetPath_4 = os.path.join(targetPath_3, 'a')
os.makedirs(targetPath_4, exist_ok=True)


# 返回给定路径的上级目录
print(os.path.dirname(targetPath_1))


# 獲取當前腳本所在的目錄
print(os.path.dirname(os.path.abspath(__file__)))


# 將檔案路徑分成兩部分
head, tail = os.path.split(targetPath_5)
print('Head:', head)
print('Tail:', tail)

split_path = os.path.split(targetPath_5)
print('Head:', split_path[0])
print('Tail:', split_path[1])


# 修改文件名
os.rename(targetPath_6, targetPath_7)