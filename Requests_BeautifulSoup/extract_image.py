# extract_image.py

# 抓取圖片

import requests
from bs4 import BeautifulSoup
import os


def download_img(url, save_path):

    print(f'downloading:{url}')
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.2 Safari/605.1.15'}
    cookies = {'over18': '1'}
    response = requests.get(url, headers=headers, cookies=cookies)
    with open(save_path, 'wb') as file:
        file.write(response.content)
        print('-' * 30)


def main():

    url = 'https://www.ptt.cc/bbs/Beauty/M.1716736764.A.95F.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.2 Safari/605.1.15'}
    headers = {'Cookie': 'over18=1'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    spans = soup.find_all('span', class_='article-meta-value')
    title = spans[2].text

    # 1. 建立一個圖片資料夾
    dir_name = f'images/{title}'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # 2. 找到網頁中所有的圖片
    links = soup.find_all('a')
    allow_file_name = ['jpg', 'png', 'jpeg', 'gif']
    for link in links:
        href = link.get('href')
        if not href:
            continue
    file_name = href.split('/')[-1]
    extension = href.split('.')[-1].lower()

    if extension in allow_file_name:
        print(f'file type:{extension}')
        print(f'url: {href}')
        download_img(href, f'{dir_name}/{file_name}')

# 3. 如過是圖片的話則下載
if __name__ == '__main__':
    main()