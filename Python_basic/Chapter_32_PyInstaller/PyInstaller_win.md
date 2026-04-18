PyInstaller_win.md

在Windows上把Python程序「封包（打包成可執行檔 .exe）」最常見、也最簡單的方法是用PyInstaller。下面按「實務流程」一步一步說，適合Tkinter/pandas類型的桌面工具

一、安裝PyInstaller

在命令提示字元（cmd）或PowerShell中執行：

pip install pyinstaller

確認安裝成功：

pyinstaller --version


二、基本封包（產生 exe）

假設你的主程式是：

main.py

執行：

pyinstaller main.py

產生結果：

dist/
 └─ main/
     └─ main.exe

（這是「資料夾型」exe）


三、封成「單一 exe 檔」（常用）

pyinstaller --onefile main.py

結果：

dist/
 └─ main.exe


四、Tkinter 程式

不顯示黑色命令列視窗

Tkinter GUI 程式一定要加：

pyinstaller --onefile --windowed main.py

或（等價）：

pyinstaller --onefile --noconsole main.py


五、常見進階需求

加上圖示（icon）

pyinstaller --onefile --windowed --icon=app.ico main.py

icon 必須是 `.ico` 格式


六、封包時包含資料檔（CSV / Excel / config）

例如有：

data/config.json

pyinstaller --onefile --windowed ^
  --add-data "data/config.json;data" ^
  main.py


Windows 分隔符是 `;`（不是 `:`）


七、程式中正確讀取被封包的檔案

在程式裡要這樣寫（非常重要）：

import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

config_path = resource_path("data/config.json")


八、pandas/numpy封包注意事項

你常用 pandas，我幫你列重點：

避免亂用虛擬環境

建議：
封包前用乾淨的 venv
只安裝你真的用到的套件


python -m venv venv
venv\Scripts\activate
pip install pandas openpyxl pyinstaller


九、若出現「模組找不到」

pyinstaller --onefile --hidden-import=pandas._libs.tslibs.timedeltas main.py

（通常 pandas 才會遇到）


十、Spec 檔（進階、可控性最高）

先產生 spec

pyinstaller main.py

會產生：

main.spec

之後用：

pyinstaller main.spec

適合大型 Tkinter + pandas 專案


十一、其他封包工具（簡要比較）

| 工具             | 適合          | 備註    |
| --------------- | ------------- | ------ |
| PyInstaller     | 桌面程式       | 最穩定   |
| cx_Freeze       | 桌面程式       | 設定較繁 |
| Nuitka          | 效能/保護原始碼 | 編譯慢   |
| py2exe          | 舊            | 不推薦   |


十二、Tkinter + pandas 專案的「建議指令」（直接可用）

pyinstaller ^
 --onefile ^
 --windowed ^
 --icon=app.ico ^
 main.py