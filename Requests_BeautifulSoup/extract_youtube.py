# extract_youtube.py

# 抓取 YouTube 音視頻

# 要使用 Python 抓取 YouTube 視頻，可以利用 pytube 這個第三方庫。pytube 是一個非常簡單易用的庫，用來下載 Youtube 視頻和提取音頻。

# 安裝 pytube 庫的指令
# pip install pytube

from pytube import YouTube

def download_video(url, path):

    try:
        # 創建 YouTube 對象
        yt = YouTube(url)

        # 獲取最高解析度的視頻
        video = yt.streams.get_highest_resolution()

        #下載視頻
        video.download(output_path=path)
        print('下載完成')

    except Exception as e:

        print(f'發生錯誤: {e}')

# 視頻URL
video_url = 'https://www.youtube.com/watch?v=mZ7nvDwhLj4'

# 下載目錄
download_path = '/Users/lei/Downloads'

download_video(video_url, download_path)

# 在使用這類工具下載 Youtube 視頻時，需要遵守 Youtube 的使用條款以及相關的版權法律，確保不違反內容創作者的權益。

# YouTube 經常更換影片簽名與 JS 加密方式，pytube 近年來跟不上 YouTube，改用 yt-dlp，這是目前業界標準