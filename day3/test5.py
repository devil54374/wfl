import os
import pandas as pd
from glob import glob

# 1. 读取并合并数据
folder = r"D:/myproject_student/pythonProject2/day3/city"
all_files = glob(os.path.join(folder, '*.csv'))
# 只读取2015-2017年数据文件
all_files = [f for f in all_files if '2015' in f or '2016' in f or '2017' in f]
df_list = [pd.read_csv(f, encoding='utf-8') for f in all_files]
df = pd.concat(df_list, ignore_index=True)

# 2. 处理缺省值，填充为0
fill_cols = ['国内生产总值', '医院、卫生院数', '社会商品零售总额']
for col in fill_cols:
    if col in df.columns:
        df[col] = df[col].fillna(0)

# 3. 按年份聚合，求每年国内生产总值
if '国内生产总值' in df.columns and '年份' in df.columns:
    gdp_by_year = df.groupby('年份')['国内生产总值'].sum().reset_index()
    print('每年国内生产总值:')
    print(gdp_by_year)

# 4. 计算2015-2017年各城市GDP年均增长率，找出最高和最低的五个城市
city_gdp = df[df['年份'].isin([2015,2016,2017])][['地区','年份','国内生产总值']]
city_gdp_pivot = city_gdp.pivot(index='地区', columns='年份', values='国内生产总值')
city_gdp_pivot = city_gdp_pivot.fillna(0)
city_gdp_pivot['growth_rate'] = ((city_gdp_pivot[2017] / city_gdp_pivot[2015]) ** (1/2) - 1) * 100
city_gdp_pivot = city_gdp_pivot.sort_values('growth_rate', ascending=False)
city_gdp_pivot[['growth_rate']].to_csv(os.path.join(folder, 'city_gdp_growth.csv'), encoding='utf-8-sig')
print('年均增长率最高的五个城市:')
print(city_gdp_pivot.head(5)[['growth_rate']])
print('年均增长率最低的五个城市:')
print(city_gdp_pivot.tail(5)[['growth_rate']])

# 5. 医院、卫生院数归一化（Min-Max标准化），并按年份比较
for col in ['医院、卫生院数']:
    if col in df.columns:
        df[col+'_norm'] = df.groupby('年份')[col].transform(lambda x: (x-x.min())/(x.max()-x.min()) if x.max()!=x.min() else 0)

# 6. 按年份比较各城市医疗资源变化
if '地区' in df.columns:
    med_cols = ['地区', '年份', '医院、卫生院数_norm']
    med_df = df[med_cols].drop_duplicates()
    med_df.to_csv(os.path.join(folder, 'medical_resources_normalized.csv'), index=False, encoding='utf-8-sig')
    print('各城市医疗资源归一化后变化已保存')

# 7. 提取四个城市2015-2017年GDP和社会商品零售总额，保存为新csv
cities = ['北京', '上海', '广州', '深圳']
extract_cols = ['地区', '年份', '国内生产总值', '社会商品零售总额']
city_extract = df[df['地区'].isin(cities) & df['年份'].isin([2015,2016,2017])][extract_cols]
city_extract.to_csv(os.path.join(folder, 'big4_cities_data.csv'), index=False, encoding='utf-8-sig')
print('已保存四城市2015-2017年GDP和社会商品零售总额数据到csv')
# 合并后的数据也可保存
combined_path = os.path.join(folder, 'combined_city_data.csv')
df.to_csv(combined_path, index=False, encoding='utf-8-sig')
print('合并后的全部数据已保存')

