import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. 设置全局中文支持
plt.rcParams['font.family'] = 'SimSun'  # 宋体
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv(r'D:\myproject_student\pythonProject2\day4\train.csv')

# 计算不同等级的生还率
pclass_survived = df.groupby('Pclass')['Survived'].mean()

# 绘制直方图（美化）
plt.figure(figsize=(7, 5))
bars = plt.bar(pclass_survived.index.astype(str), pclass_survived.values, color=['#4F81BD', '#C0504D', '#9BBB59'])
plt.xlabel('乘客等级（Pclass）', fontsize=12)
plt.ylabel('生还率', fontsize=12)
plt.title('乘客等级对生还率的影响', fontsize=14)
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
# 添加数值标签
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02, f'{bar.get_height():.2f}',
             ha='center', va='bottom', fontsize=11)
plt.tight_layout()
plt.show()


# 年龄分组（8组）
age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 100]
age_labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70+']
df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)

# 计算各年龄段生还率
age_survived = df.groupby('AgeGroup')['Survived'].mean()

# 绘制年龄对生还率的直方图（美化）
plt.figure(figsize=(9, 5))
bars = plt.bar(age_survived.index.astype(str), age_survived.values, color='#4F81BD')
plt.xlabel('年龄段', fontsize=12)
plt.ylabel('生还率', fontsize=12)
plt.title('年龄对生还率的影响', fontsize=14)
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
# 添加数值标签
for bar in bars:
    if not np.isnan(bar.get_height()):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02, f'{bar.get_height():.2f}',
                 ha='center', va='bottom', fontsize=11)
plt.tight_layout()
plt.show()
