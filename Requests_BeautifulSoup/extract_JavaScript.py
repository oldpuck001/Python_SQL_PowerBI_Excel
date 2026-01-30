# extract_JavaScript.py

# 抓取使用 JavaScript 的信息

import requests
import pandas as pd
import openpyxl

url = 'https://api.hahow.in/api/products/search?category=COURSE&limit=8&mixedResults=false&page=0&sort=TRENDING'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.2 Safari/605.1.15'}
response = requests.get(url, headers=headers)

if response.status_code == 200:

    data =response.json()
    products = data['data']['courseData']['products']
    course_list = []
    for product in products:
        course_data = [
                        product['title'],
                        product['averageRating'],
                        product['price'],
                        product['numSoldTickets']
                      ]
        course_list.append(course_data)

    df = pd.DataFrame(course_list, columns=['課程名稱', '評價', '價格', '購買人數'])
    df.to_excel('courses.xlsx', index=False, engine='openpyxl')
    print('Save!')


else:

    print('無法取得網頁')