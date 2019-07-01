from datetime import datetime, date, time, timedelta


# 自定义日期和时间
d = datetime(2019, 6, 27, 16, 40, 59)
print(d)

# 自定义日期需要导入date模块
d1 = date(2019, 6, 27)
print(d1)

# 自定义时间需要导入time模块
d2 = time(16, 25, 59)
print(d2)

print("===========================")

# 时间、日期和字符串之间的互相转换

# 1、字符串转换为datetime对象，方便获取年月日时分秒
ds = "2019-6-27 16:50:39"
ds_t = datetime.strptime(ds, "%Y-%m-%d %H:%M:%S")
print(type(ds_t))
# 格式化字符之间的连接符要对应给定的字符串连接符号
# 比如：
# ds = "2019/6-/27T16:50:39"
# ds_t = datetime.strptime(ds, "%Y/%m/%dT%H:%M:%S")
print(ds_t)
print("年:{}月:{}日:{}".format(ds_t.year, ds_t.month, ds_t.day))

# 2、把datetime对象转换为字符串
n = datetime.now()
print(n)
# 也可以单独只转换其中的年或月或其他时间(时间的连接符也可以是其他字符)
# n_str = n.strftime("%Y-%m/%d")
# n_str = n.strftime("%Y")
n_str = n.strftime("%Y/%m-%d %H:%M:%S")
print(type(n_str))
print(n_str)

# 3、datetime之间的加减操作，需要导入timedelta模块
# 加
n_time = datetime.today()
print(n_time)
next_time = n_time + timedelta(days=1, hours=1, minutes=15, seconds=56, microseconds=35)  # 天、时、分、秒、毫秒都可以加
print(next_time)

# 减
d1 = datetime(2019, 6, 27, 19, 40)  # 自定义时间日期
d2 = datetime(2019, 6, 29, 19, 40)

d3 = d2 - d1
print(type(d3))  # 是一个timedelta对象所有可以用 d3.days 获取到数据
print(d3.days)  # 相差两天

