import requests
from bs4 import BeautifulSoup

url = 'https://news.sina.com.cn/world/'
r = requests.get(url)
html = r.text.encode("latin1").decode("utf-8")
soup = BeautifulSoup(html,'html.parser')
newsall = soup.find_all('div',{'class':'blk122'})



for new in  newsall:
    title = new.get_text()
    line = new.a['href']  #只能获取一条链接
    a = title + line
    print(a)
