import random
import sys
from datetime import datetime


# 打印游戏名字
def guide_page(guide_world):
    print("{}{}{}".format("*" * 20, guide_world, "*" * 20))


# 判断内容是否为数字类型
def all_num(n):
    return n.isdigit() == 1


# 判断数据合法性
def num_legal(ls):
    number1 = int(ls[0])
    number2 = int(ls[-1])
    if number1 == number2:
        print("您输入的区间数字相同！！请重新启动程序。")
        sys.exit()
    elif number1 > number2:
        print("您输入的区间数字大小有误！！请重新启动程序。")
        sys.exit()
    else:
        return 1


# 生成随机数区间列表并返回一个随机数
def set_final_num(num1, num2):
    num_list = [num1, num2]
    # filter函数返回符合条件的数值
    all_num_list = list(filter(all_num, num_list))
    if len(all_num_list) == len(num_list):
        num_legal_result = num_legal(all_num_list)
        if num_legal_result == 1:
            print("所产生的随机数区间为：{}".format(all_num_list))
            random_number = random.randint(int(all_num_list[0]), int(all_num_list[-1]))
            return random_number
    else:
        print("您输入的字符为非数字字符，请重新启动！")
        sys.exit()


# 判断用户猜的数字是否在有效区间内
def check_num_legal(num):
    if num not in range(int(i), int(j) + 1):
        return 1


# 写入用户每次的猜测记录
def write_record(times, value):
    date = datetime.now()
    file_name = "record.txt"
    with open(file_name, "a", encoding="utf-8") as f:
        f.write("{}：第{}次您猜测的数字为{}".format(date, times, value))
        f.write("\n")


# 编写游戏规则
def main(rand1):
    temp = rand1
    count = 0
    while True:
        count += 1
        number = int(input("请继续输入您猜测的数字："))
        write_record(count, number)
        print("*" * 10)
        if check_num_legal(number) == 1:
            print("对不起您输入的数字未在指定区间！！！")
            continue
        elif number > temp:
            print("Higher than the answer")
        elif number < temp:
            print("lower than the answer")
        else:
            print("恭喜您！只用了{}次机会就赢得了游戏".format(count))
            break


if __name__ == "__main__":
    guide_page("欢迎进入数字猜猜猜小游戏")
    i = input("数字区间起始值：")
    j = input("数字区间终止值：")
    r_number = set_final_num(i, j)
    main(r_number)
