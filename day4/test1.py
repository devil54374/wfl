import numpy as np
import matplotlib.pyplot as plt

# 1. 设置全局中文支持
plt.rcParams['font.family'] = 'SimSun'  # 宋体
plt.rcParams['axes.unicode_minus'] = False

# 国家列表修正
countries = ["那", "德国", "中国", "美国", "瑞典"]

# 奖牌数据修正
gold_medal = np.array([16, 12, 9, 8, 8])
silver_medal = np.array([8, 10, 4, 10, 5])
bronze_medal = np.array([13, 5, 2, 7, 5])  # 修正为numpy数组

x = np.arange(len(countries))

# 设置图表
plt.figure(figsize=(10, 6))
plt.bar(x - 0.2, gold_medal, width=0.2, color="gold", label="金牌")
plt.bar(x, silver_medal, width=0.2, color="silver", label="银牌")
plt.bar(x + 0.2, bronze_medal, width=0.2, color="saddlebrown", label="铜牌")

# 设置x轴标签
plt.xticks(x, countries)
plt.xlabel("国家")
plt.ylabel("奖牌数量")
plt.title("各国奖牌数量统计")
plt.legend()

# 添加数据标签
for i in range(len(x)):
    plt.text(x[i] - 0.2, gold_medal[i], gold_medal[i],
             va='bottom', ha='center', fontsize=8)
    plt.text(x[i], silver_medal[i], silver_medal[i],
             va='bottom', ha='center', fontsize=8)
    plt.text(x[i] + 0.2, bronze_medal[i], bronze_medal[i],
             va='bottom', ha='center', fontsize=8)

plt.tight_layout()
plt.show()