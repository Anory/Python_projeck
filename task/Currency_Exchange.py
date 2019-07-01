service_menu = {"1": "人民币转换美元", "2": "美元转换人民币", "3": "人民币转换欧元", "0": "结束程序"}

# 在不满足条件的情况下一直循环此业务代码
while True:
    print("*" * 10, "欢迎使用货币转换系统", "*" * 10)
    for k, v in service_menu.items():
        print(k, ".", v)
    Your_Choice = input("请您选择需要的服务：")
    if Your_Choice == "1":
        print("~" * 30)
        print("欢迎使用人民币转换美元服务")
        your_money = input("请输入您需要转换的人民币金额：")
        print("您需要转换的人民币为：{}元".format(your_money))
        RMB_to_US = int(your_money) / 6.72
        print("兑换成美元为：{:0.2f}$".format(RMB_to_US))
        print("=" * 20)
    elif Your_Choice == "2":
        print("~" * 30)
        print("欢迎使用美元转换人民币服务")
        your_money = input("请输入您需要转换的美元金额：")
        print("您需要转换的美元为：{}$".format(your_money))
        US_to_RMB = int(your_money) * 6.72
        print("兑换成人民币为：{:0.2f}￥".format(US_to_RMB))
        print("=" * 20)
    elif Your_Choice == "3":
        print("~" * 30)
        print("欢迎使用人民币转换欧元服务")
        your_money = input("请输入您需要转换的欧元金额：")
        print("您需要转换的人民币为：{}￥".format(your_money))
        RMB_to_EUR = int(your_money) * 0.13
        print("兑换成欧元为：{:0.2f}€".format(RMB_to_EUR))
        print("=" * 20)
    elif Your_Choice == "0":
        print("感谢您的使用，祝您生活愉快，再见！")
        break
    else:
        print("您输入的选择有误，请重新输入！")
        continue
