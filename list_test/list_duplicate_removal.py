# 列表去重并降序排序
list1 = [23, 98, 56, 55, 76, 98, 55]
# 定义list2为空列表
list2 = []
# 循环遍历list1
for i in list1:
    # if判断list1中的每个元素不在list2中
    if i not in list2:
        # 将元素追加到list2中
        list2.append(i)
# 使用sort对list2进行降序排序
list2.sort(reverse=True)
print(list2)
