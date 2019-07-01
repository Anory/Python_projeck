# 函数的使用技巧


# 形参和默认参数
def calc_exchange_rate(amt, source, target="USD"):
    if source == "RMB" and target == "USD":
        result = amt / 6.71
        print("换算成功！")
        return result


def heath_check(name, sex, age, height, hr, hbp):
    print("身体状况良好")


# 关键字参数传参
print(heath_check(name="张飞", sex="男", age=18, height=1.98, hr=100, hbp=200))


# 星号表示之后所有的参数传参时必须使用关键字传参
def heath_check1(name, sex, *, age, height, hr, hbp):
    print("身体状况良好")


print(heath_check("张飞", "男", age=18, height=1.98, hr=100, hbp=200))

