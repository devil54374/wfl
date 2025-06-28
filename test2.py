# 输出1到100之间的所有素数
for num in range(2, 101):  # 从2开始，因为1不是素数
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # 只需检查到sqrt(num)即可
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


# 计算斐波那契数列的前20项
fib_sequence = [0, 1]  # 初始化前两项
for _ in range(18):  # 迭代18次以得到前20项
    next_fib = fib_sequence[-1] + fib_sequence[-2]  # 计算下一项
    fib_sequence.append(next_fib)  # 将下一项添加到列表中

print(fib_sequence)


# 使用 while 循环计算满足条件的数的和
total_sum = 0
num = 1

while num <= 10000:
    if (num % 3 == 0) or (num % 5 == 0 and num % 15 != 0):
        total_sum += num
    num += 1

print(total_sum)