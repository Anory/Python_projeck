print("欢迎使用某某某收银系统")
goods = input("请输入商品：")
price = float(input("请输入商品单价："))
num = int(input("请输入商品数量："))
pay_type = int(input("请选择支付类型："))
if pay_type == 1:
    total_price = price * num * 0.9 * 0.95
else:
    total_price = price * num * 0.9

print("您需要支付的金额为：", total_price)
