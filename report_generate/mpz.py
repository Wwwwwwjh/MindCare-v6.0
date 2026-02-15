import numpy as np
import matplotlib.pyplot as plt
import random
def mpz1(n1,n2,n3,n4,n5):
	# 准备数据
	x_data = ['焦虑','自闭症','强迫症','边缘型人格障碍','其他']
	y_data = [n1,n2,n3,n4,n5]

	# 正确显示中文和负号
	plt.rcParams["font.sans-serif"] = ["SimHei"]
	plt.rcParams["axes.unicode_minus"] = False

	# 画图，plt.bar()可以画柱状图
	for i in range(len(x_data)):
		plt.bar(x_data[i], y_data[i])
	# 设置图片名称
	plt.title("可能病症分析")
	# 设置x轴标签名
	plt.xlabel("病症")
	# 设置y轴标签名
	plt.ylabel("概率")

	plt.savefig(fname="./testz.png", dpi=100)

	# 显示
	plt.show()

#mpz1(43,79,35,93,51)     #生成坐标图社会生活自理
