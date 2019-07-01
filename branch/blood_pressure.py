high = int(input("请输入测量的高压值："))
low = int(input("请输入测量的低压值："))

if (60 < low < 90) and (90 < high < 140):
    print("您的血压正常，请保持良好的生活习惯。")
else:
    if low <= 60:
        print("您的低压过低！")
    elif high <= 90:
        print("您的高压过低")
    else:
        print("你的血压超标")
