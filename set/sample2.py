# 集合的增删改查

# 集合的遍历
college1 = {"法律", "医学", "科学", "法学"}
for c in college1:
    print(c)

# 判断元素是否存在
print("法律" in college1)

# 集合不支持按索引读取数据
# print(college1[3])

# 新增数据，add一次只能添加一个元素
college1.add("文学")  # 随机添加到原来的集合里面
print(college1)

# update一次可添加多个元素
college1.update(("工程学", "人工智能学"))
print(college1)

# 集合是不支持在原有的元素进行更新操作的， 只能先删除原有元素在add添加新的元素
# remove 如果删除不存在的元素时会报错
# college1.remove("法律")
# discard 如果遇到不存在的元素时会忽略删除操作
college1.discard("社会学")
college1.add("美学")
print(college1)
