import pandas as pd

# 1. 读取CSV文件并转换为DataFrame
file_path = r"D:\shixun\exercise\drinks.csv"
drinks = pd.read_csv(file_path)


# 2. 问题解答
# 1. 哪个大陆平均消耗的啤酒最多？
beer_avg = drinks.groupby('continent')['beer_servings'].mean()
most_beer_continent = beer_avg.idxmax()
print(f"1. 啤酒平均消耗最多的大陆: {most_beer_continent} ({beer_avg.max():.1f}份/人)\n")

# 2. 每个大陆的红酒消耗描述性统计值
wine_stats = drinks.groupby('continent')['wine_servings'].describe()
print("2. 每个大陆红酒消耗的描述性统计值:")
print(wine_stats, "\n")

# 3. 每个大陆每种酒类别的消耗平均值
avg_consumption = drinks.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings']].mean()
print("3. 每个大陆每种酒类别的平均消耗量:")
print(avg_consumption, "\n")

# 4. 每个大陆每种酒类别的消耗中位数
median_consumption = drinks.groupby('continent')[['beer_servings', 'spirit_servings', 'wine_servings']].median()
print("4. 每个大陆每种酒类别的消耗中位数:")
print(median_consumption)