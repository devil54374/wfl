import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
# 1. 设置全局中文支持
plt.rcParams['font.family'] = 'SimSun'  # 宋体
plt.rcParams['axes.unicode_minus'] = False

# 文件路径
data_dir = 'D:\\myproject_student\\pythonProject2\\day3\\city'
files = {
    '2015': os.path.join(data_dir, '2015年国内主要城市年度数据.csv'),
    '2016': os.path.join(data_dir, '2016年国内主要城市年度数据.csv'),
    '2017': os.path.join(data_dir, '2017年国内主要城市年度数据.csv'),
}

# 读取数据
dfs = {year: pd.read_csv(path, encoding='utf-8-sig') for year, path in files.items()}

# 以2015年城市顺序为基准
cities = dfs['2015']['地区']
x = np.arange(len(cities))
width = 0.25

plt.figure(figsize=(18, 7))
plt.bar(x - width, dfs['2015']['国内生产总值'], width, label='2015年')
plt.bar(x, dfs['2016']['国内生产总值'], width, label='2016年')
plt.bar(x + width, dfs['2017']['国内生产总值'], width, label='2017年')

plt.xlabel('城市')
plt.ylabel('国内生产总值（亿元）')
plt.title('2015-2017年各城市GDP柱状图')
plt.xticks(x, cities, rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

# 饼状图：2015年各城市GDP占比
df2015 = dfs['2015']
plt.figure(figsize=(8, 8))
# 只显示GDP前10的城市，其余合并为“其他”
top10 = df2015.nlargest(10, '国内生产总值')
others = df2015['国内生产总值'].sum() - top10['国内生产总值'].sum()
labels = list(top10['地区']) + ['其他']
sizes = list(top10['国内生产总值']) + [others]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('2015年各城市GDP占比（前10城市）')
plt.tight_layout()
plt.show()