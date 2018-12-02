import requests
from bs4 import BeautifulSoup


url = 'https://news.sina.com.cn/world/'
r = requests.get(url)
html = r.text.encode("latin1").decode("utf-8")
soup = BeautifulSoup(html,'html.parser')

for news in  soup.find_all('a',target='_blank'):
    if news in soup.find_all('a',{'class':'img'}):
        pass
    elif '详细' == news.get_text():
        pass
    elif '更多' == news.get_text():
        pass
    else:
        title = news.get_text()
        line = news.get('href')
        title_lines = title.strip() +' ' + line
        print(title_lines)
        
