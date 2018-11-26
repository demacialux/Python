import requests
from bs4 import BeautifulSoup

url = 'http://www.hbmy.edu.cn/templet/default/2015-02/48670.html'
a = requests.get(url)
html = a.text.encode("latin1").decode("gbk")  #解决gb2312乱码问题
soup = BeautifulSoup(html,'html.parser')
a_list = soup.find_all('a', attrs={'class':'blak-12a'})  #找到带有‘a’标签并且参数包含" class = '' "的HTML代码

for a in a_list:  #把“a”标签里面“href”参数的值提取出来
    url = a['href']
    sc = 'http://www.hbmy.edu.cn'
    http = 'http'
    if http not in url:
        url = sc+url
    else:
        pass
    name = a.get_text()
    n = name+'  '+url
    
    print(n)