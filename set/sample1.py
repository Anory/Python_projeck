# set的转换可以是列表，元组，字典，字符串， 但是其中转换的数据不能包含int类型的数据
# 集合间的关系操作

s1 = {1, 2, 3, 4, 5}
s2 = {5, 4, 3, 2, 1}

# 判断两个集合是否相等
print(s1 == s2)

s3 = {4, 5, 6, 7}
s4 = {1, 2, 3, 4, 5, 6, 7, 8}
# issubset 判断是否为子集
print(s3.issubset(s4))
# issuperset 判断是否为父集
print(s4.issuperset(s3))
# isdisjoint 判断两个函数是否有存在重复的元素
# 有则返回False， 没有则返回True
s5 = {8}
s6 = {3, 4, 5, 6}
print(s5.isdisjoint(s6))
