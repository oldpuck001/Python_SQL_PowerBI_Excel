BeautifulSoup_basic.md


BeautifulSoup 是一個用於解析 HTML 喝 XML 文檔的 Python 庫，非常適用於網頁抓取。它依賴於解析器如 lxml 或 html.parser 來進行文檔解析。

Beautiful Soup網站: http://crummy.com/software/BeautifulSoup

BeautifulSoup 主要功能包括：

1. 解析HTML/XML: 能夠處理各種類型的標記，即使標記非常混亂或者不規範。

```python
soup = BeautifulSoup(html_doc, 'html.parser')
```

2. 導航標籤樹：提供了簡單的方法來訪問和修改 parse 樹中的元素。

```python
title_tag = soup.title
```

3. 搜索文件樹：支持複雜的搜索請求，如查找所有符合特定屬性的標籤。

```python
links = soup.find_all('a')
```

4. 修改和解析：可以對文檔樹進行修改，如改變標籤和屬性。

```python
tag = soup.b
tag.string = "New text"
```

5. 提取信息：容易提取所需的信息，例如標籤的屬性值。

```python
link = soup.find('a', id='link3')
```

6. 格式化輸出：將 parse 樹格式化為標準的格式輸出。

```python
pretty_html = soup.prettify()
```

7. 編碼處理：自動處理各種編碼，確保文本輸出的正確性。


8. 與解析器無關：雖然 BeautifulSoup 自身不解析文檔，但它可以與多種解析器配合使用，如 lxml、html5lib


BeautifulSoup 以其強大的解析能力和靈活的搜索功能，被廣泛用於網頁數據抓取、網頁內容提取等場景。它的易用性和功能強大使其成為 Python 網絡爬蟲領域的主要工具之一。

如過要抓取 RSS feed，可使用另一個與 Beautiful Soup 相關的工具，名為 Scrape ‘Nʼ Feed http://crummy.com/software/ScrapeNFeed