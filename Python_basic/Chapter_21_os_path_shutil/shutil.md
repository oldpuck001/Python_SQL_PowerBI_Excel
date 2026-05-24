shutil.md

shutil是Python標準庫中的一個模組，全名是“shell utilities”，主要用來高階檔案操作與目錄處理，是os模組的進階補充。


常見功能一覽：

功能                                                 說明
shutil.copy(src, dst)                               複製檔案，保留內容但不保留權限
shutil.copy2(src, dst)                              複製檔案，保留內容與metadata（如修改時間）
shutil.copyfile(src, dst)                           僅複製檔案內容，不建立目標目錄
shutil.move(src, dst)                               搬移檔案或目錄
shutil.rmtree(path)	                                遞迴刪除整個目錄樹


使用場景：
自動備份檔案
建立安裝包或壓縮包
整理或同步資料夾結構
批次移動或刪除檔案與目錄