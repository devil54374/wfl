# rectangle.py
def area(length, width):
    """计算矩形面积"""
    return length * width

def perimeter(length, width):
    """计算矩形周长"""
    return 2 * (length + width)

def is_square(length, width):
    """判断是否为正方形"""
    return length == width