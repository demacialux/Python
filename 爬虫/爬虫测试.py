import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/collection/43262308'
headers ={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
html = requests.get(url,headers=headers).text
doc = pq(html)
items = doc('.zu-main-content').items()

for item in items:
        question = item.find('h2').text()
        print(question)