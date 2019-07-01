from datetime import datetime
import time


# 获取系统当前时间
now_time = datetime.now()
print(now_time)

# 获取当前日期
print(now_time.date())

# 获取当前时间
print(now_time.time())
print("今天时间：", datetime.today())
# 年月日时分秒都可以获取到
print("年:", now_time.year)
print("月:", now_time.month)
print("日:", now_time.day)
print("毫秒:", now_time.microsecond)


print("====================================")
# 获取到的是时间戳
print(time.time())




