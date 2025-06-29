import numpy as np

# 创建3x4二维数组（1-12整数）
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# 任务1：打印数组属性
print("1. 数组属性：")
print(f"形状(shape): {arr.shape}")      # 输出: (3, 4)
print(f"维度(ndim): {arr.ndim}")       # 输出: 2
print(f"数据类型(dtype): {arr.dtype}")  # 输出: int32/int64

# 任务2：元素乘以2
arr_doubled = arr * 2
print("\n2. 元素乘以2后的数组：")
print(arr_doubled)


# 任务3：重塑为4x3
arr_reshaped = arr.reshape(4, 3)
print("\n3. 重塑为4x3的数组：")
print(arr_reshaped)



import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

print("原始数组:")
print(array)

# 任务1: 提取第2行所有元素（索引1）
print("\n1. 第2行所有元素:")
print(array[1])  # 输出: [5 6 7 8]

# 任务2: 提取第3列所有元素（索引2）
print("\n2. 第3列所有元素:")
print(array[:, 2])  # 输出: [ 3  7 11 15]

# 任务3: 提取子数组（包含第1、2行和第2、3列）
print("\n3. 子数组（第1-2行，第2-3列）:")
print(array[:2, 1:3])  # 输出: [[2 3] [6 7]]

# 任务4: 将大于10的元素替换为0并打印修改后的数组
modified_array = np.where(array > 10, 0, array)
print("\n4. 修改后的数组（>10的元素替换为0）:")
print(modified_array)



import numpy as np

# 创建数组
A = np.array([[1, 2], [3, 4], [5, 6]])  # 3x2 二维数组
B = np.array([10, 20])                   # 一维数组

# 任务1: 逐元素相加（广播机制）
add_result = A + B
"""
广播过程：
A.shape = (3, 2)
B.shape = (2,) → 补齐为 (1, 2) → 复制为 (3, 2)
计算逻辑：
[[1+10, 2+20],
 [3+10, 4+20],
 [5+10, 6+20]]
"""
print("1. A + B =\n", add_result)

# 任务2: 逐元素相乘（广播机制）
mul_result = A * B
"""
广播过程同任务1
计算逻辑：
[[1 * 10, 2 * 20],
 [3 * 10, 4 * 20],
 [5 * 10, 6 * 20]]
"""
print("\n2. A * B =\n", mul_result)

# 任务3: 每行与B的点积
dot_result = np.dot(A, B)  # 等效于 A @ B
"""
数学原理：
点积 = 行向量与B的线性组合
计算过程：
行0: 1 * 10 + 2 * 20 = 50
行1: 3 * 10 + 4 * 20 = 110
行2: 5 * 10 + 6 * 20 = 170
"""
print("\n3. A每行与B的点积 =\n", dot_result)