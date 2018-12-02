import requests
import re
import json

url = 'https://news.qq.com/'
r = requests.get(url)
html = r.text
result = re.compile('<a.*href="(.*html)">(.{10,30})</a>')
item = re.findall(result,html)
for news in item:
    with open('腾讯新闻.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(news,ensure_ascii=False) + '\n')

print('完成')