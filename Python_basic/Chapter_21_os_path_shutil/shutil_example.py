# shutil_example.py

import shutil

targetPath_1 = '/Users/lei/Downloads/a.txt'
targetPath_2 = '/Users/lei/Downloads/b.txt'
targetPath_3 = '/Users/lei/Downloads/自动改名程序/a.txt'
targetPath_4 = '/Users/lei/Downloads/a'


# 複製檔案（不保留原檔權限時間）
shutil.copy( targetPath_1, targetPath_2)

# 搬移檔案或資料夾
shutil.move(targetPath_1, targetPath_3)

# 刪除整個資料夾（小心使用）
shutil.rmtree(targetPath_4)