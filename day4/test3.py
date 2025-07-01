import pandas as pd
import matplotlib.pyplot as plt

# 1. 设置全局中文支持
plt.rcParams['font.family'] = 'SimSun'  # 宋体
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv(r'D:\myproject_student\pythonProject2\day4\train.csv')

# 计算不同等级的生还率
pclass_survived = df.groupby('Pclass')['Survived'].mean()

# 绘制直方图
pclass_survived.plot(kind='bar')
plt.xlabel('乘客等级（Pclass）')
plt.ylabel('生还率')
plt.title('乘客等级对生还率的影响')
plt.ylim(0, 1)
plt.show()