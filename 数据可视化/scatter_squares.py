import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]  #x的平方

#c可以为颜色，使用'red'或GB自定义(0,0,0)；若使用颜色映射，则添加cmap；s为尺寸
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=40) 

#设置图标标题，并给坐标轴加上标签
plt.title('Square Numbers',fontsize=24)  #图标标题和文字大小
plt.xlabel('Value',fontsize=14)  #x轴标题
plt.ylabel('Square of Value',fontsize=14)  #y轴标题
plt.tick_params(axis='both',labelsize=14)  #设置刻度的样式和标记的大小
plt.axis([0,1100,0,1100000])  #设置每个坐标轴的取值范围

plt.savefig('squares_plot.png',bbox_inches='tight')  #自动保存图片并去除多余空白
plt.show()  #显示图片