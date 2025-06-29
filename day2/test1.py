def is_palindrome(num):
    """
    判断整数是否为回文数（数学方法）
    :param num: 待判断的整数
    :return: bool类型结果
    """
    if num < 0 or (num % 10 == 0 and num != 0):
        return False  # 负数或末尾为0的非零数直接排除[1,5](@ref)

    reversed_half = 0
    original = num

    # 进阶：仅反转数字的后半部分[1](@ref)
    while num > reversed_half:
        reversed_half = reversed_half * 10 + num % 10
        num //= 10

    # 偶数位：反转后两部分相等；奇数位：去掉中间位后相等[1](@ref)
    return num == reversed_half or num == reversed_half // 10

# 测试示例
print(is_palindrome(121))  # True
print(is_palindrome(-121))  # False
print(is_palindrome(12321))  # True


def calculate_average(*args, decimal_places=2):
    """
    计算任意数量参数的平均值
    :param args: 可变参数（支持任意数量数字）
    :param decimal_places: 结果保留小数位数（默认2位）[6,8](@ref)
    :return: 浮点数结果
    """
    if not args:
        return 0.0  # 空输入返回0.0

    total = sum(args)
    average = total / len(args)
    return round(average, decimal_places)  # 四舍五入到指定小数位[6](@ref)


# 测试示例
print(calculate_average(1, 2, 3))  # 2.0
print(calculate_average(1.5, 2.75, 3.25))  # 2.5
print(calculate_average(10, 20, 30, 40))  # 25.0


def find_longest_string(*strings):
    """
    从任意数量字符串中返回最长的一个
    :param strings: 可变字符串参数
    :return: 最长字符串（空输入返回None）
    """
    if not strings:
        return None  # 处理空输入[9](@ref)

    # 使用max的key参数按长度比较[9,10](@ref)
    return max(strings, key=len)


# 测试示例
print(find_longest_string("apple", "banana", "cherry"))  # "banana"
print(find_longest_string("cat", "dog", "bird"))  # "bird"

# main.py
from rectangle import area, perimeter, is_square


def main():
    try:
        l = float(input("输入长度: "))
        w = float(input("输入宽度: "))

        if l <= 0 or w <= 0:
            raise ValueError("尺寸必须为正数")

        print(f"面积: {area(l, w):.2f}")
        print(f"周长: {perimeter(l, w):.2f}")
        if is_square(l, w):
            print("※ 这是正方形")
    except ValueError as e:
        print(f"错误: {e}")


if __name__ == "__main__":
    main()