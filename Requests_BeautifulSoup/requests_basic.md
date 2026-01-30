requests_basic.md


requests 庫是 Python 中最流行的 HTTP 客戶端之一，用於發送所有類型的 HTTP 請求。它以其簡單性、易用性和強大的功能而聞名。以下是 requests 庫一些主要功能：

1. 簡單的請求：發送各種 HTTP 請求（如 GET, POST, PUT, DELETE等）非常簡單。

```python
response = requests.get('<https://api.example.com>')
```

2. 傳遞參數：輕鬆傳遞 URL 參數和 POST 數據。

```python
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('<https://api.example.com>', data=payload)
```

3. 定製頭部：支持自定義請求頭。

```python
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, headers=headers)
```

4. 響應處理：方便地訪問響應數據，如文本、JSON、二進制數據。

```python
json_response = response.json()
```

5. Cookies: 自動處理服務器 Cookies，並允許自定義 Cookies。

```python
cookies = dict(cookies_are='working')
response = requests.get(url, cookies=cookies)
```

6. 會話對象：使用會話對象進行持久連結。

```python
with requests.Session() as session:
    session.post('<https://api.example.com>', data=payload)
```

7. SSL證書驗證：支持 SSL 證書驗證，也可以禁用驗證。

```python
response = requests.get('<https://api.example.com>', verify=False)
```

8. 超時：可以設置請求的超時時間。

```python
response = requests.get('<https://api.example.com>', timeout=5)
```

9. 重定向和請求歷史：自動處理 HTTP 重定向，並可以訪問重定向歷史。

```python
response = requests.get('<https://api.example.com>')
history = response.history
```

10. 錯誤和異常處理：提供了詳細的錯誤和異常處理機制

這些功能使得 requests 非常適合於各種不同的網絡請求場景，從簡單的數據獲取到複雜的 RESTful API 交互。由於其簡潔和強大的功能，requests 成為了 Python 中處理 HTTP 請求的首選庫。