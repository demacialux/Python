import requests
from bs4 import BeautifulSoup


url = 'http://www.hbmy.edu.cn/templet/default/2015-02/48670.html'
h = requests.get(url)
html = h.text.encode("latin1").decode("gbk")   
soup = BeautifulSoup(html,'html.parser')
a_list = soup.find_all('a',{'class':'blak-12a'})
x = 0

for a in a_list:  
    url = a['href']  
    sc = 'http://www.hbmy.edu.cn'
    http = 'http'
    if http not in url:
        url = sc+url
        x += 1
        print('第'+ str(x) +'人')
        print(a.get_text())
    else:
        pass

    h = requests.get(url)
    html = h.text.encode("latin1").decode("gbk")    
    soup = BeautifulSoup(html,'html.parser')

    for b in soup.find_all('font',color='#333399'):
        name = b.get_text()
        print(name)
    for a in soup.find_all('td',colspan='2'):  
        person = a.get_text()
        print(person.replace(' ',''))
