import requests
from pyquery import PyQuery as pq

def get_page(url):
    headers ={
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    html = requests.get(url,headers=headers).text
    doc = pq(html)
    items = doc('.zu-main-content .zm-item').items()  #选择所有的zm-item标签
    return items

def parse_page(items):
    for item in items:
            question = item.find('h2').text()
            author = item.find('.author-link-line').text()
            answer = pq(item.find('.content').html()).text()
            
            file = open('知乎.txt','a',encoding='utf-8')
            file.write('\n'.join([question,author,answer]))
            file.write('\n' + '=' * 50 + '\n')
            file.close()

def main(p):
    url = 'https://www.zhihu.com/collection/43262308?page=' + str(p)
    items = get_page(url)
    parse_page(items)

if __name__ == '__main__':
    for i in range(28):
        print('第' + str(i) + '页')
        main(i)