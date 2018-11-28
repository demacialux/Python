import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#执行PAI调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:',r.status_code)

#将API响应存储在一个变量中
response_dict = r.json()  #将信息转换为一个字典
print("Total repositories:",response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']

names,plot_dicts = [],[]  #创建列表
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value':repo_dict['stargazers_count'],  #确定条形高度
        'label':repo_dict['description'],  #添加描述
        'xlink':repo_dict['html_url'],  #添加可点击的链接
        } 
    plot_dicts.append(plot_dict)

#可视化
my_style = LS('#333366',base_style=LCS)  #图表样式

my_config = pygal.Config()  #创建实例
my_config.x_label_rotation = 45  #让标签围绕x轴旋转45度
my_config.show_legend = False  #隐藏图例
my_config.title_font_size = 24  #字体设置
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15  #将较长的项目名缩短为15个字符
my_config.show_y_guides = False  #隐藏水平线
my_config.width = 1000  #自定义宽度

chart = pygal.Bar(my_config,style=my_style)  #创建条形图
chart.title = 'Most - Starred Python Projects on Github'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')