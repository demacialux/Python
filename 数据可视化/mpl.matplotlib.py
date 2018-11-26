import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_values,squares,linewidth=5)  #线条的粗细

#设置图标标题，并给坐标轴加上标签
plt.title('Square Numbers',fontsize=24)  #图标标题和文字大小
plt.xlabel('Value',fontsize=14)  #x轴标题
plt.ylabel('Square of Value',fontsize=14)  #y轴标题
plt.tick_params(axis='both',labelsize=14)  #设置刻度的样式和标记的大小

plt.show()