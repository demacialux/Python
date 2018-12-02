import requests
import re
import json
from multiprocessing import Pool

def get_one_page(url):
    """获取网页"""
    r = requests.get(url)
    html = r.text
    return html

def parse_one_page(html):
    """"正则表达式分析网页"""
    result = re.compile('<h2.*?href="(.*?)".*?title="(.*?)".*?</h2>'
    +'.*?pub"(.*?)</div>.*?nums">(.*?)</span>.*?pl">(.*?)</span>.*?'
    +'<p>(.*?)</p>',re.S)
    items = re.findall(result,html)
    for item in items:
        yield{
            'link':item[0],
            'title':item[1],
            'author':item[2].split('/'),
            'comment':item[3],
            'persons':item[4],
            'short':item[5]
        }

def write_to_file(content):
    with open('豆瓣小说图书排行.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False) + '\n')

def main(s):
    """主程序"""
    url = 'https://book.douban.com/tag/小说?start='+ str(s) + '&type=S'
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    pool = Pool()
    pool.map(main,[i * 20 for i in range(10)])