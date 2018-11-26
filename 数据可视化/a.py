import requests
import urllib.request 
from bs4 import BeautifulSoup

req = urllib.request.Request('http://www.hbmy.edu.cn/templet/default/2015-02/48670.html')
res = urllib.request.urlopen(req)
h = res.read()
res.close()
h = str(h, "gbk").encode("utf8")  


r = requests.get(h)  #请求网址
html = r.content
soup = BeautifulSoup(html,'html.parser')

div_people_list = soup.find_all('a', attrs={'class':'blak-12a'})  #找到带有‘div’标签并且参数包含" class = '' "的HTML代码


for a in div_people_list:  #把“a”标签里面“href”参数的值提取出来
    url = a['href']
    name = a.get_text()
    print(name,url)
    print(type(name))


input()