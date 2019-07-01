year = input("请输入正确的年份：")
if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
    print("{}年是闰年".format(year))
else:
    print("{}年不是闰年".format(year))
