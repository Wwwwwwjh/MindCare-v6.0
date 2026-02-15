# Libraries
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

from numpy import size

# Set data
# 用于正常显示中文
plt.rcParams['font.sans-serif'] = 'SimSun'
# 用于正常显示符号
plt.rcParams['axes.unicode_minus'] = False

plt.style.use('ggplot')

# 构造数据
values = [37, 57, 69, 42, 80]
values = np.concatenate((values, [values[0]]))
feature = ['交往', '躯体和物体使用', '语言', '社会生活自理', '感觉']
feature = np.concatenate((feature, [feature[0]]))

# 设置每个数据点的显示位置，在雷达图上用角度表示
angles = np.linspace(0, 2 * np.pi, 5, endpoint=False)
angles = np.concatenate((angles, [angles[0]]))

# 绘图
fig = plt.figure()
# 设置为极坐标格式
ax = fig.add_subplot(111, polar=True)
# 绘制折线图
ax.plot(angles, values, 'o-', linewidth=1)
# 填充颜色
ax.fill(angles, values, alpha=0.5, color='red')

# 设置图标上的角度划分刻度，为每个数据点处添加标签
ax.set_thetagrids(angles * 180 / np.pi, feature)
# 设置刻度数字的大小
ax.tick_params(labelsize=15)

# 设置雷达图的范围
ax.set_ylim(0, 100)
# 添加标题
# plt.title('各项能力指标', fontsize=20)
# 添加网格线
ax.grid(True)

# 设置刻度颜色
ax.tick_params(axis='x', colors='red', labelsize=20)
# 设置极坐标背景颜色
ax.set_facecolor('lightblue')
# 设置图形背景颜色
# fig.patch.set_facecolor('yellow')

plt.savefig('plot/ability_1.jpg', format='jpg')
plt.show()



