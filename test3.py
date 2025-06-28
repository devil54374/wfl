# 生成1-100的整数列表
numbers = [i for i in range(1, 101)]
print([x for x in range(2, 101, 2)])

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))


original_list = [3, 2, 1, 2, 4, 3]
result = remove_duplicates(original_list)
print(result)  # 输出: [3, 2, 1, 4]

keys = ["a", "b", "c"]
values = [1, 2, 3]
merged_dict = dict(zip(keys, values))
print(merged_dict)  # 输出: {'a': 1, 'b': 2, 'c': 3}


# 定义元组
student = ("张三", 20, 90)

# 解包元组
name, age, score = student

# 输出各字段
print(f"姓名: {name}")    # 输出: 姓名: 张三
print(f"年龄: {age}")     # 输出: 年龄: 20
print(f"成绩: {score}")   # 输出: 成绩: 90