# 列表新增删除修改（也叫写操作）

name_list = ["张三", "李四", "王五", "赵六", "孙斌", "王五"]
# 列表元素追加
name_list.append("二狗")
print(name_list)
# 列表插入
name_list.insert(2, "熊大")
print(name_list)
# 用insert实现append的功能
name_list.insert(len(name_list), "熊二")
print(name_list)

# 列表更新(替换列表原来的元素)
name_list[1] = "周十"
print(name_list)
# 范围更新
name_list[1: 3] = ["杨大", "杨桂"]
print(name_list)

# 列表删除
# 按内容删除
name_list.remove("杨大")
print(name_list)
# 按索引值删除
name_list.pop(1)
print(name_list)
# 范围删除
name_list[4: 6] = []
print(name_list)

# 统计元素在列表出现的次数
count = name_list.count("王五")
print(count)

# 追加操作
# append是将整个类表追加到原来的列表里面形成一个二维列表， extend是将列表里面的元素追加到原来的列表里面形成一个新的列表
name_list.append(["钱大", "小明"])
print(name_list)

name_list.extend(["钱大", "小明"])
print(name_list)

# 判断元素是否在列表中（in 成员运算符）
b = "王五" in name_list
print(b)

# 复制列表,新的列表不受原列表影响
name_list1 = name_list.copy()
print(name_list1)


# 清空列表元素返回空类表
name_list.clear()
print(name_list)
