# extract_txt.py


import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

# header
url = 'https://www.ptt.cc/bbs/NBA/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.2 Safari/605.1.15',
           'Accept': 'text/html'}
cookies = {'over18': '1'}

# 發出HTTP請求
response = requests.get(url, headers=headers, cookies=cookies)

if response.status_code == 200:                             # 確認請求成功

    # 導出為html文件
    with open('output.html', 'w', encoding = 'utf-8') as f:
        f.write(response.text)

    # 解析 HTML 內容
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.find_all('div', class_ = 'r-ent')

    data_list = []

    for a in articles:

        data = {}

        title = a.find('div', class_='title')
        if title and title.a:
            title = title.a.text
        else:
            title = 'No title'
        data['Title'] = title

        popular = a.find('div',class_='nrec')
        if popular and popular.span:
            popular = popular.span.text
        else:
            popular = 'N/A'
        data['Popular'] = popular

        date = a.find('div', class_='date')
        if date:
            date = date.text
        else:
            date = 'N/A'
        data['Date'] = date

        data_list.append(data)
        
    with open('ptt_nba_data.json', 'w', encoding='utf-8') as file:
        json.dump(data_list, file, ensure_ascii=False,indent=4)

    df = pd.DataFrame(data_list)
    df.to_excel('ptt_nba.xlsx', index=False, engine='openpyxl')
    print(' ')


else:
        print('Error: Unable to fetch the web page.')