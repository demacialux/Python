import csv
from matplotlib import pyplot as plt
from datetime import datetime

def get_weather_data(filename, dates, highs, lows):
    """收集文件名、日期、最高温和最低温"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:  #reader对象每次自动返回当前所处位置的下一行
            try:
                current_date = datetime.strptime(row[0],"%Y-%m-%d")  #日期格式转换
                high = int(row[1])  #转换为整数，最高温
                low = int(row[3])  #最低温
            except ValueError:
                pass
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

fig = plt.figure(dpi=128,figsize=(10,6))  #屏幕参数

#根据甲地数据绘制图形
dates,highs,lows = [],[],[]
get_weather_data('sitka_weather_2014.csv', dates, highs, lows)
plt.plot(dates,highs,c='red',alpha=0.6)
plt.plot(dates,lows,c='blue',alpha=0.6)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.05)  #绘图表区域填充颜色

#根据乙地数据绘制图形
dates,highs,lows = [],[],[]
get_weather_data('death_valley_2014.csv', dates, highs, lows)
plt.plot(dates,highs,c='red',alpha=0.3)
plt.plot(dates,lows,c='blue',alpha=0.3)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.15)  #绘图表区域填充颜色

#设置图形格式
plt.title("Daily high and low temperatures - 2014",fontsize=24)  #正标题
plt.xlabel('',fontsize=16)  #x轴
fig.autofmt_xdate()  #绘制斜的日期标签
plt.ylabel("temperature(F)",fontsize=16)  #y轴及轴标题
plt.tick_params(axis='both',which='major',labelsize=16)
plt.ylim(10, 120)  #设置y轴刻度范围

plt.show()  #目前日期没有以x轴原点为起点