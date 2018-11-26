import pygal
from die import Die

die_1 = Die()  #创建两个D6
die_2 = Die()  

#掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(10000):
    result = die_1.roll()+die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = [str(value for value in range(2,max_result+1))]  #列表解析，并转换为字符串       
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6',frequencies)
hist.render_to_file('die_visual.svg')