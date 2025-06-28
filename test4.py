s1 = "Python is a powerful programming language"
words = s1.split()  # 按空格分割字符串为单词列表
last_word = words[-1]  # 通过索引 -1 获取最后一个单词
print(last_word)
s1 = "Python is a powerful programming language"
s2 = " Let's learn together"
combined = s1 + s2  # 拼接 s1 和 s2
print(combined * 3)  # 重复输出 3 次
s1 = "Python is a powerful programming language"
words = s1.split()
p_words = [word for word in words if word.startswith(('p', 'P'))]  # 检查开头字符
print(p_words)


s3 = " Hello, World! This is a test string. "

# (1) 去除字符串前后的空格
s3_stripped = s3.strip()
print(f"(1) 去除前后空格: '{s3_stripped}'")  # 输出: 'Hello, World! This is a test string.' [1,3,4](@ref)

# (2) 将所有字符转换为大写
s3_upper = s3_stripped.upper()
print(f"(2) 转换为大写: '{s3_upper}'")  # 输出: 'HELLO, WORLD! THIS IS A TEST STRING.' [6,7](@ref)

# (3) 查找子串 "test" 的起始下标
substring = "TEST"  # 注意：因已转大写，需匹配大写形式
start_index = s3_upper.find(substring)
print(f"(3) 'TEST'起始下标: {start_index}")  # 输出: 24 [9,10](@ref)

# (4) 将 "TEST" 替换为 "PRACTICE"
s3_replaced = s3_upper.replace("TEST", "PRACTICE")
print(f"(4) 替换后: '{s3_replaced}'")  # 输出: 'HELLO, WORLD! THIS IS A PRACTICE STRING.' [1,4](@ref)

# (5) 分割字符串并用 "-" 连接
words = s3_replaced.split()  # 默认按空格分割
s3_joined = "-".join(words)
print(f"(5) 分割后连接: '{s3_joined}'")  # 输出: 'HELLO,-WORLD!-THIS-IS-A-PRACTICE-STRING.' [1,2](@ref)