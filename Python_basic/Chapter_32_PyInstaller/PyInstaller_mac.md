PyInstaller_mac.md


適合：
CLI 工具
Tkinter / PyQt / wxPython GUI
想快速產出 .app 或單一執行檔


安裝

pip install pyinstaller


封裝成 macOS App

pyinstaller --windowed --onefile your_script.py

參數	          說明
--windowed	     不顯示 Terminal（GUI 必備）
--onefile	     產生單一執行檔
--icon xxx.icns	 指定 App 圖示
--name MyApp	 App 名稱


產出位置：
dist/MyApp.app


優點
文件多、踩雷案例最多 → 容易解決問題
支援 Apple Silicon / Intel
對 Tkinter 支援穩定（你目前用 Tkinter，很合適）


缺點
打包檔案偏大（50～100MB 正常）
macOS Gatekeeper 需要額外處理（後面說）