SSL_fail.md

SSL 證書驗證失敗的解決辦法


本地的 Python 環境缺少了必要的 SSL 證書，會發生由於 SSL 證書驗證失敗引起的錯誤。在macOS 喝一些 Linux 發行版上，這個問題可能會比較常見。以下是解決這個問題的一些方法：


## 方法一：更新證書（macOS）

如果使用的是macOS，可以使用以下命令來更新證書：

```python
/Applications/Python\\ 3.x/Install\\ Certificates.command
```

請將 3.x 替換為您的 Python 版本。


## 方法二：手動安裝證書（適用於所有操作系統）

可以手動安裝SSL證書。以下是具體不周：

1. 下載證書文件：可以從 Certifi 官網獲取證書。

2. 編寫代碼來使用下載的證書：

```python
import ssl
import certifi
from pytube import YouTube

def download_video(url, path):

    try:

        # 創建 YouTube SSL 對象，並設置 SSL 上下文
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        yt = YouTube(url, ssl_context=ssl_context)

        # 獲取最高解析度的視頻
        video = yt.streams.get_highest_resolution()

        # 下載視頻
        video.download(output_path=path)
        print('下載完成')

    except Exception as e:

        print(f'發生錯誤: {e}')

# 視頻URL
video_url = '這裡填入 YouTube 視頻的 URL'

# 下載目錄
download_path = '這裡填入想要的保存視頻的路徑'

download_video(video_url, download_path)
```


## 方法三：禁用SSL驗證（不推薦）

禁用SSL驗證並不是一個推薦的做法，因為這會降低安全性。但在某些情況下，為了臨時測試，可以這樣做：

```python
import ssl
from pytube import YouTube

def download_video(url, path):

    try:

        # 創建YouTube SSL對象，並禁用SSL驗證
        yt = YouTube(url, ssl._create_unverified_context())

        # 獲取最高解析度的視頻
        video = yt.streams.get_highest_resolution()

        # 下載視頻
        video.download(output_path=path)
        print('下載完成')

    except Exception as e:

        print(f" : {e}")

    # 視頻URL
    video_url = '這裡填入YouTube視頻的URL'

    # 下載目錄
    download_path = '這裡填入想要保存視頻的路徑'

    download_video(video_url, download_path)
```

請注意，這種方法應該只在測試環境下使用，不應在生產環境中使用，因為它會降低應用程序的安全性。