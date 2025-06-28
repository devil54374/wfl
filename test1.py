x = 10
y = "10"
z = True

# 判断并输出类型
print(f"x 的值: {x}, 类型: {type(x).__name__}")  # <class 'int'> [1,4](@ref)
print(f"y 的值: '{y}', 类型: {type(y).__name__}")  # <class 'str'>
print(f"z 的值: {z}, 类型: {type(z).__name__}")  # <class 'bool'>

PI = 3.14  # 根据要求定义 π 为 3.14 [6,8](@ref)

try:
    radius = float(input("请输入圆的半径: "))  # 接收用户输入并转为浮点数
    area = PI * (radius ** 2)  # 面积公式 S = πr²
    print(f"半径为 {radius} 的圆面积为: {area:.2f}")  # 保留两位小数
except ValueError:
    print("错误: 请输入有效的数字！")  # 处理非数字输入

s = "3.14"

# 转换步骤
float_val = float(s)  # 字符串 → 浮点数 [9,10](@ref)
int_val = int(float_val)  # 浮点数 → 整数

# 输出转换结果
print(f"原始字符串: '{s}', 类型: {type(s).__name__}")
print(f"转浮点数后: {float_val}, 类型: {type(float_val).__name__}")  # 3.14 (float)
print(f"转整数后: {int_val}, 类型: {type(int_val).__name__}")  # 3 (int)