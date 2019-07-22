# 字典写操作

employee = {"name": "杨过", "sex": "男", "hiredate": "1990-06-05", "grade": "A", "job": "销售"}

# 单个更新
employee["add"] = "新增的"
print(employee)
# 多个更新
employee.update(sex="女", name="杨梅")
print(employee)


# 字典的新增操作和更新操作完全相同，秉承有则更新无则新增
