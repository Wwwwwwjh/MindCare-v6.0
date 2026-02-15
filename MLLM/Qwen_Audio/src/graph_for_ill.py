import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 用于正常显示中文
plt.rcParams['font.sans-serif'] = 'SimSun'
# 用于正常显示符号
plt.rcParams['axes.unicode_minus'] = False
# 构造数据
mydata = pd.DataFrame({'疾病': ['自闭症','非典型孤独症', '脆性X综合征', '雷特综合征', '语言发育障碍'],
                       '概率': [60, 30, 25, 20, 46]})
fig = plt.figure()
ax1 = fig.add_subplot(111)
max_index = np.argmax(mydata['概率'])

# 绘制柱状图，并将最大值的颜色设置为红色
ax1.bar(mydata['疾病'], mydata['概率'], width=0.5, align='center', color=['red' if i == max_index else 'lightblue' for i in range(len(mydata))])

for i, v in enumerate(mydata['概率']):
    ax1.text(i, v + 1, str(v), ha='center', va='bottom', fontsize=15)


# 设置图形背景颜色
# fig.patch.set_facecolor('yellow')
# plt.title('可能病症', fontsize=20, color='black')
plt.savefig('plot/ill_1.jpg', format='jpg')
plt.show()
