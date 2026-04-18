subprocess.md

subprocess模塊是Python提供的一個強大的工具，用於在程序中創建和管理子進程，允許你從Python代碼中執行操作系統命令或外部程序。

核心功能
1.執行系統命令：
   你可以通過subprocess.run()或其他方法來執行系統命令，並捕獲輸出、錯誤信息等。

2.與子進程交互：
   可以使用管道與子進程進行交互，例如向子進程提供輸入或獲取子進程的輸出。

3.替代舊模塊：
   替代了舊的模塊（例如os.system、os.spawn*），提供更靈活和安全的子進程管理方式。


常用方法和參數

1. subprocess.run()
用於執行命令並等待完成（推薦使用）。

import subprocess

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)                                                    # 輸出命令的執行結果

常用參數：
args：要執行的命令及其參數（列表或字符串）。
capture_output：是否捕獲標準輸出和標準錯誤。
text：設置為True時，自動將字節輸出解碼為字符串。
check：設置為True時，如果命令執行失敗，則引發異常。

2. subprocess.Popen
提供更低層次的接口，用於創建子進程並進行詳細控制。

import subprocess

process = subprocess.Popen(['ping', '-c', '4', 'google.com'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()                                  # 與子進程交互
print(stdout.decode())                                                  # 解碼並輸出標準輸出

3. subprocess.call
執行命令，返回命令的退出碼（不推薦，已被run()替代）。

import subprocess

exit_code = subprocess.call(['echo', 'Hello, World!'])
print('Exit code:', exit_code)

4. subprocess.check_output
執行命令並返回其輸出。

import subprocess

output = subprocess.check_output(['echo', 'Hello, World!'], text=True)
print(output)


例子：根據操作系統執行不同命令

import subprocess
import platform

if platform.system() == 'Windows':
    subprocess.run(['dir'], shell=True)
else:
    subprocess.run(['ls', '-l'])


使用注意
1. 安全性：
   避免直接拼接字符串構建命令，應使用列表格式（例如['ls', '-l']），以防止命令注入風險。

2. 異常處理：
   配合try-except捕獲執行過程中的異常，如subprocess.CalledProcessError。

3. 跨平台支持：
   注意不同操作系統上命令的差異，避免執行無效的命令。

subprocess是處理外部進程的核心工具，適合需要精細控制或與外部程序進行交互的場景。