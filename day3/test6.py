import pandas as pd
import numpy as np

# 1. 创建CSV文件
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Score': [85, 92, 78, np.nan, 88],
    'Grade': ['A', 'A', 'C', 'B', 'A']
}
df = pd.DataFrame(data)
df.to_csv('students.csv', index=False)

# 2. 读取并显示前3行
students_df = pd.read_csv('students.csv')
print("📋 原始数据前3行：")
print(students_df.head(3))

# 3. 处理缺失值
score_mean = students_df['Score'].mean()
students_df['Score'] = students_df['Score'].fillna(score_mean)
students_df['Name'] = students_df['Name'].fillna("Unknown")

# 4. 保存处理结果
students_df.to_csv('students_cleaned.csv', index=False)
print("\n✨ 处理后的完整数据：")
print(students_df)
print("✅ 清洗后的数据已保存为 students_cleaned.csv")