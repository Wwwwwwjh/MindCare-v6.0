import pandas as pd
import math
import matplotlib.pyplot as plt
import os
import numpy as np



def mpl1(n1, n2, n3, n4, n5):
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
    plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

    labels = ['情绪认知', '人际交往', '视听感知', '反应速度', '自我认知']
    values = [n1, n2, n3, n4, n5]  # 数值范围建议 0-100
    #生成极坐标图
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]
    values += values[:1]
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    ax.plot(angles, values, color='red', linewidth=2, label='能力值')
    ax.fill(angles, values, color='red', alpha=0.25)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=15)
    ax.set_rlabel_position(0)
    ax.set_ylim(0, 100)
    ax.set_facecolor('lightblue')  # 修改背景颜色为浅蓝色
    plt.title('各项能力指标')
    ax.grid(True, linestyle='--', alpha=0.5, color='black')  # 修改坐标线颜色为白色
    plt.legend(loc='upper right')
    plt.savefig(fname="./testl.png", dpi=100)
    plt.show()

#mpl1(43,79,35,93,51)