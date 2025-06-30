import numpy as np
import matplotlib.pyplot as plt

# 1. 生成数据
x = np.linspace(-5, 5, 500)  # 在[-5, 5]区间生成500个均匀点
y = x**3  # 计算立方值

# 2. 创建画布和坐标轴
plt.figure(figsize=(8, 6), facecolor='#f8f9fa')  # 设置画布大小和背景色
ax = plt.axes()
ax.set_facecolor('#ffffff')  # 坐标轴区域背景色

# 3. 绘制函数曲线
plt.plot(x, y,
         color='#1f77b4',  # 曲线颜色（Matplotlib默认蓝色）
         linewidth=2.5,
         linestyle='-',
         label=r'$y = x^3$')  # 使用LaTeX公式

# 4. 设置坐标轴和标签
plt.axhline(y=0, color='k', linewidth=0.8)  # 绘制x轴
plt.axvline(x=0, color='k', linewidth=0.8)  # 绘制y轴
plt.title('$y = x^3$', fontsize=14, pad=15)  # 标题
plt.xlabel('x', fontsize=12)  # x轴标签
plt.ylabel('y', fontsize=12)  # y轴标签

# 5. 添加辅助元素
plt.grid(True, linestyle='--', alpha=0.6)  # 网格线（虚线，半透明）
plt.legend(loc='upper left', frameon=True, shadow=True)  # 带阴影的图例

# 6. 设置坐标范围
plt.xlim(-5.5, 5.5)
plt.ylim(-130, 130)

# 7. 高亮关键点
plt.scatter([-2, 0, 2], [-8, 0, 8],  # 标记(-2,-8), (0,0), (2,8)
            color='red',
            s=50,
            zorder=5,
            label='关键点')

# 8. 显示图像
plt.tight_layout()  # 自动调整布局
plt.show()


year = np.arange(2000,2021).astype(np.str_)
month = np.random.randint(1,13,size =20).astype(np.str_)
day = np.random.randint(1,31,size = 20).astype(np.str_)
date = np.array([])
for i in range(20):
    a = np.array([year[i], month[i], day[i]])
    b = ['/'.join(a)]  # 组合年月日
    date = np.append(date, b)

# 随机出销最
sales =np.random.randint(500,2000,size=len(date))
#绘制图形
plt.xticks(range(0,len(date),2),['日期:%s'%i for i in date][::2],rotation=45, color='red')
plt.plot(date, sales)
plt.show()