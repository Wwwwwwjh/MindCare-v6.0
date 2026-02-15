import numpy as np
import pandas as pd

# 生成时间序列
time = pd.date_range("2025-03-09 10:00", periods=30, freq="min")

# 生成心率数据（正态分布+随机游走）
heart_base = np.random.normal(loc=75, scale=3, size=30)
heart_trend = np.cumsum(np.random.uniform(-0.5, 0.5, 30))
heart_rate = np.clip(heart_base + heart_trend, 60, 90).astype(int)

# 生成压力数据（泊松分布+时间递增+脉冲）
stress_base = np.random.poisson(lam=5, size=30)
stress_trend = np.linspace(40, 70, 30)
stress_pulse = np.random.choice([0, 15], 30, p=[0.85, 0.15])
stress_level = np.clip(stress_base + stress_trend + stress_pulse, 40, 85)
print(pd.DataFrame({
    '心率统计': [heart_rate.min(), heart_rate.max(), heart_rate.mean()],
    '压力统计': [stress_level.min(), stress_level.max(), stress_level.mean()]
}, index=['最小值', '最大值', '均值']))

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
plt.figure(figsize=(14, 7), facecolor='#FAFAFA')
ax = plt.gca()

# 绘制双轴折线图
ax.plot(time, heart_rate,
        color=(255/255, 60/255, 175/255),
        linewidth=2.5,
        marker='D',
        markersize=8,
        markeredgecolor='white',
        label='心率 (bpm)')

ax2 = ax.twinx()  # 创建第二个Y轴
ax2.plot(time, stress_level,
         color=(50/255, 120/255, 230/255),
         linewidth=2.5,
         linestyle='-.',
         marker='X',
         markersize=8,
         markeredgecolor='white',
         label='压力指数')

# 高级样式配置
date_format = DateFormatter("%H:%M")
ax.xaxis.set_major_formatter(date_format)
ax.set_ylabel('心率 (bpm)', fontsize=12, fontweight='bold')
ax2.set_ylabel('压力指数', fontsize=12, fontweight='bold')
plt.title('30分钟生理指标动态监测 - '+time[0].strftime("%Y-%m-%d"),
         fontsize=14, pad=20, fontweight='bold')

# 网格与装饰线
ax.grid(True, linestyle='--', alpha=0.5, axis='y')
ax.axhline(y=80, color='#FF6B6B', linestyle=':', linewidth=1.5)  # 心率警戒线
ax2.axhline(y=75, color='#4ECDC4', linestyle=':', linewidth=1.5)  # 压力警戒线

# 图例与注释
lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines + lines2, labels + labels2,
         loc='upper center',
         ncol=2,
         frameon=False,
         bbox_to_anchor=(0.5, -0.15))

plt.tight_layout()
plt.show()

import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=time, y=heart_rate, name='心率',
                         line=dict(color='rgb(255,60,175)', width=2)))
fig.add_trace(go.Scatter(x=time, y=stress_level, name='压力',
                         yaxis='y2',
                         line=dict(color='rgb(50,120,230)', width=2)))
fig.update_layout(title='交互式生理指标监测图',
                 yaxis2=dict(overlaying='y', side='right'))
fig.show()